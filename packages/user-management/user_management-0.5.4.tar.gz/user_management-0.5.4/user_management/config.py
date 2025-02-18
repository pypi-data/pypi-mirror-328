from typing import Dict, Any, Optional
from dataclasses import dataclass, field


@dataclass
class Config:
    """Global configuration for user_management package."""
    
    # Database table names
    user_table_name: str = "users"
    customer_table_name: str = "customers"
    subscription_table_name: str = "subscriptions"
    
    # Firebase configurations
    firebase_credentials_path: Optional[str] = None
    firebase_credentials_dict: Optional[Dict[str, Any]] = None
    firebase_app_name: Optional[str] = None
    
    # Stripe configurations
    stripe_api_key: Optional[str] = None
    stripe_api_version: str = "2023-10-16"
    stripe_webhook_secret: Optional[str] = None
    
    # Custom configurations
    custom_settings: Dict[str, Any] = field(default_factory=dict)
    
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @classmethod
    def get_instance(cls) -> 'Config':
        """Get the global configuration instance."""
        if cls._instance is None:
            cls._instance = Config()
        return cls._instance
    
    def update(self, **kwargs):
        """Update configuration values."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                self.custom_settings[key] = value
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value."""
        if hasattr(self, key):
            return getattr(self, key)
        return self.custom_settings.get(key, default) 