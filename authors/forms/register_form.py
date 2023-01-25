from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from utils.django_forms import add_placeholder, strong_password


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Seu nome de usuario')
        add_placeholder(self.fields['email'], 'Seu e-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: Jose')
        add_placeholder(self.fields['last_name'], 'Ex.: Silva')
        add_placeholder(self.fields['password'], 'Digite a sua senha')
        add_placeholder(self.fields['password2'], 'Repita a sua senha')

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'A senha é um campo obrigatório'
        },
        help_text=(
            'A senha deve conter no minimo: '
            '6 digitos, uma letra Maiuscula e uma minuscula'
        ),
        validators=[strong_password]
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
    )

    email = forms.EmailField(
        required=True,
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
        # exclude = ['first_name'] tbm posso só retirar campos
        # Inclusõe adicionais se quiser alterar os nomes padrões do django
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'username': 'Nome de Usuario',
            'email': 'E-mail',
            'password': 'Senha',
        }

        help_texts = {
            'first_name': 'Digite seu primeiro nome.',
            'email': 'digite seu email.',
        }

        error_messages = {
            'username': {
                'required': 'Esse campo é obrigatório.',
            }
        }

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError('O email informado já está registrado')

        return email

    def clean_password(self):
        data = self.cleaned_data.get('password')

        if 'atenção' in data:
            raise ValidationError(
                'Não digite %(palavrainv)s no campo password',
                code='invalido',
                params={'palavrainv': 'atenção'}
            )

        return data

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise ValidationError({
                'password': 'As senhas digitadas são diferentes',
                'password2': 'As senhas digitadas são diferentes',
            })
