from typing import Dict, Any, List
from datetime import datetime

class User:
    def __init__(
        self,
        name: str,
        customer_ids: List[str],
        id: str,
        email: str,
        created: datetime,
        email_validated: bool,
        **kwargs
    ):
        self.name = name
        self.customer_ids = customer_ids
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
            'customer_ids': self.customer_ids,
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
        required_fields = {'name', 'customer_ids', 'id', 'email', 'created', 'email_validated'}
        
        # Extract required fields
        required_data = {field: data[field] for field in required_fields}
        
        # Convert timestamp string to datetime if needed
        if isinstance(required_data['created'], str):
            required_data['created'] = datetime.fromisoformat(required_data['created'].replace('Z', '+00:00'))
        
        # Handle legacy data where customer_id might be a string
        if 'customer_id' in data and 'customer_ids' not in data:
            required_data['customer_ids'] = [data['customer_id']] if data['customer_id'] else []
        
        # Ensure customer_ids is always a list
        if not isinstance(required_data['customer_ids'], list):
            required_data['customer_ids'] = [required_data['customer_ids']] if required_data['customer_ids'] else []
        
        # Extract additional fields
        additional_data = {k: v for k, v in data.items() if k not in required_fields and k != 'customer_id'}
        
        # Create instance with both required and additional fields
        return cls(**required_data, **additional_data) 