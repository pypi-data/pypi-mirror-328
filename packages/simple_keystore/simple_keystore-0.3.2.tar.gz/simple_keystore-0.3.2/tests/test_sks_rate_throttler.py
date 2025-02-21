import pytest
from unittest.mock import Mock, patch
from datetime import timedelta
import time

from simple_keystore import SKSRateThrottler

# Mock Redis client
@pytest.fixture
def mock_redis():
    with patch('redis.Redis') as MockRedis:
        redis_instance = MockRedis.return_value
        redis_instance.script_load.return_value = "mock_script_sha"  # Mock the script SHA
        yield redis_instance

# Test class setup
def test_initialization(mock_redis):
    """Test that SKSRateThrottler initializes correctly with Lua script loading."""
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
    mock_redis.script_load.assert_called_once()  # Ensure Lua script was loaded

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
    mock_redis.evalsha.return_value = 1  # Simulate success (not rate-limited)

    throttler = SKSRateThrottler(
        api_key_id=1,
        number_of_uses_allowed=1000,
        amount_of_time=timedelta(hours=1),
        redis_host="localhost",
        redis_port=6379,
        redis_db=0
    )

    # Use a fixed time for predictability in testing
    with patch('time.time', return_value=1600000000):  # Mock time to a fixed value
        assert not throttler.is_rate_limited()
        mock_redis.evalsha.assert_called_once_with(
            throttler.lua_increment_script_sha,
            1,
            "ratelimit:1",
            "1600000000",  # Fixed current time
            str(1600000000 - timedelta(hours=1).total_seconds()),  # Window start
            "1000",
            str(timedelta(hours=1).total_seconds())
        )

def test_is_rate_limited_exceeds_limit(mock_redis):
    """Test that the rate limit is enforced when exceeded."""
    mock_redis.evalsha.return_value = 0  # Simulate rate limit exceeded

    throttler = SKSRateThrottler(
        api_key_id=1,
        number_of_uses_allowed=1000,
        amount_of_time=timedelta(hours=1),
        redis_host="localhost",
        redis_port=6379,
        redis_db=0
    )

    # Use a fixed time for predictability in testing
    with patch('time.time', return_value=1600000000):  # Mock time to a fixed value
        assert throttler.is_rate_limited()
        mock_redis.evalsha.assert_called_once_with(
            throttler.lua_increment_script_sha,
            1,
            "ratelimit:1",
            "1600000000",  # Fixed current time
            str(1600000000 - timedelta(hours=1).total_seconds()),  # Window start
            "1000",
            str(timedelta(hours=1).total_seconds())
        )

def test_sliding_window_behavior(mock_redis):
    """Test that old requests are removed from the sliding window."""
    # First call: not rate-limited, some requests exist
    mock_redis.evalsha.side_effect = [1, 1]  # Both calls succeed

    throttler = SKSRateThrottler(
        api_key_id=1,
        number_of_uses_allowed=1000,
        amount_of_time=timedelta(minutes=5),  # Short window for testing
        redis_host="localhost",
        redis_port=6379,
        redis_db=0
    )

    # Use a fixed time for predictability
    with patch('time.time', return_value=1600000000):
        # First check
        assert not throttler.is_rate_limited()  # Should not be limited
        mock_redis.evalsha.assert_called()

        # Simulate time passing (no need to mock time further, Lua handles window)
        mock_redis.evalsha.reset_mock()
        mock_redis.evalsha.return_value = 1  # Still not limited

        assert not throttler.is_rate_limited()  # Still not limited

def test_redis_failure(mock_redis):
    """Test behavior when Redis connection fails during initialization."""
    mock_redis.script_load.side_effect = Exception("Redis connection failed")

    with pytest.raises(RuntimeError, match="Failed to load Lua script: Redis connection failed"):
        SKSRateThrottler(
            api_key_id=1,
            number_of_uses_allowed=1000,
            amount_of_time=timedelta(hours=1),
            redis_host="localhost",
            redis_port=6379,
            redis_db=0
        )

def test_wait_until_available(mock_redis):
    """Test blocking until the API key is available."""
    throttler = SKSRateThrottler(
        api_key_id=1,
        number_of_uses_allowed=1000,
        amount_of_time=timedelta(minutes=1),
        redis_host="localhost",
        redis_port=6379,
        redis_db=0
    )

    # Use a mock for time.time that increments continuously
    def time_generator():
        current_time = 0
        while True:
            yield current_time
            current_time += 1

    # Test that it eventually succeeds
    with patch('time.time') as mock_time, patch.object(mock_redis, 'evalsha') as mock_evalsha:
        mock_time.side_effect = time_generator()  # Infinite generator for time
        mock_evalsha.side_effect = [0, 0, 1]  # First two calls rate-limited, third succeeds

        result = throttler.wait_until_available(timeout=5)
        assert result is None  # wait_until_available doesn't return anything on success
        assert mock_evalsha.call_count == 3  # Should call 3 times (twice rate-limited, once succeeds)

    # Test timeout
    with patch('time.time') as mock_time, patch.object(mock_redis, 'evalsha') as mock_evalsha:
        mock_time.side_effect = time_generator()  # Reset infinite generator
        mock_evalsha.side_effect = iter([0] * 10)  # Always rate-limited for 10 calls (should timeout)

        with pytest.raises(TimeoutError, match="API key self.api_key_id=1 is still rate limited after the timeout period of 5s"):
            throttler.wait_until_available(timeout=5)

# Run tests with pytest
if __name__ == "__main__":
    pytest.main(["-v", __file__])