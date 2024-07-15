from django import forms 
from django.contrib.auth.models import User

    
class RegisterForm(forms.ModelForm):

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

        widgets = {
            'first_name' : forms.TextInput(attrs={
                'placeholder' : 'Type yuor first name here',
                'class' : 'input text-input'
            }),

            'password' : forms.PasswordInput(attrs={
                'placeholder' : 'Type yuor Password here'
            })
        }
