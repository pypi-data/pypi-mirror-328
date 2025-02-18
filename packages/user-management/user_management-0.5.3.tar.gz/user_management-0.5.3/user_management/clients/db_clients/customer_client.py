import boto3
from typing import Dict, Any, Optional, List
from datetime import datetime
import uuid
from ...models.customer import Customer
from ...config import Config


class CustomerClient:
    """Client for managing customers in DynamoDB."""
    
    def __init__(self, table_name: Optional[str] = None, region: str = 'us-east-1'):
        """
        Initialize DynamoDB client with table name.
        
        Args:
            table_name (str, optional): Name of the DynamoDB table. If not provided, will use from configuration.
            region (str): AWS region (default: us-east-1)
        """
        config = Config.get_instance()
        
        # Use provided table name or get from config
        self.table_name = table_name or config.customer_table_name
        if not self.table_name:
            raise ValueError("No table name provided in either arguments or configuration")
            
        self.dynamodb = boto3.resource('dynamodb', region_name=region)
        self.table = self.dynamodb.Table(self.table_name)
    
    def _to_dynamo_item(self, customer: Customer) -> Dict[str, Any]:
        """Convert Customer model to DynamoDB item format."""
        customer_dict = customer.to_dict()
        timestamp = datetime.utcnow().isoformat()
        
        dynamo_item = {
            'id': str(uuid.uuid4()),
            'name': customer_dict['name'],
            'subscription_info': {
                'stripe_id': customer_dict['subscription_id']
            } if customer_dict['subscription_id'] is not None else None,
            'users': customer_dict['users'],
            'is_org': customer_dict['is_org'],
            'owner': customer_dict['owner'],
            'created': timestamp
        }
        
        # Add any additional fields
        for key, value in customer_dict.items():
            if key not in {'name', 'subscription_id', 'users', 'is_org', 'owner'}:
                dynamo_item[key] = value
                
        return dynamo_item
    
    def _from_dynamo_item(self, item: Dict[str, Any]) -> Customer:
        """Convert DynamoDB item to Customer model."""
        if not item:
            return None
            
        customer_data = {
            'name': item['name'],
            'subscription_id': item['subscription_info']['stripe_id'] if item.get('subscription_info') else None,
            'users': item.get('users', []),
            'is_org': item.get('is_org', False),
            'owner': item.get('owner')
        }
        
        # Add any additional fields from DynamoDB
        for key, value in item.items():
            if key not in {'id', 'name', 'subscription_info', 'created', 'users', 'is_org', 'owner'}:
                customer_data[key] = value
                
        return Customer.from_dict(customer_data)
        
    def create_customer(self, customer: Customer) -> Customer:
        """
        Create a new customer.
        
        Args:
            customer (Customer): Customer model instance
            
        Returns:
            Customer: Created customer model with updated fields
        """
        customer_item = self._to_dynamo_item(customer)
        self.table.put_item(Item=customer_item)
        return self._from_dynamo_item(customer_item)
    
    def get_customer(self, customer_id: str) -> Optional[Customer]:
        """
        Retrieve a customer by ID.
        
        Args:
            customer_id (str): Customer's unique identifier
            
        Returns:
            Customer: Customer model if found, None otherwise
        """
        response = self.table.get_item(Key={'id': customer_id})
        return self._from_dynamo_item(response.get('Item'))
    
    def get_customer_by_name(self, name: str) -> Optional[Customer]:
        """
        Retrieve a customer by name.
        
        Args:
            name (str): Customer name
            
        Returns:
            Customer: Customer model if found, None otherwise
        """
        response = self.table.scan(
            FilterExpression='#name = :name',
            ExpressionAttributeNames={'#name': 'name'},
            ExpressionAttributeValues={':name': name}
        )
        items = response.get('Items', [])
        return self._from_dynamo_item(items[0]) if items else None
    
    def get_by_owner(self, owner_id: str) -> List[Customer]:
        """
        Retrieve all customers owned by a specific user.
        
        Args:
            owner_id (str): The ID of the owner/user
            
        Returns:
            List[Customer]: List of customer models owned by the specified user
        """
        response = self.table.scan(
            FilterExpression='#owner = :owner',
            ExpressionAttributeNames={'#owner': 'owner'},
            ExpressionAttributeValues={':owner': owner_id}
        )
        items = response.get('Items', [])
        return [self._from_dynamo_item(item) for item in items]
    
    def update_customer(self, customer_id: str, customer: Customer) -> Optional[Customer]:
        """
        Update a customer profile.
        
        Args:
            customer_id (str): Customer's unique identifier
            customer (Customer): Updated customer model
            
        Returns:
            Customer: Updated customer model if successful, None if customer not found
        """
        customer_dict = customer.to_dict()
        
        # Prepare update expression
        update_parts = []
        expression_attribute_names = {}
        expression_attribute_values = {}
        
        # Handle core fields
        if 'name' in customer_dict:
            update_parts.append('#name = :name')
            expression_attribute_names['#name'] = 'name'
            expression_attribute_values[':name'] = customer_dict['name']
            
        if 'subscription_id' in customer_dict:
            update_parts.append('#subscription_info.#stripe_id = :stripe_id')
            expression_attribute_names['#subscription_info'] = 'subscription_info'
            expression_attribute_names['#stripe_id'] = 'stripe_id'
            expression_attribute_values[':stripe_id'] = customer_dict['subscription_id']
            
        if 'users' in customer_dict:
            update_parts.append('#users = :users')
            expression_attribute_names['#users'] = 'users'
            expression_attribute_values[':users'] = customer_dict['users']
            
        if 'is_org' in customer_dict:
            update_parts.append('#is_org = :is_org')
            expression_attribute_names['#is_org'] = 'is_org'
            expression_attribute_values[':is_org'] = customer_dict['is_org']

        if 'owner' in customer_dict:
            update_parts.append('#owner = :owner')
            expression_attribute_names['#owner'] = 'owner'
            expression_attribute_values[':owner'] = customer_dict['owner']
        
        # Handle additional fields
        for key, value in customer_dict.items():
            if key not in {'name', 'subscription_id', 'users', 'is_org', 'owner'}:
                update_parts.append(f'#{key} = :{key}')
                expression_attribute_names[f'#{key}'] = key
                expression_attribute_values[f':{key}'] = value
        
        if not update_parts:
            return self.get_customer(customer_id)
            
        update_expression = 'SET ' + ', '.join(update_parts)
        
        try:
            response = self.table.update_item(
                Key={'id': customer_id},
                UpdateExpression=update_expression,
                ExpressionAttributeNames=expression_attribute_names,
                ExpressionAttributeValues=expression_attribute_values,
                ReturnValues='ALL_NEW'
            )
            return self._from_dynamo_item(response.get('Attributes'))
        except self.dynamodb.meta.client.exceptions.ConditionalCheckFailedException:
            return None
    
    def delete_customer(self, customer_id: str) -> bool:
        """
        Delete a customer.
        
        Args:
            customer_id (str): Customer's unique identifier
            
        Returns:
            bool: True if deletion was successful, False otherwise
        """
        try:
            self.table.delete_item(Key={'id': customer_id})
            return True
        except:
            return False
    
    def list_customers(self, limit: int = 100) -> List[Customer]:
        """
        List all customers.
        
        Args:
            limit (int): Maximum number of customers to return
            
        Returns:
            list: List of customer models
        """
        response = self.table.scan(Limit=limit)
        return [self._from_dynamo_item(item) for item in response.get('Items', [])] 