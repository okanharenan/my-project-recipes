import re
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=[0-9]).{8,}$')
    if not regex.match(password):
        raise ValidationError(
            ('Password must have at letter one uppercase,'
             'one letter lowercase,'
             'one number. the lentgh should be at least 8 characters'),
             code='invalid'
        )
    
def add_attr(field, attr_name, attr_new_val):
    existing_attr = field.widget.attrs.get(attr_name,'')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_val}'.strip()

def add_placeholder(field, placeholder_val):
    add_attr(field,'placeholder', placeholder_val)

class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['first_name'], 'Ex: John')
        add_placeholder(self.fields['last_name'], 'Ex: Doe')
        add_placeholder(self.fields['username'], 'Your username')
        add_placeholder(self.fields['email'], 'Ex: youremail@email.com')
        add_attr(self.fields['first_name'], 'requerid', 'Fisrt_name must not be empty')

    
   
    first_name = forms.CharField(
            error_messages={'required': 'Write yuor first name'},
            label='First name',
            )
    
    last_name = forms.CharField(
            error_messages={'required': 'Write yuor last name',},
            label='Last name',
            )
    
    username = forms.CharField(
        error_messages= {'required':'This field must not be empty',
                        'min_length':'Username must be have at least 4 characters',
                        'max_length': 'Username must have less than 150 characters'},
        label='Username',
        help_text=('Username must have letters, numbers or one be of those @.+-_,'
                   'the length should be  between 4 and 150 characters'),
                   min_length=4 , max_length=150

    )

    email = forms.EmailField(
        error_messages={'required': 'the E-mail must be valid'},
        label='E-mail',
         help_text = 'the E-mail must be valid'
    
    )

    password = forms.CharField(
        required=True,
        widget = forms.PasswordInput(attrs= {'placeholder': 'Your Password'}),
        error_messages= {
            'required' : 'Password must not be empty',
            
        },
        help_text=('Password must have at letter one uppercase,'
                   'one letter lowercase,'
                   'one number. the lentgh should be at least 8 characters'),

        validators = [strong_password],

        label='Password',

        
        
    )

    password2 = forms.CharField(
        required=True,
        widget = forms.PasswordInput(attrs= {'placeholder': 'Repeat your Password'}),
         error_messages= {
            'required' : 'Password must not be empty'
        },

        label='Password2'
    )
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'password2'
        ]

           
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError(
                "Password 1 and Password 2 must be equal",
                code = "invalid")
            raise ValidationError ({
                "password" : password_confirmation_error,
                "password2": [
                    password_confirmation_error
                ]
            })