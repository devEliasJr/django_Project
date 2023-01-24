from unittest import TestCase

from parameterized import parameterized

from authors.forms import RegisterForm


class AuthorRegisterFormUnitTest(TestCase):
    @parameterized.expand([
        ('username', 'Seu nome de usuario'),
        ('email', 'Seu e-mail'),
        ('first_name', 'Ex.: Jose'),
        ('last_name', 'Ex.: Silva'),
        ('password', 'Digite a sua senha'),
        ('password2', 'Repita a sua senha'),
    ])
    def test_first_name_placeholder(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)
