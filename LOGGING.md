# Logging Standards and Guidelines

## Overview

This document defines logging standards, formats, and best practices for the Binance Crypto Trading Bot. Proper logging is essential for monitoring, debugging, and maintaining the trading system.

## Log Levels

### CRITICAL
- Bot shutdown due to critical errors
- API key revocation or authentication failures
- System-wide failures that require immediate attention

**Example:**
```python
app_logger.critical("CRITICAL ERROR for BTCUSDT: API key invalid - stopping bot")
```

### ERROR
- Trading operation failures
- Data corruption or file system errors
- Network errors that affect functionality

**Example:**
```python
app_logger.error(f"Failed to save positions: {e}", exc_info=True)
```

### WARNING
- Recoverable errors or degraded functionality
- Missing data or configuration issues
- Performance concerns

**Example:**
```python
app_logger.warning("Failed to get current price for BTCUSDT. Skipping iteration.")
```

### INFO
- Normal operation events
- Trading decisions and actions
- System state changes

**Example:**
```python
app_logger.info("✅ Circuit Breaker initialized (threshold=3, cooldown=300s)")
```

### DEBUG
- Detailed execution flow
- Variable values and intermediate calculations
- Development and troubleshooting information

**Example:**
```python
app_logger.debug(f"Asset rules cache cleared after exchange info update")
```

## Log Format Standards

### Standard Message Format
```
[TIMESTAMP] [LEVEL] [LOGGER] MESSAGE
```

### Trading Operations Format
```
[TIMESTAMP] [LEVEL] [trade] [SYMBOL] ACTION: DETAILS
```

**Examples:**
```
2025-12-13 10:30:15 INFO trade [BTCUSDT] Entry price: $50000.00, Current: $51000.00, PnL: 2.00%
2025-12-13 10:30:16 INFO trade [BTCUSDT] Take Profit triggered (2.00%) - executing sell
2025-12-13 10:30:17 INFO trade [BTCUSDT] Sell completed: 0.001 BTC @ $51000.00, PnL: +$1.00
```

### Error Context Format
Include relevant context in error messages:
```python
app_logger.error(
    f"Trading error for {symbol}: {error}",
    extra={
        "symbol": symbol,
        "error_category": category,
        "trade_quantity": str(quantity),
        "trade_price": str(price)
    }
)
```

## Structured Logging Examples

### Bot Startup
```python
app_logger.info(
    f"✅ Bot initialized successfully "
    f"(mode={'TESTNET' if is_testnet else 'MAINNET'}, "
    f"version={bot_version})"
)
```

### Trading Decision
```python
trade_logger.info(
    f"[{symbol}] Trading decision: {action} "
    f"(RSI: {rsi:.2f}, MA_short: {ma_short:.4f}, MA_long: {ma_long:.4f})"
)
```

### Error Handling
```python
app_logger.error(
    f"Decision matrix error for {symbol}: {error}",
    extra={
        "symbol": symbol,
        "error_type": type(error).__name__,
        "circuit_breaker_state": circuit_breaker.get_state(symbol)
    }
)
```

### Performance Metrics
```python
app_logger.info(
    f"Iteration completed in {duration:.2f}s "
    f"(processed {symbol_count} symbols, {trade_count} trades)"
)
```

## Log Rotation and Retention

### File Structure
```
logs/
├── mainnet/
│   ├── activity.log      # Current log file
│   ├── activity.log.1    # Previous day
│   ├── activity.log.2    # 2 days ago
│   └── ...
└── testnet/
    ├── activity.log
    ├── activity.log.1
    └── ...
```

### Rotation Policy
- **Size-based rotation**: 10MB per file
- **Time-based rotation**: Daily at midnight
- **Retention period**: 30 days
- **Compression**: Older files compressed with gzip

### Configuration Example
```python
import logging.handlers

handler = logging.handlers.RotatingFileHandler(
    filename='logs/mainnet/activity.log',
    maxBytes=10*1024*1024,  # 10MB
    backupCount=30,         # 30 days
    encoding='utf-8'
)
```

## Logger Configuration

### Main Application Logger
```python
app_logger = logging.getLogger("app")
app_logger.setLevel(logging.INFO)
```

### Trading Logger
```python
trade_logger = logging.getLogger("trade")
trade_logger.setLevel(logging.INFO)
```

### Module-Specific Loggers
```python
# Decision Matrix
dm_logger = logging.getLogger("decision_matrix")

# Circuit Breaker
cb_logger = logging.getLogger("circuit_breaker")

# Data Manager
data_logger = logging.getLogger("data_manager")
```

## Best Practices

### DO
- Use appropriate log levels consistently
- Include relevant context in messages
- Use structured logging for complex data
- Log both successful and failed operations
- Include timing information for performance monitoring
- Use exc_info=True for exception logging

### DON'T
- Log sensitive information (API keys, private data)
- Use print() statements instead of logging
- Log at DEBUG level in production without rotation
- Include passwords or tokens in log messages
- Log inside tight loops without rate limiting

### Security Considerations
```python
# ✅ GOOD: Mask sensitive data
app_logger.info(f"API key configured: {api_key[:8]}***")

# ❌ BAD: Expose sensitive data
app_logger.info(f"API key: {api_key}")
```

### Performance Logging
```python
import time

start_time = time.time()
# ... operation ...
duration = time.time() - start_time

app_logger.info(f"Operation completed in {duration:.3f}s")
```

## Monitoring and Alerting

### Critical Error Patterns
Monitor logs for these patterns that require immediate attention:
- `CRITICAL ERROR`
- `API key invalid`
- `Circuit breaker OPEN`
- `Failed to save positions`
- `Bot shutdown`

### Performance Monitoring
Track these metrics from logs:
- Iteration duration
- API response times
- Error rates by category
- Trading frequency and success rates

### Log Analysis Tools
Recommended tools for log analysis:
- **grep/awk**: Basic pattern matching
- **ELK Stack**: Elasticsearch, Logstash, Kibana
- **Grafana**: Visualization and alerting
- **Custom scripts**: Python/PowerShell for specific analysis

## Example Log Output

```
2025-12-13 10:30:00 INFO app ✅ Bot initialized successfully (mode=TESTNET, version=2.0)
2025-12-13 10:30:01 INFO app --- Starting new iteration (10:30:01) ---
2025-12-13 10:30:02 INFO trade Checking sell opportunities...
2025-12-13 10:30:03 INFO trade [BTCUSDT] Entry price: $50000.00, Current: $51000.00, PnL: 2.00%
2025-12-13 10:30:04 INFO trade [BTCUSDT] Take Profit triggered (2.00%) - executing sell
2025-12-13 10:30:05 INFO trade [BTCUSDT] Sell completed: 0.001 BTC @ $51000.00, PnL: +$1.00 USDT
2025-12-13 10:30:06 INFO app Sell check completed.
2025-12-13 10:30:07 INFO app Rebalancing enabled. Checking buy conditions...
2025-12-13 10:30:08 INFO trade Current USDT percentage: 45.50%. Buy trigger: 35%
2025-12-13 10:30:09 INFO trade Rebalancing triggered. Looking for assets to buy...
2025-12-13 10:30:10 INFO app Buy check completed.
2025-12-13 10:30:11 INFO app Iteration completed in 11.2s
```

This logging standard ensures consistent, informative, and actionable log output across the entire trading bot system.