from django.contrib.auth.tokens import PasswordResetTokenGenerator
import django_six

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (django_six.text_type(user.pk) + 
                django_six.text_type(timestamp) + 
                django_six.text_type(user.is_active))
    
generate_token = TokenGenerator()