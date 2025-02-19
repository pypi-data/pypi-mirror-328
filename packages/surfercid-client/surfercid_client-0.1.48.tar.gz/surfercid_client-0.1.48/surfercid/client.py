"""
SurferCID API client implementation.
"""

from typing import Optional, Dict, Any, List, Union
from datetime import datetime
import requests
import time

from .models import (
    Account,
    CIDAccount,
    MailAccount,
    Status,
    UbiConnectAccount,
    LTokenAccount,
    OrderResponse,
)


class SurferCIDClient:
    """
    Client for interacting with the SurferCID API.
    
    This client provides methods to interact with all SurferCID API endpoints,
    including purchasing accounts, managing orders, and refreshing tokens.
    
    Example:
        >>> from surfercid import SurferCIDClient
        >>> client = SurferCIDClient(api_key="your_api_key")
        >>> order = client.purchase(product_name="ltoken", quantity=1)
        >>> for account in order.accounts:
        ...     print(account.to_format())
    """

    BASE_URL = "https://cid.surferwallet.net/publicApi"

    def __init__(self, api_key: str):
        """
        Initialize the SurferCID API client.
        
        Args:
            api_key (str): Your API key for authentication
        """
        self.api_key = api_key
        self.session = requests.Session()
        # Set default headers for all requests
        self.session.headers.update({
            "User-Agent": "SurferCID-Client/Python",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        })
        
    def __enter__(self):
        """Support for context manager protocol."""
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Cleanup when exiting context manager."""
        self.session.close()
        
    def close(self):
        """Close the session manually if not using context manager."""
        self.session.close()
        
    def _make_request(self, method: str, endpoint: str, data: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Make an HTTP request to the API.
        
        Args:
            method (str): HTTP method to use
            endpoint (str): API endpoint to call
            data (Dict[str, Any], optional): Request data. Defaults to None.
            
        Returns:
            Dict[str, Any]: API response data
            
        Raises:
            ValueError: If the API key is invalid or missing
            requests.exceptions.RequestException: If the API request fails
            RuntimeError: If the API returns an error response
        """
        if not self.api_key:
            raise ValueError("API key is required but not provided")

        url = f"{self.BASE_URL}/{endpoint}"
        
        if data is None:
            data = {}
            
        try:
            if method.upper() == "GET":
                # For GET requests, add apikey as query parameter
                params = {"apikey": self.api_key}
                if data:
                    params.update(data)
                response = self.session.get(url, params=params)
            else:
                # For other methods (POST, etc), add apikey to the JSON body
                data["apikey"] = self.api_key
                response = self.session.request(method, url, json=data)

            # Check for HTTP errors
            response.raise_for_status()

            # Parse response
            json_response = response.json()

            # Check for API-specific errors
            if not json_response.get("success", True):  # Some endpoints don't return success field
                error_msg = json_response.get("message", "Unknown API error")
                if "invalid api key" in error_msg.lower():
                    raise ValueError(f"Invalid API key: {error_msg}")
                elif "insufficient balance" in error_msg.lower():
                    raise ValueError(f"Insufficient balance: {error_msg}")
                elif response.status_code == 400:
                    raise ValueError(f"Bad request: {error_msg}")
                elif response.status_code == 404:
                    raise ValueError(f"Resource not found: {error_msg}")
                else:
                    raise RuntimeError(f"API error: {error_msg}")

            return json_response

        except requests.exceptions.RequestException as e:
            if "SSLError" in str(e):
                raise RuntimeError("SSL verification failed. Check your connection security.") from e
            elif "ConnectionError" in str(e):
                raise RuntimeError("Failed to connect to the API. Check your internet connection.") from e
            elif "Timeout" in str(e):
                raise RuntimeError("Request timed out. The API server might be slow or unreachable.") from e
            else:
                raise RuntimeError(f"Request failed: {str(e)}") from e
        except ValueError as e:
            if "JSONDecodeError" in str(type(e)):
                raise RuntimeError("Failed to parse API response as JSON") from e
            raise
    
    def refresh_token(self, token_data: Union[str, LTokenAccount]) -> LTokenAccount:
        """
        Refresh a token using the refreshToken endpoint.
        
        Args:
            token_data (Union[str, LTokenAccount]): Either a formatted token string (RID|MAC|PLATFORM|TOKEN)
                                                  or an LTokenAccount instance
            
        Returns:
            LTokenAccount: A new LTokenAccount instance with the refreshed token
            
        Raises:
            ValueError: If the token format is invalid
            RuntimeError: If the token refresh fails
            requests.exceptions.RequestException: If the API request fails
            
        Example:
            >>> try:
            ...     account = client.purchase(product_name="ltoken", quantity=1).accounts[0]
            ...     refreshed = client.refresh_token(account)
            ...     print(f"New token: {refreshed.token}")
            ... except ValueError as e:
            ...     print(f"Invalid token: {e}")
            ... except RuntimeError as e:
            ...     print(f"Refresh failed: {e}")
        """
        try:
            # Get original token parts for later use
            if isinstance(token_data, LTokenAccount):
                original_account = token_data
                token = token_data.token  # Just use the token value
            elif isinstance(token_data, str):
                # Parse the token string to get original values
                try:
                    parts = token_data.split('|')
                    if len(parts) < 4:
                        raise ValueError("Invalid token format. Expected: RID|MAC|PLATFORM|TOKEN")
                    original_account = LTokenAccount(
                        created_at=datetime.now().isoformat(),
                        rid=parts[0],
                        mac=parts[1],
                        platform=parts[2],
                        name="",  # We don't have this from the formatted string
                        token=parts[3]
                    )
                    token = parts[3]  # Just use the token part
                except (IndexError, ValueError) as e:
                    raise ValueError(f"Failed to parse token string: {str(e)}")
            else:
                raise ValueError("token_data must be either a string or LTokenAccount instance")

            data = {
                "token": token  # Only send the token value
            }
            
            try:
                response = self._make_request("POST", "refreshToken", data)
                
                # Get the new token from the response
                new_token = response.get("token")
                if not new_token:
                    raise ValueError("No token in response")
                
                # Create a new LTokenAccount with the refreshed token
                return LTokenAccount(
                    created_at=datetime.now().isoformat(),  # Update creation time to now
                    mac=original_account.mac,
                    name=original_account.name,
                    platform=original_account.platform,
                    rid=original_account.rid,
                    token=new_token
                )
            except (ValueError, RuntimeError) as e:
                raise RuntimeError(f"Token refresh failed: {str(e)}")
            
        except Exception as e:
            if isinstance(e, (ValueError, RuntimeError)):
                raise
            raise RuntimeError(f"Unexpected error during token refresh: {str(e)}")
    
    def _parse_account(self, acc_data: Dict[str, Any], product_type: Optional[str] = None) -> Account:
        """
        Parse account data into appropriate Account type.
        
        Args:
            acc_data (Dict[str, Any]): Raw account data
            product_type (Optional[str]): Product type if known
            
        Returns:
            Account: Parsed account object
            
        Raises:
            ValueError: If the account type cannot be determined
        """
        if product_type == "cid" or "growid" in acc_data:
            return CIDAccount(**acc_data)
        elif product_type == "mail" or ("mail" in acc_data and "password" in acc_data and len(acc_data) == 2):
            return MailAccount(**acc_data)
        elif product_type == "ubiconnect" or "email" in acc_data:
            return UbiConnectAccount(**acc_data)
        elif product_type == "ltoken" or all(key in acc_data for key in ["created_at", "mac", "name", "platform", "rid", "token"]):
            return LTokenAccount(**acc_data)
        elif product_type == "ltoken_create" or all(key in acc_data for key in ["created_at", "mac", "name", "platform", "rid", "token"]):
            return LTokenAccount(**acc_data)
        raise ValueError(f"Unknown account type: {acc_data}")
    
    def get_stock(self, product_name: str) -> Dict[str, Any]:
        """
        Get stock information for a specific product.
        
        Args:
            product_name (str): Name of the product (e.g., "ltoken", "old_account")
            
        Returns:
            Dict[str, Any]: Stock information containing:
                - available (int): Number of items in stock
                - price (float): Price per item
                - enabled (bool): Whether the product is enabled
            
        Example:
            >>> stock = client.get_stock("ltoken")
            >>> print(f"Available: {stock['available']}, Price: ${stock['price']}")
        """
        response = self._make_request("GET", "stock")
        
        # Convert product name to lowercase for case-insensitive comparison
        product_name = product_name.lower()
        
        # Search through products list
        for product in response.get("products", []):
            if product["name"].lower() == product_name:
                return {
                    "available": product["instock"],
                    "price": product["price"],
                    "enabled": product["enabled"]
                }
                
        # If product not found, return empty stock
        return {
            "available": 0,
            "price": 0,
            "enabled": False,
            "error": f"Product '{product_name}' not found"
        }

    def get_balance(self) -> float:
        """
        Get current balance of the account.
        
        Returns:
            float: Current balance
            
        Example:
            >>> balance = client.get_balance()
            >>> print(f"Current balance: ${balance}")
        """
        response = self._make_request("GET", "getBalance")
        return float(response.get("balance", 0))
    
    def purchase(self, product_name: str, quantity: int) -> OrderResponse:
        """
        Purchase products from the service.
        
        Args:
            product_name (str): Name of the product to purchase
            quantity (int): Number of items to purchase
            
        Returns:
            OrderResponse: Purchase response with order details
            
        Example:
            >>> order = client.purchase(product_name="ltoken", quantity=2)
            >>> for account in order.accounts:
            ...     print(account.to_format())
        """
        data = {
            "name": product_name,
            "quantity": quantity
        }
        
        response = self._make_request("POST", "purchase", data)
        accounts = [
            self._parse_account(acc_data, product_name)
            for acc_data in response.get("accounts", [])
        ]
            
        return OrderResponse(
            accounts=accounts,
            message=response.get("message", ""),
            success=response.get("success", False),
            cost=response.get("cost", 0),
            order_id=response.get("orderID", 0),
            order_date=datetime.fromisoformat(response.get("orderDate").replace('Z', '+00:00')),
            status=Status(response.get("status", "").lower())
        )
    
    def get_order(self, order_id: int) -> OrderResponse:
        """
        Get details of a specific order.
        
        Args:
            order_id (int): ID of the order to retrieve
            
        Returns:
            OrderResponse: Order details
            
        Example:
            >>> order = client.get_order(123)
            >>> print(f"Order cost: ${order.cost}")
        """
        data = {"orderID": order_id}
        response = self._make_request("GET", "getOrder", data)
        
        accounts = [
            self._parse_account(acc_data)
            for acc_data in response.get("accounts", [])
        ]
            
        return OrderResponse(
            accounts=accounts,
            message=response.get("message", ""),
            success=response.get("success", False),
            cost=response.get("cost", 0),
            order_id=response.get("orderID", 0),
            order_date=datetime.fromisoformat(response.get("orderDate").replace('Z', '+00:00'))
        )
    
    def get_orders(self, limit: Optional[int] = None) -> List[OrderResponse]:
        """
        Get list of orders.
        
        Args:
            limit (Optional[int]): Maximum number of orders to retrieve
            
        Returns:
            List[OrderResponse]: List of orders
            
        Example:
            >>> orders = client.get_orders(limit=5)
            >>> for order in orders:
            ...     print(f"Order {order.order_id}: ${order.cost}")
        """
        data = {}
        if limit is not None:
            data["limit"] = limit
            
        response = self._make_request("GET", "getOrders", data)
        orders = []
        
        for order_data in response.get("orders", []):
            accounts = [
                self._parse_account(acc_data)
                for acc_data in order_data.get("accounts", [])
            ]
                
            orders.append(OrderResponse(
                accounts=accounts,
                message=order_data.get("message", ""),
                success=order_data.get("success", False),
                cost=order_data.get("cost", 0),
                order_id=order_data.get("orderID", 0),
                order_date=datetime.fromisoformat(order_data.get("orderDate").replace('Z', '+00:00'))
            ))
            
        return orders 

    def create_token(self, quantity: int = 1) -> OrderResponse:
        """
        Create new LTokens using the Ltoken_create product.
        
        Args:
            quantity (int, optional): Number of tokens to create. Defaults to 1.
            
        Returns:
            OrderResponse: Creation order details
            
        Raises:
            ValueError: If the request is invalid
            RuntimeError: If the API returns an error
            
        Example:
            >>> response = client.create_token(quantity=1)
            >>> print(f"Order ID: {response.order_id}")
            >>> print(f"Status: {response.status}")
        """
        data = {
            "name": "Ltoken_create",
            "quantity": quantity
        }
        
        response = self._make_request("POST", "purchase", data)
        
        
        return OrderResponse(
            accounts=response.get("accounts", []),
            cost=float(response.get("cost", 0)),
            message=response.get("message", ""),
            order_date=datetime.fromisoformat(response.get("orderDate").replace('Z', '+00:00')),
            order_id=response.get("orderID", 0),
            processing=response.get("processing", False),
            quantity=response.get("quantity", 0),
            success=response.get("success", False),
            refund_amount=float(response.get("refundAmount", 0)),
            status=Status.PROCESSING if response.get("processing", False) else Status.from_str(response.get("status", "failed"))
        )

    def get_task_status(self, order_id: int, wait: bool = False, check_interval: float = 5.0) -> OrderResponse:
        """
        Check the status of a token creation order.
        
        Args:
            order_id (int): The order ID to check
            wait (bool, optional): Whether to wait for processing to complete. Defaults to False.
            check_interval (float, optional): How often to check status when waiting (in seconds). Defaults to 5.0.
            
        Returns:
            OrderResponse: The order response with current status
            
        Raises:
            ValueError: If the order ID is invalid
            RuntimeError: If the API returns an error
            
        Example:
            >>> creation = client.create_token(quantity=1)
            >>> status = client.get_task_status(creation.order_id, wait=True)
            >>> if status.status == Status.SUCCESS:
            ...     print("Token created successfully!")
        """
        while True:
            response = self._make_request("GET", "getOrder", {"orderID": order_id})
            
            accounts = [
                self._parse_account(acc_data)
                for acc_data in response.get("accounts", [])
            ]
             
            # Create OrderResponse with current status
            order = OrderResponse(
                accounts=accounts,
                message=response.get("message", ""),
                success=response.get("success", False),
                cost=float(response.get("cost", 0)),
                order_id=order_id,
                order_date=datetime.fromisoformat(response.get("orderDate").replace('Z', '+00:00')),
                processing=response.get("processing", False),
                quantity=response.get("quantity", 0),
                refund_amount=float(response.get("refundAmount", 0)),
                status=Status.PROCESSING if response.get("processing", False) else Status.from_str(response.get("status", "failed"))
            )
            
            # If not waiting or not processing anymore, return current status
            if not wait or not order.processing:
                return order
                
            time.sleep(check_interval)