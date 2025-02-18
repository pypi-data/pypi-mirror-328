import stripe
from typing import Dict, Any, Optional
from ..config import Config


class StripeClient:
    """Client for managing Stripe customers."""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize Stripe client with API key.
        
        Args:
            api_key (str, optional): Stripe API key. If not provided, will use from configuration.
        """
        config = Config.get_instance()
        
        # Use provided API key or get from config
        self.api_key = api_key or config.stripe_api_key
        if not self.api_key:
            raise ValueError("No Stripe API key provided in either arguments or configuration")
            
        stripe.api_key = self.api_key
        
        # Set API version from config
        if config.stripe_api_version:
            stripe.api_version = config.stripe_api_version
        
    def create_customer(self, email: str, name: str, 
                       metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Create a new Stripe customer.
        
        Args:
            email (str): Customer's email address
            name (str): Customer's name
            metadata (dict): Optional metadata to attach to the customer
            
        Returns:
            dict: Created Stripe customer object
        """
        customer_data = {
            'email': email,
            'name': name
        }
        
        if metadata:
            customer_data['metadata'] = metadata
            
        try:
            customer = stripe.Customer.create(**customer_data)
            return customer
        except stripe.error.StripeError as e:
            raise Exception(f"Failed to create Stripe customer: {str(e)}")
    
    def get_customer(self, customer_id: str) -> Dict[str, Any]:
        """
        Retrieve a Stripe customer by ID.
        
        Args:
            customer_id (str): Stripe customer ID
            
        Returns:
            dict: Stripe customer object
            
        Raises:
            Exception: If customer retrieval fails
        """
        try:
            customer = stripe.Customer.retrieve(customer_id)
            return customer
        except stripe.error.StripeError as e:
            raise Exception(f"Failed to retrieve Stripe customer: {str(e)}")
    
    def update_customer(self, customer_id: str, 
                       updates: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a Stripe customer.
        
        Args:
            customer_id (str): Stripe customer ID
            updates (dict): Fields to update and their new values
            
        Returns:
            dict: Updated Stripe customer object
            
        Raises:
            Exception: If customer update fails
        """
        try:
            customer = stripe.Customer.modify(customer_id, **updates)
            return customer
        except stripe.error.StripeError as e:
            raise Exception(f"Failed to update Stripe customer: {str(e)}")
    
    def delete_customer(self, customer_id: str) -> bool:
        """
        Delete a Stripe customer.
        
        Args:
            customer_id (str): Stripe customer ID
            
        Returns:
            bool: True if deletion was successful
            
        Raises:
            Exception: If customer deletion fails
        """
        try:
            deleted = stripe.Customer.delete(customer_id)
            return deleted['deleted']
        except stripe.error.StripeError as e:
            raise Exception(f"Failed to delete Stripe customer: {str(e)}")

    def list_products(self, active: Optional[bool] = None, 
                     limit: Optional[int] = None) -> Dict[str, Any]:
        """
        Retrieve a list of products from Stripe.
        
        Args:
            active (bool, optional): If true, only return active products
            limit (int, optional): Maximum number of products to return
            
        Returns:
            dict: Object containing a list of Stripe products and metadata
            
        Raises:
            Exception: If product retrieval fails
        """
        try:
            params = {}
            if active is not None:
                params['active'] = active
            if limit is not None:
                params['limit'] = limit
                
            products = stripe.Product.list(**params)
            return products
        except stripe.error.StripeError as e:
            raise Exception(f"Failed to retrieve Stripe products: {str(e)}") 