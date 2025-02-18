import boto3
from typing import Dict, Any, Optional, List
from datetime import datetime
import uuid
from ...models.product import Product
from ...config import Config


class ProductClient:
    """Client for managing products in DynamoDB."""
    
    def __init__(self, table_name: Optional[str] = None, region: str = 'us-east-1'):
        """
        Initialize DynamoDB client with table name.
        
        Args:
            table_name (str, optional): Name of the DynamoDB table. If not provided, will use from configuration.
            region (str): AWS region (default: us-east-1)
        """
        config = Config.get_instance()
        
        # Use provided table name or get from config
        self.table_name = table_name or config.product_table_name
        if not self.table_name:
            raise ValueError("No table name provided in either arguments or configuration")
            
        self.dynamodb = boto3.resource('dynamodb', region_name=region)
        self.table = self.dynamodb.Table(self.table_name)
    
    def _to_dynamo_item(self, product: Product) -> Dict[str, Any]:
        """Convert Product model to DynamoDB item format."""
        product_dict = product.to_dict()
        timestamp = datetime.utcnow().isoformat()
        
        dynamo_item = {
            'id': product_dict.get('id', str(uuid.uuid4())),
            'stripe_id': product_dict['stripe_id'],
            'name': product_dict['name'],
            'frequency': product_dict['frequency'],
            'created': timestamp
        }
        
        # Add any additional fields
        for key, value in product_dict.items():
            if key not in {'id', 'stripe_id', 'name', 'frequency'}:
                dynamo_item[key] = value
                
        return dynamo_item
    
    def _from_dynamo_item(self, item: Dict[str, Any]) -> Optional[Product]:
        """Convert DynamoDB item to Product model."""
        if not item:
            return None
            
        product_data = {
            'id': item['id'],
            'stripe_id': item['stripe_id'],
            'name': item['name'],
            'frequency': item['frequency']
        }
        
        # Add any additional fields from DynamoDB
        for key, value in item.items():
            if key not in {'id', 'stripe_id', 'name', 'frequency', 'created'}:
                product_data[key] = value
                
        return Product.from_dict(product_data)
        
    def create_product(self, product: Product) -> Product:
        """
        Create a new product.
        
        Args:
            product (Product): Product model instance
            
        Returns:
            Product: Created product model with updated fields
        """
        product_item = self._to_dynamo_item(product)
        self.table.put_item(Item=product_item)
        return self._from_dynamo_item(product_item)
    
    def get_product(self, product_id: str) -> Optional[Product]:
        """
        Retrieve a product by ID.
        
        Args:
            product_id (str): Product's unique identifier
            
        Returns:
            Product: Product model if found, None otherwise
        """
        response = self.table.get_item(Key={'id': product_id})
        return self._from_dynamo_item(response.get('Item'))
    
    def get_product_by_stripe_id(self, stripe_id: str) -> Optional[Product]:
        """
        Retrieve a product by Stripe ID.
        
        Args:
            stripe_id (str): Product's Stripe identifier
            
        Returns:
            Product: Product model if found, None otherwise
        """
        response = self.table.scan(
            FilterExpression='stripe_id = :stripe_id',
            ExpressionAttributeValues={':stripe_id': stripe_id}
        )
        items = response.get('Items', [])
        return self._from_dynamo_item(items[0]) if items else None
    
    def update_product(self, product_id: str, product: Product) -> Optional[Product]:
        """
        Update a product.
        
        Args:
            product_id (str): Product's unique identifier
            product (Product): Updated product model
            
        Returns:
            Product: Updated product model if successful, None if product not found
        """
        product_dict = product.to_dict()
        
        # Prepare update expression
        update_parts = []
        expression_attribute_names = {}
        expression_attribute_values = {}
        
        # Handle core fields
        if 'stripe_id' in product_dict:
            update_parts.append('#stripe_id = :stripe_id')
            expression_attribute_names['#stripe_id'] = 'stripe_id'
            expression_attribute_values[':stripe_id'] = product_dict['stripe_id']
            
        if 'name' in product_dict:
            update_parts.append('#name = :name')
            expression_attribute_names['#name'] = 'name'
            expression_attribute_values[':name'] = product_dict['name']
            
        if 'frequency' in product_dict:
            update_parts.append('#frequency = :frequency')
            expression_attribute_names['#frequency'] = 'frequency'
            expression_attribute_values[':frequency'] = product_dict['frequency']
        
        # Handle additional fields
        for key, value in product_dict.items():
            if key not in {'id', 'stripe_id', 'name', 'frequency'}:
                update_parts.append(f'#{key} = :{key}')
                expression_attribute_names[f'#{key}'] = key
                expression_attribute_values[f':{key}'] = value
        
        if not update_parts:
            return self.get_product(product_id)
            
        update_expression = 'SET ' + ', '.join(update_parts)
        
        try:
            response = self.table.update_item(
                Key={'id': product_id},
                UpdateExpression=update_expression,
                ExpressionAttributeNames=expression_attribute_names,
                ExpressionAttributeValues=expression_attribute_values,
                ReturnValues='ALL_NEW'
            )
            return self._from_dynamo_item(response.get('Attributes'))
        except self.dynamodb.meta.client.exceptions.ConditionalCheckFailedException:
            return None
    
    def delete_product(self, product_id: str) -> bool:
        """
        Delete a product.
        
        Args:
            product_id (str): Product's unique identifier
            
        Returns:
            bool: True if deletion was successful, False otherwise
        """
        try:
            self.table.delete_item(Key={'id': product_id})
            return True
        except:
            return False
    
    def list_products(self, limit: int = 100) -> List[Product]:
        """
        List all products.
        
        Args:
            limit (int): Maximum number of products to return
            
        Returns:
            list: List of product models
        """
        response = self.table.scan(Limit=limit)
        return [self._from_dynamo_item(item) for item in response.get('Items', [])] 