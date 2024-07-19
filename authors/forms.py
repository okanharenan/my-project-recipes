from django import forms
import re
from django.forms import widgets
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')
    if not regex.match(password):
        raise ValidationError(
            'Password must have at least one uppercase letter'
            'one lowercase letter' 
            'and one number. The length should be at least 8 characters.',
            code='invalid'
        )
    
def add_attr(field, attr_name, attr_new_val):
    existing_attr = field.widget.attrs.get(attr_name,'')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_val}'.strip()

def add_placeholder(field, placeholder_val):
    add_attr(field,'placeholder', placeholder_val)

class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__()
        add_placeholder(self.fields['first_name'], 'Ex: John')
        add_placeholder(self.fields['last_name'], 'Ex: Doe')
        add_placeholder(self.fields['username'], 'Your username')
        add_placeholder(self.fields['email'], 'Ex: youremail@email.com')


    password = forms.CharField(
        required=True,
        widget = forms.PasswordInput(attrs= {'placeholder': 'Your Password'}),
        error_messages= {
            'required' : 'Password must not be empty'
        },
        help_text=('Password must have at letter one uppercase,'
                   'one letter lowercase,'
                   'one number. the lentgh should be at least 8 characters')
    )

    password2 = forms.CharField(
        required=True,
        widget = forms.PasswordInput(attrs= {'placeholder': 'Repeat your Password'}),
         error_messages= {
            'required' : 'Password must not be empty'
        }
    )
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'username' : 'Username',
            'password' : 'Password',
        }

        help_texts = {
            'email': 'the E-mail must be valid'
        }

        error_messages = {
            'username': {
                'required': 'this field must be empty'
            }
        }

        def clean_password(self):
            data = self.cleaned_data.get('password')
            if 'atenção' in data:
                raise ValidationError(
                    "Não digite atenção na sua senha"
                )
            return data