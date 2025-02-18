"""
User Management Package

A package for managing user-related operations using Firebase.
"""

from .clients.firebase_client import FirebaseClient, FirebaseUser
from .clients.db_clients.customer_client import CustomerClient
from .clients.db_clients.user_client import UserClient
from .clients.db_clients.subscription_client import SubscriptionClient
from .clients.stripe_client import StripeClient
from .clients.db_clients.product_client import ProductClient
from .models.product import Product
from .models.user import User
from .models.customer import Customer
from .models.subscription import Subscription
from .config import Config

__version__ = "0.5.1"

# Create a default configuration instance
config = Config.get_instance()

# Expose configuration update function at package level
def configure(**kwargs):
    """Update global configuration for user_management package.
    
    Example:
        >>> import user_management
        >>> user_management.configure(
        ...     user_table_name='custom_users',
        ...     customer_table_name='custom_customers'
        ... )
    """
    config.update(**kwargs)

__all__ = [
    "FirebaseClient",
    "FirebaseUser",
    "CustomerClient",
    "UserClient",
    "SubscriptionClient",
    "StripeClient",
    "ProductClient",
    "Product",
    "User",
    "Customer",
    "Subscription",
    "config",
    "configure"
] 