from typing import Dict, Any, Literal
from datetime import datetime

class Product:
    def __init__(
        self,
        id: str,
        stripe_id: str,
        name: str,
        frequency: Literal["monthly", "annually", "6_months", "3_months", "single_charge"],
        **kwargs
    ):
        self.id = id
        self.stripe_id = stripe_id
        self.name = name
        self.frequency = frequency
        
        # Allow for dynamic field addition
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the product object to a dictionary."""
        base_dict = {
            'id': self.id,
            'stripe_id': self.stripe_id,
            'name': self.name,
            'frequency': self.frequency
        }
        
        # Add any additional fields that were dynamically added
        for key, value in self.__dict__.items():
            if key not in base_dict:
                base_dict[key] = value
                
        return base_dict
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Product':
        """Create a Product instance from a dictionary."""
        required_fields = {'id', 'stripe_id', 'name', 'frequency'}
        
        # Extract required fields
        required_data = {field: data[field] for field in required_fields}
        
        # Extract additional fields
        additional_data = {k: v for k, v in data.items() if k not in required_fields}
        
        # Create instance with both required and additional fields
        return cls(**required_data, **additional_data) 