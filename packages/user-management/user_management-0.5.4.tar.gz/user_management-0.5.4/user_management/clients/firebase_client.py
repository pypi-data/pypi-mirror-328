from typing import Optional, Dict, Any, Union
import json
import firebase_admin
from firebase_admin import auth, credentials
from pydantic import BaseModel
from datetime import datetime
from ..config import Config

class FirebaseUser(BaseModel):
    """Firebase user data model"""
    uid: str
    email: Optional[str] = None
    display_name: Optional[str] = None
    phone_number: Optional[str] = None
    disabled: bool = False
    custom_claims: Optional[Dict[str, Any]] = None
    created_at: datetime
    last_sign_in: Optional[datetime] = None

class FirebaseClient:
    """Firebase client for user management operations"""
    
    def __init__(self, credentials_info: Optional[Union[str, Dict[str, Any]]] = None):
        """Initialize Firebase client with service account credentials
        
        Args:
            credentials_info: Optional. Can be one of:
                - Path to Firebase service account credentials JSON file (str)
                - Dictionary containing the credentials (Dict[str, Any])
                If not provided, will use credentials from configuration
                            
        Example:
            # Using configuration (recommended)
            client = FirebaseClient()
            
            # Using path to JSON file
            client = FirebaseClient("path/to/firebase-credentials.json")
            
            # Using credentials dictionary
            client = FirebaseClient({
                "type": "service_account",
                "project_id": "your-project-id",
                "private_key_id": "key-id",
                "private_key": "-----BEGIN PRIVATE KEY-----\n...",
                "client_email": "firebase-adminsdk...iam.gserviceaccount.com",
                "client_id": "...",
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                "client_x509_cert_url": "https://www.googleapis.com/..."
            })
        """
        config = Config.get_instance()
        
        # If no credentials provided, try to get from config
        if credentials_info is None:
            if config.firebase_credentials_path:
                credentials_info = config.firebase_credentials_path
            elif config.firebase_credentials_dict:
                credentials_info = config.firebase_credentials_dict
            else:
                raise ValueError("No Firebase credentials provided in either arguments or configuration")
        
        if isinstance(credentials_info, str):
            cred = credentials.Certificate(credentials_info)
        elif isinstance(credentials_info, dict):
            # Create a temporary JSON file with the credentials
            import tempfile
            import os
            
            with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as temp_file:
                json.dump(credentials_info, temp_file)
                temp_path = temp_file.name
            
            try:
                cred = credentials.Certificate(temp_path)
            finally:
                # Clean up the temporary file
                try:
                    os.unlink(temp_path)
                except OSError:
                    pass
        else:
            raise ValueError("credentials_info must be a path to a JSON file or a dictionary")
            
        # Use app name from config if provided
        app_name = config.firebase_app_name if config.firebase_app_name else None
        self.app = firebase_admin.initialize_app(cred, name=app_name)
    
    def create_user(self, email: str, password: str, display_name: Optional[str] = None) -> FirebaseUser:
        """Create a new user in Firebase
        
        Args:
            email: User's email address
            password: User's password
            display_name: Optional display name for the user
            
        Returns:
            FirebaseUser object containing the created user's information
            
        Raises:
            firebase_admin.auth.AuthError: If user creation fails
        """
        user = auth.create_user(
            email=email,
            password=password,
            display_name=display_name
        )
        return self._convert_to_user_data(user)
    
    def get_user(self, uid: str) -> FirebaseUser:
        """Get user information by UID
        
        Args:
            uid: User's unique identifier
            
        Returns:
            FirebaseUser object containing the user's information
            
        Raises:
            firebase_admin.auth.AuthError: If user retrieval fails
        """
        user = auth.get_user(uid)
        return self._convert_to_user_data(user)
    
    def update_user(self, uid: str, **kwargs) -> FirebaseUser:
        """Update user information
        
        Args:
            uid: User's unique identifier
            **kwargs: User properties to update (email, password, display_name, etc.)
            
        Returns:
            FirebaseUser object containing the updated user information
            
        Raises:
            firebase_admin.auth.AuthError: If user update fails
        """
        user = auth.update_user(uid, **kwargs)
        return self._convert_to_user_data(user)
    
    def delete_user(self, uid: str) -> None:
        """Delete a user
        
        Args:
            uid: User's unique identifier
            
        Raises:
            firebase_admin.auth.AuthError: If user deletion fails
        """
        auth.delete_user(uid)
    
    def verify_token(self, id_token: str, user_id: Optional[str] = None) -> Dict[str, Any]:
        """Verify a Firebase ID token
        
        Args:
            id_token: The Firebase ID token to verify
            user_id: Optional user ID to verify against the token's UID
            
        Returns:
            Dictionary containing the decoded token claims
            
        Raises:
            firebase_admin.auth.AuthError: If token verification fails
            ValueError: If the token's UID doesn't match the provided user_id
        """
        decoded_token = auth.verify_id_token(id_token)
        
        if user_id is not None and decoded_token['uid'] != user_id:
            raise ValueError(f"Token UID does not match provided user_id. Token UID: {decoded_token['uid']}, Provided user_id: {user_id}")
            
        return decoded_token
    
    def set_custom_claims(self, uid: str, custom_claims: Dict[str, Any]) -> None:
        """Set custom claims for a user
        
        Args:
            uid: User's unique identifier
            custom_claims: Dictionary of custom claims to set
            
        Raises:
            firebase_admin.auth.AuthError: If setting custom claims fails
        """
        auth.set_custom_user_claims(uid, custom_claims)
    
    def _convert_to_user_data(self, firebase_user: auth.UserRecord) -> FirebaseUser:
        """Convert Firebase UserRecord to FirebaseUser model
        
        Args:
            firebase_user: Firebase UserRecord object
            
        Returns:
            FirebaseUser object
        """
        return FirebaseUser(
            uid=firebase_user.uid,
            email=firebase_user.email,
            display_name=firebase_user.display_name,
            phone_number=firebase_user.phone_number,
            disabled=firebase_user.disabled,
            custom_claims=firebase_user.custom_claims,
            created_at=datetime.fromtimestamp(firebase_user.user_metadata.creation_timestamp / 1000),
            last_sign_in=datetime.fromtimestamp(firebase_user.user_metadata.last_sign_in_timestamp / 1000)
            if firebase_user.user_metadata.last_sign_in_timestamp
            else None
        ) 