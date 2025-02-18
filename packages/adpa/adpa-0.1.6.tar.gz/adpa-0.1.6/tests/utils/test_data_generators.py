"""Specialized test data generators for ADPA Framework."""
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Union
import random
import uuid

from faker import Faker

class BaseGenerator:
    """Base class for all test data generators."""
    
    def __init__(self):
        self.faker = Faker()

    def _generate_timestamp(self, start_date: Optional[datetime] = None) -> datetime:
        """Generate a timestamp within the last 30 days."""
        if not start_date:
            start_date = datetime.now()
        days = random.randint(0, 30)
        return start_date - timedelta(days=days)

class LLMGenerator(BaseGenerator):
    """Generator for LLM-related test data."""
    
    PROMPT_TEMPLATES = {
        'question': "What is {topic}?",
        'summary': "Summarize the following text: {text}",
        'analysis': "Analyze the following {aspect}: {content}",
        'translation': "Translate the following to {language}: {text}",
        'code': "Write a {language} function that {task}"
    }
    
    def generate_prompt(self, template_type: str = None) -> Dict[str, Any]:
        """Generate an LLM prompt with metadata."""
        if not template_type:
            template_type = random.choice(list(self.PROMPT_TEMPLATES.keys()))
            
        template = self.PROMPT_TEMPLATES[template_type]
        
        if template_type == 'question':
            prompt = template.format(topic=self.faker.catch_phrase())
        elif template_type == 'summary':
            prompt = template.format(text=self.faker.text(max_nb_chars=500))
        elif template_type == 'analysis':
            prompt = template.format(
                aspect=random.choice(['sentiment', 'tone', 'style']),
                content=self.faker.paragraph()
            )
        elif template_type == 'translation':
            prompt = template.format(
                language=random.choice(['Spanish', 'French', 'German']),
                text=self.faker.sentence()
            )
        else:  # code
            prompt = template.format(
                language=random.choice(['Python', 'JavaScript', 'Java']),
                task=self.faker.bs()
            )
            
        return {
            'prompt': prompt,
            'template_type': template_type,
            'max_tokens': random.randint(50, 2000),
            'temperature': round(random.uniform(0.0, 1.0), 2),
            'timestamp': self._generate_timestamp().isoformat(),
            'request_id': str(uuid.uuid4())
        }

class DatabaseGenerator(BaseGenerator):
    """Generator for database-related test data."""
    
    def generate_record(self, table_name: str) -> Dict[str, Any]:
        """Generate a database record based on table type."""
        record = {
            'id': str(uuid.uuid4()),
            'created_at': self._generate_timestamp().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'is_active': random.choice([True, False])
        }
        
        if table_name == 'users':
            record.update({
                'username': self.faker.user_name(),
                'email': self.faker.email(),
                'first_name': self.faker.first_name(),
                'last_name': self.faker.last_name(),
                'address': self.faker.address(),
                'phone': self.faker.phone_number()
            })
        elif table_name == 'products':
            record.update({
                'name': self.faker.catch_phrase(),
                'description': self.faker.text(max_nb_chars=200),
                'price': round(random.uniform(10.0, 1000.0), 2),
                'category': random.choice(['Electronics', 'Books', 'Clothing', 'Food']),
                'stock': random.randint(0, 1000)
            })
        elif table_name == 'orders':
            record.update({
                'user_id': str(uuid.uuid4()),
                'total_amount': round(random.uniform(20.0, 5000.0), 2),
                'status': random.choice(['pending', 'processing', 'shipped', 'delivered']),
                'shipping_address': self.faker.address(),
                'payment_method': random.choice(['credit_card', 'paypal', 'bank_transfer'])
            })
            
        return record

class APIGenerator(BaseGenerator):
    """Generator for API-related test data."""
    
    def generate_request(self, endpoint: str) -> Dict[str, Any]:
        """Generate API request data."""
        request = {
            'request_id': str(uuid.uuid4()),
            'timestamp': self._generate_timestamp().isoformat(),
            'client_id': self.faker.uuid4(),
            'api_version': f"v{random.randint(1, 3)}"
        }
        
        if endpoint == '/users':
            request['data'] = {
                'username': self.faker.user_name(),
                'email': self.faker.email(),
                'password': self.faker.password()
            }
        elif endpoint == '/products':
            request['data'] = {
                'name': self.faker.catch_phrase(),
                'price': round(random.uniform(10.0, 1000.0), 2),
                'description': self.faker.text()
            }
        elif endpoint == '/orders':
            request['data'] = {
                'user_id': str(uuid.uuid4()),
                'products': [str(uuid.uuid4()) for _ in range(random.randint(1, 5))],
                'shipping_address': self.faker.address()
            }
            
        return request
    
    def generate_response(self, status_code: int = None) -> Dict[str, Any]:
        """Generate API response data."""
        if not status_code:
            status_code = random.choice([200, 201, 400, 401, 403, 404, 500])
            
        response = {
            'status_code': status_code,
            'timestamp': datetime.now().isoformat(),
            'request_id': str(uuid.uuid4())
        }
        
        if 200 <= status_code < 300:
            response['success'] = True
            response['data'] = {
                'id': str(uuid.uuid4()),
                'created_at': datetime.now().isoformat()
            }
        else:
            response['success'] = False
            response['error'] = {
                'code': f"ERR_{status_code}",
                'message': self.faker.sentence(),
                'details': self.faker.paragraph()
            }
            
        return response

class SecurityGenerator(BaseGenerator):
    """Generator for security-related test data."""
    
    def generate_auth_token(self, token_type: str = 'jwt') -> Dict[str, Any]:
        """Generate authentication token data."""
        expiry = datetime.now() + timedelta(hours=random.randint(1, 24))
        
        token_data = {
            'token_type': token_type,
            'user_id': str(uuid.uuid4()),
            'issued_at': datetime.now().isoformat(),
            'expires_at': expiry.isoformat(),
            'scope': random.choice(['read', 'write', 'admin']),
            'issuer': self.faker.domain_name()
        }
        
        if token_type == 'jwt':
            token_data['token'] = f"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.{self.faker.sha256()}"
        else:
            token_data['token'] = self.faker.uuid4()
            
        return token_data
    
    def generate_audit_log(self, event_type: str = None) -> Dict[str, Any]:
        """Generate security audit log data."""
        if not event_type:
            event_type = random.choice(['login', 'logout', 'access_denied', 'permission_change'])
            
        return {
            'event_id': str(uuid.uuid4()),
            'event_type': event_type,
            'timestamp': self._generate_timestamp().isoformat(),
            'user_id': str(uuid.uuid4()),
            'ip_address': self.faker.ipv4(),
            'user_agent': self.faker.user_agent(),
            'status': random.choice(['success', 'failure']),
            'details': {
                'location': self.faker.city(),
                'device': random.choice(['mobile', 'desktop', 'tablet']),
                'severity': random.choice(['low', 'medium', 'high'])
            }
        }
