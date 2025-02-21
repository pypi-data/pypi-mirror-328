# Copyright 2025 Zyber Pireci

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import bcrypt
import uuid
import jwt
import time
from datetime import datetime, timedelta

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = self.hash_password(password)
        self.api_key = None

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def verify_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password)

    def generate_api_key(self):
        self.api_key = str(uuid.uuid4())  # Generate a unique API key
        return self.api_key

class AuthManager:
    @staticmethod
    def authenticate(email, password, users_db):
        for user in users_db:
            if user.email == email and user.verify_password(password):
                return user
        return None
    
    @staticmethod
    def create_jwt_token(user):
        expiration = datetime.utcnow() + timedelta(hours=1)  # 1 hour expiry
        payload = {
            'user_id': user.email,
            'exp': expiration
        }
        return jwt.encode(payload, 'secret', algorithm='HS256')
