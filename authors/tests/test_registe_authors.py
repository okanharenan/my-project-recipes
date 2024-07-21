from django.test import TestCase
from authors.forms import RegisterForm
from parameterized import parameterized

class AuthorRegisterTest(TestCase):

    @parameterized.expand([
        ('first_name', 'Ex: John'),
        ('last_name', 'Ex: Doe'),
        ('username', 'Your username'),
        ('email', 'Ex: youremail@email.com'),
    ])
    def test_first_name_placeholder_is_correct(self, field, placeholder):
        form  = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)