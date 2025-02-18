from typing import Dict, Any
from datetime import datetime

class User:
    def __init__(
        self,
        name: str,
        customer_id: str,
        id: str,
        email: str,
        created: datetime,
        email_validated: bool,
        **kwargs
    ):
        self.name = name
        self.customer_id = customer_id
        self.id = id
        self.email = email
        self.created = created
        self.email_validated = email_validated
        
        # Allow for dynamic field addition
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the user object to a dictionary."""
        base_dict = {
            'name': self.name,
            'customer_id': self.customer_id,
            'id': self.id,
            'email': self.email,
            'created': self.created,
            'email_validated': self.email_validated
        }
        
        # Add any additional fields that were dynamically added
        for key, value in self.__dict__.items():
            if key not in base_dict:
                base_dict[key] = value
                
        return base_dict
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'User':
        """Create a User instance from a dictionary."""
        required_fields = {'name', 'customer_id', 'id', 'email', 'created', 'email_validated'}
        
        # Extract required fields
        required_data = {field: data[field] for field in required_fields}
        
        # Convert timestamp string to datetime if needed
        if isinstance(required_data['created'], str):
            required_data['created'] = datetime.fromisoformat(required_data['created'].replace('Z', '+00:00'))
        
        # Extract additional fields
        additional_data = {k: v for k, v in data.items() if k not in required_fields}
        
        # Create instance with both required and additional fields
        return cls(**required_data, **additional_data) 