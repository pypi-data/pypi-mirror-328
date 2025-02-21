# DMTAPI

A Python package for interacting with trading accounts and managing trades.

## Installation

```bash
pip install dmtapi
```

## Quick Start

```python
from dmtapi import DMTAPI
from dmtapi.models.trade_model import TradeSetup, TradeDirection, TakeProfit

# Initialize the API
api = DMTAPI(api_key="your_api_key")

# Get account information
account_info = await api.get_account_info(
    access_token="your_access_token",
)

# alternatively use api key
# account_info = await api.get_account_info(
#     login=123
#     server="your_server
# )

# Create and execute a trade
setup = TradeSetup(
    symbol="EURUSD",
    volume=0.1,
    direction=TradeDirection.buy,
    stop_loss=1.0500,
    take_profits=[
        TakeProfit(price=1.0600, close_pct=1.0)
    ]
)

result = await api.open_trade(
    setup=setup,
    access_token="your_access_token",
    login=12345,
    server="your_server"
)
```

## API Reference

### DMTAPI Class

The main class for interacting with the trading API.

#### Methods

- `get_account_info(access_token=None, login=None, server=None, api_key=None) -> TraderInfo`
    - Retrieves information about a specific trading account.
    - Returns a TraderInfo object containing account details.

- `get_all_accounts(api_key=None) -> list[TraderInfo]`
    - Retrieves information about all available trading accounts.
    - Returns a list of TraderInfo objects.

- `open_trade(setup, access_token, login, server, api_key=None) -> dict`
    - Opens a new trade based on the provided setup.
    - Returns a dictionary containing the trade result.

### Models

#### TradeSetup

Represents a trade setup configuration.

**Fields:**

- `symbol: str` - Trading symbol (e.g., "EURUSD")
- `volume: float` - Trading volume (0-100)
- `direction: TradeDirection` - Trade direction (buy/sell)
- `magic: int` - Magic number for trade identification (optional)
- `entry_price: float` - Entry price for the trade
- `stop_loss: float` - Stop loss price
- `sl_as_pip: float` - Stop loss in pips (takes priority over sl_as_pct)
- `sl_as_pct: float` - Stop loss as percentage
- `take_profits: list[TakeProfit]` - List of take profit levels
- `deviation: int` - Maximum price deviation (0-100)

#### TakeProfit

Represents a take profit configuration.

**Fields:**

- `price: float` - Take profit price level
- `close_pct: float` - Percentage of position to close (0-1)
- `tp_as_pip: float` - Take profit in pips
- `tp_as_pct: float` - Take profit as percentage

#### TraderInfo

Represents trading account information.

**Fields:**

- `name: str` - Account name
- `server: str` - Trading server
- `login: int` - Account login
- `server_type: str` - Server type (default: "mt5")
- `access_token: str` - Access token
- `inception_date: datetime` - Account creation date
- `starting_balance: float` - Initial account balance
- `currency: str` - Account currency
- `leverage: int` - Account leverage
- `balance: float` - Current balance
- `equity: float` - Current equity
- `margin: float` - Used margin
- `margin_free: float` - Free margin
- `status: AccountStatusEnum` - Account connection status

## Examples

### Getting Account Information

```python
api = DMTAPI(api_key="your_api_key")

# Using access token
account = await api.get_account_info(access_token="your_access_token")

# Using login and server
# account = await api.get_account_info(
#     login="your_login",
#     server="your_server"
# )

print(f"Account Balance: {account.balance}")
print(f"Account Equity: {account.equity}")
```

### Opening a Trade

```python
from dmtapi.models.trade_model import TradeSetup, TradeDirection, TakeProfit

# Create trade setup
setup = TradeSetup(
    symbol="EURUSD",
    volume=0.1,
    direction=TradeDirection.buy,
    stop_loss=1.0500,
    take_profits=[
        TakeProfit(price=1.0600, close_pct=0.5),
        TakeProfit(price=1.0700, close_pct=0.5)
    ]
)

# Open trade
result = await api.open_trade(
    setup=setup,
    access_token="your_access_token",
)
```