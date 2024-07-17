from django import forms 
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def add_attr(field, attr_name, attr_new_val):
    existing_attr = field.widget.attrs.get('attr_name', '')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_val}'.strip() 

def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)
    
class RegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Your Username')
        add_placeholder(self.fields['email'], 'Youre-mail@email.com')
        add_placeholder(self.fields['first_name'], 'Nome')
        add_placeholder(self.fields['last_name'], 'Sobrenome')
        add_attr(self.fields['username'], 'css', 'a-css-class')


    password = forms. CharField(
    
        widget= forms.PasswordInput(attrs={
            'placeholder': 'Type yuor Password here',
            'class' : 'input text-input'
        }),
        error_messages={
            'requerid': 'Password must not be empty'
        },

        help_text=(
            'Password must have at least one uppercase letter'

            'one lowercase letter  and one number. The length should be '

            'at lest 8 characters.'
    )
        
    )

    password2 = forms.CharField(
        
        widget= forms.PasswordInput(attrs={
            'placeholder': 'Repeat yuor password'
        }),
        label= 'Password 2'
    )

    

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password")
        #exclude = ["last_name"] exemplo para exclusão de campo

        labels = {
            'first_name' : 'First name',
            'last_name' : 'Last name',
            'username' : 'UserName',
            'email' : 'E-mail',
            'password' : 'Password',
        }
        help_texts = {
            'email' : 'the e-mail must be valid.'
        }
        
        error_messages = {
            'username' : {
                'requerid': 'this field must not be empty'
            }
        }

    
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError(
                'Password and password2 must be equal',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': [
                    password_confirmation_error,
                ],
            })

