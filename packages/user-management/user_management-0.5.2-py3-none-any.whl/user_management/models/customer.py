from typing import List, Dict, Any

class Customer:
    def __init__(
        self,
        name: str,
        subscription_id: str,
        users: List[str],
        is_org: bool,
        **kwargs
    ):
        self.name = name
        self.subscription_id = subscription_id
        self.users = users
        self.is_org = is_org
        
        # Allow for dynamic field addition
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the customer object to a dictionary."""
        base_dict = {
            'name': self.name,
            'subscription_id': self.subscription_id,
            'users': self.users,
            'is_org': self.is_org
        }
        
        # Add any additional fields that were dynamically added
        for key, value in self.__dict__.items():
            if key not in base_dict:
                base_dict[key] = value
                
        return base_dict
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Customer':
        """Create a Customer instance from a dictionary."""
        required_fields = {'name', 'subscription_id', 'users', 'is_org'}
        
        # Extract required fields
        required_data = {field: data[field] for field in required_fields}
        
        # Extract additional fields
        additional_data = {k: v for k, v in data.items() if k not in required_fields}
        
        # Create instance with both required and additional fields
        return cls(**required_data, **additional_data) 