import boto3
from typing import Dict, Any, Optional, List
from datetime import datetime
import uuid
from ...config import Config
from ...models.user import User


class UserClient:
    """Client for managing users in DynamoDB."""
    
    def __init__(self, table_name: Optional[str] = None, region: str = 'us-east-1'):
        """
        Initialize DynamoDB client with table name.
        
        Args:
            table_name (str, optional): Name of the DynamoDB table. If not provided, will use from configuration.
            region (str): AWS region (default: us-east-1)
        """
        config = Config.get_instance()
        
        # Use provided table name or get from config
        self.table_name = table_name or config.user_table_name
        if not self.table_name:
            raise ValueError("No table name provided in either arguments or configuration")
            
        self.dynamodb = boto3.resource('dynamodb', region_name=region)
        self.table = self.dynamodb.Table(self.table_name)
        
    def create_user(self, user: User) -> User:
        """
        Create a new user.
        
        Args:
            user (User): User model instance to create
            
        Returns:
            User: Created user with updated fields (e.g. id, created timestamp)
        """
        # Generate ID and timestamp if not provided
        if not user.id:
            user.id = str(uuid.uuid4())
        if not user.created:
            user.created = datetime.utcnow()
            
        # Ensure customer_ids is a list
        if not user.customer_ids:
            user.customer_ids = []
            
        self.table.put_item(Item=user.to_dict())
        return user
    
    def get_user(self, user_id: str) -> Optional[User]:
        """
        Retrieve a user by ID.
        
        Args:
            user_id (str): User's unique identifier
            
        Returns:
            User: User if found, None otherwise
        """
        response = self.table.get_item(Key={'id': user_id})
        item = response.get('Item')
        return User.from_dict(item) if item else None
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """
        Retrieve a user by email.
        
        Args:
            email (str): User's email address
            
        Returns:
            User: User if found, None otherwise
        """
        response = self.table.scan(
            FilterExpression='email = :email',
            ExpressionAttributeValues={':email': email}
        )
        items = response.get('Items', [])
        return User.from_dict(items[0]) if items else None
        
    def get_users_by_customer(self, customer_id: str, limit: int = 100) -> List[User]:
        """
        Retrieve all users belonging to a specific customer.
        
        Args:
            customer_id (str): Customer's unique identifier
            limit (int): Maximum number of users to return
            
        Returns:
            list: List of users belonging to the customer
        """
        response = self.table.scan(
            FilterExpression='contains(customer_ids, :customer_id)',
            ExpressionAttributeValues={':customer_id': customer_id},
            Limit=limit
        )
        return [User.from_dict(item) for item in response.get('Items', [])]
    
    def update_user(self, user_id: str, updates: Dict[str, Any]) -> Optional[User]:
        """
        Update a user.
        
        Args:
            user_id (str): User's unique identifier
            updates (dict): Fields to update and their new values
            
        Returns:
            User: Updated user if successful, None if user not found
        """
        # Don't allow updating of id field
        if 'id' in updates:
            del updates['id']
            
        # Ensure customer_ids is a list if it's being updated
        if 'customer_ids' in updates and not isinstance(updates['customer_ids'], list):
            updates['customer_ids'] = [updates['customer_ids']] if updates['customer_ids'] else []
            
        update_expression = 'SET ' + ', '.join(f'#{k} = :{k}' for k in updates.keys())
        expression_attribute_names = {f'#{k}': k for k in updates.keys()}
        expression_attribute_values = {f':{k}': v for k, v in updates.items()}
        
        try:
            response = self.table.update_item(
                Key={'id': user_id},
                UpdateExpression=update_expression,
                ExpressionAttributeNames=expression_attribute_names,
                ExpressionAttributeValues=expression_attribute_values,
                ReturnValues='ALL_NEW'
            )
            attributes = response.get('Attributes')
            return User.from_dict(attributes) if attributes else None
        except self.dynamodb.meta.client.exceptions.ConditionalCheckFailedException:
            return None
    
    def delete_user(self, user_id: str) -> bool:
        """
        Delete a user.
        
        Args:
            user_id (str): User's unique identifier
            
        Returns:
            bool: True if deletion was successful, False otherwise
        """
        try:
            self.table.delete_item(Key={'id': user_id})
            return True
        except:
            return False
    
    def list_users(self, limit: int = 100) -> List[User]:
        """
        List all users.
        
        Args:
            limit (int): Maximum number of users to return
            
        Returns:
            list: List of User objects
        """
        response = self.table.scan(Limit=limit)
        return [User.from_dict(item) for item in response.get('Items', [])]
        
    def add_customer_to_user(self, user_id: str, customer_id: str) -> Optional[User]:
        """
        Add a customer ID to a user's list of customers.
        
        Args:
            user_id (str): User's unique identifier
            customer_id (str): Customer ID to add
            
        Returns:
            User: Updated user if successful, None if user not found
        """
        try:
            response = self.table.update_item(
                Key={'id': user_id},
                UpdateExpression='ADD customer_ids :customer_id',
                ExpressionAttributeValues={':customer_id': {customer_id}},
                ReturnValues='ALL_NEW'
            )
            attributes = response.get('Attributes')
            return User.from_dict(attributes) if attributes else None
        except self.dynamodb.meta.client.exceptions.ConditionalCheckFailedException:
            return None
            
    def remove_customer_from_user(self, user_id: str, customer_id: str) -> Optional[User]:
        """
        Remove a customer ID from a user's list of customers.
        
        Args:
            user_id (str): User's unique identifier
            customer_id (str): Customer ID to remove
            
        Returns:
            User: Updated user if successful, None if user not found
        """
        try:
            response = self.table.update_item(
                Key={'id': user_id},
                UpdateExpression='DELETE customer_ids :customer_id',
                ExpressionAttributeValues={':customer_id': {customer_id}},
                ReturnValues='ALL_NEW'
            )
            attributes = response.get('Attributes')
            return User.from_dict(attributes) if attributes else None
        except self.dynamodb.meta.client.exceptions.ConditionalCheckFailedException:
            return None 