"""
Data models for the SurferCID API client.
"""

from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime
from enum import Enum


@dataclass
class Account:
    """Base class for account data types."""
    pass


@dataclass
class LTokenAccount(Account):
    """
    Account model for LToken product type.
    
    Attributes:
        created_at (str): ISO format timestamp of when the token was created
        mac (str): MAC address associated with the token
        name (str): Account name
        platform (str): Platform identifier
        rid (str): Resource identifier
        token (str): Authentication token
    """
    created_at: str
    mac: str
    name: str
    platform: str
    rid: str
    token: str
    wk:str="NONE0"
    cbits:int=1536
    player_age:int=25
    vid:str=""

    def to_format(self) -> str:
        """
        Convert the account data to key:value format.
        
        Returns:
            str: Formatted string in the format key:value
            
        Example:
            >>> account = LTokenAccount(...)
            >>> print(account.to_format())
            'mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:|name:fruincup|cbits:1536|playerAge:25|token:|vid:'
        """
        return f"mac:{self.mac}|wk:{self.wk}|platform:{self.platform}|rid:{self.rid}|name:{self.name}|cbits:{self.cbits}|playerAge:{self.player_age}|token:{self.token}|vid:{self.vid}"

    @classmethod
    def from_format(cls, formatted_str: str, name: str = "") -> "LTokenAccount":
        """
        Create an LTokenAccount instance from a formatted string.
        
        Args:
            formatted_str (str): String in key:value|key:value format
            name (str, optional): Account name. Defaults to empty string.
            
        Returns:
            LTokenAccount: New instance with the parsed data
            
        Raises:
            ValueError: If the string format is invalid
            
        Example:
            >>> token_str = "mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:|name:fruincup|cbits:1536|playerAge:25|token:|vid:"
            >>> account = LTokenAccount.from_format(token_str)
        """
        try:
            # Split into key-value pairs and create dictionary
            pairs = dict(pair.split(':', 1) for pair in formatted_str.strip().split('|'))
            
            # Create instance with required fields
            return cls(
                created_at=datetime.now().isoformat(),  # Set current time as creation time
                mac=pairs.get('mac', ''),
                name=pairs.get('name', name),  # Use provided name if not in string
                platform=pairs.get('platform', ''),
                rid=pairs.get('rid', ''),
                token=pairs.get('token', ''),
                wk=pairs.get('wk', 'NONE0'),
                cbits=int(pairs.get('cbits', '1536')),
                player_age=int(pairs.get('playerAge', '25')),
                vid=pairs.get('vid', '')
            )
        except Exception as e:
            raise ValueError(f"Failed to parse token string: {e}")


@dataclass
class CIDAccount(Account):
    """
    Account model for CID product type.
    
    Attributes:
        growid (str): Grow ID for the account
        password (str): Account password
        mail (str): Email address
        mail_pass (str): Email password
    """
    growid: str
    password: str
    mail: str
    mail_pass: str


@dataclass
class MailAccount(Account):
    """
    Account model for Mail product type.
    
    Attributes:
        mail (str): Email address
        password (str): Email password
    """
    mail: str
    password: str


@dataclass
class UbiConnectAccount(Account):
    """
    Account model for UbiConnect product type.
    
    Attributes:
        email (str): Email address
        password (str): Account password
        number (str): Phone number
        secret_code (str): Secret code for authentication
        recovery_codes (List[str]): List of recovery codes
    """
    email: str
    password: str
    number: str
    secret_code: str
    recovery_codes: List[str]


class Status(Enum):
    """
    Enum representing the possible status values for orders.
    """
    SUCCESS = "success"
    FAILED = "failed"
    PROCESSING = "processing"

    @classmethod
    def from_str(cls, status: str) -> 'Status':
        """
        Create a Status enum from a string value.
        
        Args:
            status (str): Status string from the API
            
        Returns:
            Status: Corresponding Status enum value
            
        Example:
            >>> status = Status.from_str("success")
            >>> print(status == Status.SUCCESS)  # True
        """
        status = status.lower()
        for member in cls:
            if member.value == status:
                return member
        return cls.FAILED  # Default to FAILED if unknown status


@dataclass
class OrderResponse:
    """
    Response model for order-related operations.
    
    Attributes:
        accounts (List[Account]): List of purchased accounts
        message (str): Response message
        success (bool): Whether the operation was successful
        cost (float): Order cost
        processing (bool): Whether the order is still processing
        order_id (int): Unique order identifier
        order_date (datetime): Date and time of the order
    """
    accounts: List[Account]
    message: str
    success: bool
    cost: float
    order_id: int
    order_date: datetime 
    processing: bool=False
    quantity: int=0
    refund_amount: float=0
    status: Status=Status.FAILED  # Default to FAILED
