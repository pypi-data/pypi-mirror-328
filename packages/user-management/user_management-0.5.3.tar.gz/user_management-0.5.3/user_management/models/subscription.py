from typing import Dict, Any
from datetime import datetime

class Subscription:
    def __init__(
        self,
        id: str,
        stripe_id: str,
        product_id: str,
        **kwargs
    ):
        self.id = id
        self.stripe_id = stripe_id
        self.product_id = product_id
        
        # Allow for dynamic field addition
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the subscription object to a dictionary."""
        base_dict = {
            'id': self.id,
            'stripe_id': self.stripe_id,
            'product_id': self.product_id,
        }
        
        # Add any additional fields that were dynamically added
        for key, value in self.__dict__.items():
            if key not in base_dict:
                base_dict[key] = value
                
        return base_dict
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Subscription':
        """Create a Subscription instance from a dictionary."""
        required_fields = {'id', 'stripe_id', 'product_id'}
        
        # Extract required fields
        required_data = {field: data[field] for field in required_fields}
        
        # Extract additional fields
        additional_data = {k: v for k, v in data.items() if k not in required_fields}
        
        # Create instance with both required and additional fields
        return cls(**required_data, **additional_data) 