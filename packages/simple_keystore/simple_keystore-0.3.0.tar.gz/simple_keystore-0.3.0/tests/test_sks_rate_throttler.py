import pytest
from unittest.mock import Mock, patch
from datetime import timedelta
from simple_keystore import SKSRateThrottler

# Mock Redis client
@pytest.fixture
def mock_redis():
    with patch('redis.Redis') as MockRedis:
        redis_instance = MockRedis.return_value
        redis_instance.pipeline.return_value = Mock()
        yield redis_instance

# Test class setup
def test_initialization(mock_redis):
    """Test that SKSRateThrottler initializes correctly."""
    throttler = SKSRateThrottler(
        api_key_id=1,
        number_of_uses_allowed=1000,
        amount_of_time=timedelta(hours=1),
        redis_host="localhost",
        redis_port=6379,
        redis_db=0
    )

    assert throttler.api_key_id == 1
    assert throttler.rate_limit_uses_allowed == 1000
    assert isinstance(throttler.rate_limit_timedelta, timedelta)
    assert throttler.redis == mock_redis

def test_set_rate_limit_valid(mock_redis):
    """Test setting a valid rate limit."""
    throttler = SKSRateThrottler(
        api_key_id=1,
        number_of_uses_allowed=500,
        amount_of_time=timedelta(minutes=30),
        redis_host="localhost",
        redis_port=6379,
        redis_db=0
    )

    throttler.set_rate_limit(1000, timedelta(hours=1))

    assert throttler.rate_limit_uses_allowed == 1000
    assert throttler.rate_limit_timedelta == timedelta(hours=1)

def test_set_rate_limit_invalid(mock_redis):
    """Test that setting invalid rate limits raises ValueError."""
    throttler = SKSRateThrottler(
        api_key_id=1,
        number_of_uses_allowed=1000,
        amount_of_time=timedelta(hours=1),
        redis_host="localhost",
        redis_port=6379,
        redis_db=0
    )

    with pytest.raises(ValueError, match="Number of uses allowed must be positive"):
        throttler.set_rate_limit(0, timedelta(hours=1))

    with pytest.raises(ValueError, match="Amount of time must be positive"):
        throttler.set_rate_limit(1000, timedelta(seconds=0))

def test_is_rate_limited_not_limited(mock_redis):
    """Test that a new API key is not rate limited."""
    pipe = mock_redis.pipeline.return_value
    pipe.execute.return_value = [None, 0, None, None]  # zremrangebyscore, zcard, zadd, expire

    throttler = SKSRateThrottler(
        api_key_id=1,
        number_of_uses_allowed=1000,
        amount_of_time=timedelta(hours=1),
        redis_host="localhost",
        redis_port=6379,
        redis_db=0
    )

    assert not throttler.is_rate_limited()
    pipe.zadd.assert_called_once()  # Ensure new request was added
    pipe.expire.assert_called_once()  # Ensure expiration was set

def test_is_rate_limited_exceeds_limit(mock_redis):
    """Test that the rate limit is enforced when exceeded."""
    pipe = mock_redis.pipeline.return_value
    pipe.execute.return_value = [None, 1001, None, None]  # Simulate 1001 requests already in window

    throttler = SKSRateThrottler(
        api_key_id=1,
        number_of_uses_allowed=1000,
        amount_of_time=timedelta(hours=1),
        redis_host="localhost",
        redis_port=6379,
        redis_db=0
    )

    assert throttler.is_rate_limited()
    pipe.zadd.assert_called_once()  # Still adds the new request

def test_sliding_window_behavior(mock_redis):
    """Test that old requests are removed from the sliding window."""
    pipe = mock_redis.pipeline.return_value
    # Simulate initial state with some old and new requests
    pipe.execute.side_effect = [
        [None, 5, None, None],  # First call: 5 requests in window
        [None, 3, None, None],  # Second call: after removing old, only 3 remain
    ]

    throttler = SKSRateThrottler(
        api_key_id=1,
        number_of_uses_allowed=1000,
        amount_of_time=timedelta(minutes=5),  # Short window for testing
        redis_host="localhost",
        redis_port=6379,
        redis_db=0
    )

    # First check
    assert not throttler.is_rate_limited()  # Should not be limited (5 < 1000)
    pipe.zremrangebyscore.assert_called()  # Ensure old data was cleaned

    # Simulate time passing (mock would need adjustment for real time)
    pipe.reset_mock()
    pipe.execute.return_value = [None, 3, None, None]  # Fewer after cleanup

    assert not throttler.is_rate_limited()  # Still not limited

def test_redis_failure(mock_redis):
    """Test behavior when Redis connection fails."""
    mock_redis.pipeline.side_effect = Exception("Redis connection failed")

    throttler = SKSRateThrottler(
        api_key_id=1,
        number_of_uses_allowed=1000,
        amount_of_time=timedelta(hours=1),
        redis_host="localhost",
        redis_port=6379,
        redis_db=0
    )

    with pytest.raises(Exception, match="Redis connection failed"):
        throttler.is_rate_limited()

# Run tests with pytest
if __name__ == "__main__":
    pytest.main(["-v", __file__])