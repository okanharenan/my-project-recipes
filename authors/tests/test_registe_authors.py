from unittest import TestCase
from authors.forms import RegisterForm
from parameterized import parameterized
from django.test import TestCase as djangoTestCase
from django.urls import reverse

class AuthorRegisterTest(TestCase):

    @parameterized.expand([
        ('first_name', 'Ex: John'),
        ('last_name', 'Ex: Doe'),
        ('username', 'Your username'),
        ('email', 'Ex: youremail@email.com'),
        ('password', 'Your Password'),
        ('password2', 'Repeat your Password'),

    ])
    def test_first_name_placeholder_is_correct(self, field, placeholder):
        form  = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)


    @parameterized.expand([
        ('email', 'the E-mail must be valid'),
        ('username', 'Username must have letters, numbers or one be of those @.+-_,the length should be  between 4 and 150 characters'),
        ('password', 'Password must have at letter one uppercase,'
                   'one letter lowercase,'
                   'one number. the lentgh should be at least 8 characters'),
       
    ])

    def test_field_text_help(self, field, needed):
        form  = RegisterForm()
        current = form[field].field.help_text
        self.assertEqual(current, needed)

    
    @parameterized.expand([
        ('first_name', 'First name'),
        ('last_name', 'Last name'),
        ('username', 'Username'),
        ('email', 'E-mail'),
        ('password', 'Password'),
        ('password2', 'Password2'),

    ])
    
    def test_field_label(self, field, label):
        form  = RegisterForm()
        current_label = form[field].field.label
        self.assertEqual(current_label, label)

class AuthorRegisterFormIntegrationTest(djangoTestCase):
    def setUp(self, *args, **kwargs) -> None:
        self.form_data = {
            'first_name':'fisrt',
            'last_name': 'last',
            'username': 'user',
            'email': 'email',
            'password': 'Passw0rdmy',
            'password2': 'Passw0rdmy',
        }
        return super().setUp(*args, **kwargs)
    
    @parameterized.expand([
        ('first_name', 'Write yuor first name'),
        ('last_name', 'Write yuor last name'),
        ('username', 'This field must not be empty'),
        ('email', 'the E-mail must be valid'),
        ('password', 'Password must not be empty'),
        ('password2', 'Password must not be empty'),



    ])
    def test_fields_cannot_be_empty(self, field, msg):
        self.form_data[field] = ''
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg, response.content.decode('utf-8'))

    def test_username_field_min_length_shold_be_4(self):
        self.form_data['username'] = 'joo' 
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'Username must be have at least 4 characters'
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get('username'))


    def test_username_field_max_length_shold_be_150(self):
        self.form_data['username'] = "A" * 151
        url = reverse('authors:create')
        response = self.client.post(url , data=self.form_data, follow=True)
        msg = 'Username must have less than 150 characters'
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get('username'))

    def test_password_field_have_lower_upper_case_letters_and_numbers(self):
        self.form_data['password'] = '$Aabc123'
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = ('Password must have at letter one uppercase,'
             'one letter lowercase,'
             'one number. the lentgh should be at least 8 characters')
        

        self.assertIn(msg, response.context['form'].errors.get('password'))
        self.assertIn(msg, response.content.decode('utf-8'))

        self.form_data['password'] = 'abc123'
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        self.assertNotIn(msg, response.context['form'].errors.get('password'))

    def test_password_and_password_confirmation_are_equal(self):
        self.form_data['password'] = '@A123abc123'
        self.form_data['password2'] = '@A123abc1234'
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'Password 1 and Password 2 must be equal'

        self.assertIn(msg, response.context['form'].errors.get('password'))
        self.assertIn(msg, response.content.decode('utf-8'))

        self.form_data['password'] = '@A123abc123'
        self.form_data['password2'] = '@A123abc123'
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        self.assertNotIn(msg, response.context['form'].errors.get('password'))
