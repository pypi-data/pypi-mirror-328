# SurferCID API Client

A Python client for interacting with the SurferCID API. This client provides easy access to SurferCID's services including purchasing accounts, creating and refreshing LTokens, checking orders, and managing balance.

## Project Structure

```
surfercid_client/
├── models.py           # Data models and response types
├── surfercid_client.py # Main API client implementation
└── requirements.txt    # Project dependencies
```

## Installation

1. Install via pip:
```bash
pip install surfercid-client
```

## Usage

```python
from surfercid import SurferCIDClient
from surfercid.models import LTokenAccount, Status

# Initialize the client
client = SurferCIDClient(api_key="your_api_key_here")

# Get stock information for a product
stock_info = client.get_stock("Ltoken_create")
print("Stock Info: ", stock_info)

# Check account balance
balance = client.get_balance()
print("Balance: ", balance)

# Create new LTokens
creation_order = client.create_token(quantity=1)
print(f"Order ID: {creation_order.order_id}")

# Wait for token creation to complete
order = client.get_task_status(creation_order.order_id, wait=True)
if order.status == Status.SUCCESS:
    for account in order.accounts:
        if isinstance(account, LTokenAccount):
            print(f"Token created: {account.to_format()}")
            # Outputs: mac:XX:XX:XX:XX:XX:XX|wk:NONE0|platform:1|rid:XXX|name:XXX|cbits:1536|playerAge:25|token:XXX|vid:XXX

# Example of refreshing tokens
if isinstance(account, LTokenAccount):
    refreshed = client.refresh_token(account)
    print(f"Refreshed token: {refreshed.to_format()}")
```

## Available Methods

### Token Creation and Management
- `create_token(quantity: int = 1) -> OrderResponse`: Create new LTokens
- `get_task_status(order_id: int, wait: bool = False) -> OrderResponse`: Check token creation status
- `refresh_token(token_data: Union[str, LTokenAccount]) -> LTokenAccount`: Refresh an LToken

### Account Management
- `get_stock(product_name: str) -> Dict[str, Any]`: Get stock information for a specific product
- `get_balance() -> float`: Get current account balance
- `purchase(product_name: str, quantity: int) -> OrderResponse`: Purchase products
- `get_order(order_id: int) -> OrderResponse`: Get details of a specific order
- `get_orders(limit: Optional[int] = None) -> List[OrderResponse]`: Get list of orders

## Data Models

### LTokenAccount
```python
@dataclass
class LTokenAccount(Account):
    created_at: str
    mac: str
    name: str
    platform: str
    rid: str
    token: str
    wk: str = "NONE0"
    cbits: int = 1536
    player_age: int = 25
    vid: str = ""

    def to_format(self) -> str:
        """Convert to the new token format"""
        return f"mac:{self.mac}|wk:{self.wk}|platform:{self.platform}|rid:{self.rid}|name:{self.name}|cbits:{self.cbits}|playerAge:{self.player_age}|token:{self.token}|vid:{self.vid}"
```

### OrderResponse
```python
@dataclass
class OrderResponse:
    accounts: List[Account]
    message: str
    success: bool
    cost: float
    order_id: int
    order_date: datetime
    processing: bool = False
    quantity: int = 0
    refund_amount: float = 0
    status: Status = Status.FAILED
```

### Status Enum
```python
class Status(Enum):
    SUCCESS = "success"
    FAILED = "failed"
    PROCESSING = "processing"
```

## Error Handling

The client includes comprehensive error handling for various scenarios:

```python
from requests.exceptions import RequestException

try:
    # Create a new token
    order = client.create_token(quantity=1)
    status = client.get_task_status(order.order_id, wait=True)
    
    if status.status == Status.SUCCESS:
        print("Token created successfully!")
    elif status.status == Status.FAILED:
        print(f"Creation failed: {status.message}")
    
except RequestException as e:
    print(f"API request failed: {e}")
except ValueError as e:
    print(f"Invalid input or response: {e}")
```

## Token Format

The new token format includes additional fields for enhanced functionality:
```
mac:XX:XX:XX:XX:XX:XX|wk:NONE0|platform:1|rid:XXX|name:XXX|cbits:1536|playerAge:25|token:XXX|vid:XXX
```

Where:
- `mac`: MAC address
- `wk`: World key (default: NONE0)
- `platform`: Platform identifier
- `rid`: Resource identifier
- `name`: Account name
- `cbits`: Client bits (default: 1536)
- `playerAge`: Player age (default: 25)
- `token`: Authentication token
- `vid`: Version identifier