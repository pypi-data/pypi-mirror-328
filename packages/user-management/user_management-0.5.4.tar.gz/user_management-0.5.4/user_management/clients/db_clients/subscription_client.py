import boto3
from typing import Dict, Any, Optional, List
from datetime import datetime
import uuid
from ...models.subscription import Subscription
from ...config import Config


class SubscriptionClient:
    """Client for managing subscriptions in DynamoDB."""
    
    def __init__(self, table_name: Optional[str] = None, region: str = 'us-east-1'):
        """
        Initialize DynamoDB client with table name.
        
        Args:
            table_name (str, optional): Name of the DynamoDB table. If not provided, will use from configuration.
            region (str): AWS region (default: us-east-1)
        """
        config = Config.get_instance()
        
        # Use provided table name or get from config
        self.table_name = table_name or config.subscription_table_name
        if not self.table_name:
            raise ValueError("No table name provided in either arguments or configuration")
            
        self.dynamodb = boto3.resource('dynamodb', region_name=region)
        self.table = self.dynamodb.Table(self.table_name)
    
    def create_subscription(self, product_id: str, customer_id: str, 
                          status: str = 'active', 
                          additional_fields: Optional[Dict[str, Any]] = None) -> Subscription:
        """
        Create a new subscription.
        
        Args:
            product_id (str): ID of the product being subscribed to
            customer_id (str): ID of the customer who owns the subscription
            status (str): Status of the subscription (default: 'active')
            additional_fields (dict): Optional additional fields to store
            
        Returns:
            Subscription: Created subscription
        """
        timestamp = datetime.utcnow()
        subscription_id = str(uuid.uuid4())
        
        subscription_data = {
            'id': subscription_id,
            'product_id': product_id,
            'customer_id': customer_id,
            'status': status,
            'created': timestamp
        }
        
        if additional_fields:
            # Don't allow overwriting of core fields
            core_fields = {'id', 'product_id', 'customer_id', 'status', 'created'}
            safe_additional_fields = {k: v for k, v in additional_fields.items() 
                                   if k not in core_fields}
            subscription_data.update(safe_additional_fields)
            
        subscription = Subscription.from_dict(subscription_data)
        self.table.put_item(Item=subscription.to_dict())
        return subscription
    
    def get_subscription(self, subscription_id: str) -> Optional[Subscription]:
        """
        Retrieve a subscription by ID.
        
        Args:
            subscription_id (str): Subscription's unique identifier
            
        Returns:
            Subscription: Subscription if found, None otherwise
        """
        response = self.table.get_item(Key={'id': subscription_id})
        item = response.get('Item')
        return Subscription.from_dict(item) if item else None
    
    def get_subscriptions_by_customer(self, customer_id: str, limit: int = 100) -> List[Subscription]:
        """
        Retrieve all subscriptions belonging to a specific customer.
        
        Args:
            customer_id (str): Customer's unique identifier
            limit (int): Maximum number of subscriptions to return
            
        Returns:
            list: List of subscriptions belonging to the customer
        """
        response = self.table.scan(
            FilterExpression='customer_id = :customer_id',
            ExpressionAttributeValues={':customer_id': customer_id},
            Limit=limit
        )
        return [Subscription.from_dict(item) for item in response.get('Items', [])]
    
    def get_subscriptions_by_product(self, product_id: str, limit: int = 100) -> List[Subscription]:
        """
        Retrieve subscriptions by product ID.
        
        Args:
            product_id (str): Product's unique identifier
            limit (int): Maximum number of subscriptions to return
            
        Returns:
            List[Subscription]: List of subscription models
        """
        response = self.table.scan(
            FilterExpression='product_id = :product_id',
            ExpressionAttributeValues={':product_id': product_id},
            Limit=limit
        )
        return [Subscription.from_dict(item) for item in response.get('Items', [])]
    
    def update_subscription(self, subscription_id: str, updates: Dict[str, Any]) -> Optional[Subscription]:
        """
        Update a subscription.
        
        Args:
            subscription_id (str): Subscription's unique identifier
            updates (dict): Fields to update and their new values
            
        Returns:
            Subscription: Updated subscription if successful, None if subscription not found
        """
        # Don't allow updating of id field
        if 'id' in updates:
            del updates['id']
            
        update_expression = 'SET ' + ', '.join(f'#{k} = :{k}' for k in updates.keys())
        expression_attribute_names = {f'#{k}': k for k in updates.keys()}
        expression_attribute_values = {f':{k}': v for k, v in updates.items()}
        
        try:
            response = self.table.update_item(
                Key={'id': subscription_id},
                UpdateExpression=update_expression,
                ExpressionAttributeNames=expression_attribute_names,
                ExpressionAttributeValues=expression_attribute_values,
                ReturnValues='ALL_NEW'
            )
            attributes = response.get('Attributes')
            return Subscription.from_dict(attributes) if attributes else None
        except self.dynamodb.meta.client.exceptions.ConditionalCheckFailedException:
            return None
    
    def delete_subscription(self, subscription_id: str) -> bool:
        """
        Delete a subscription.
        
        Args:
            subscription_id (str): Subscription's unique identifier
            
        Returns:
            bool: True if deletion was successful, False otherwise
        """
        try:
            self.table.delete_item(Key={'id': subscription_id})
            return True
        except:
            return False
    
    def list_subscriptions(self, limit: int = 100) -> List[Subscription]:
        """
        List all subscriptions.
        
        Args:
            limit (int): Maximum number of subscriptions to return
            
        Returns:
            list: List of Subscription objects
        """
        response = self.table.scan(Limit=limit)
        return [Subscription.from_dict(item) for item in response.get('Items', [])] 