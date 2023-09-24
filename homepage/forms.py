from django import forms
from .models import CustomUser

class FormCriarConta(forms.ModelForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de Senha', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = [
            'email',
            'cpf',
            'nome',
            'telefone',
            'data_nascimento',
            'nacionalidade',
            'estado_civil',
            'renda_mensal',
            'logradouro',
            'numero',
            'complemento',
            'bairro',
            'cidade',
            'estado',
            'cep',
        ]
