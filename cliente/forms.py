from django import forms

class CriarContaForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem.")

        return cleaned_data

nacionalidades = [('Brasileiro', 'Brasileiro'), ('Estrangeiro', 'Estrangeiro')]
estados_civis = [('Solteiro', 'Solteiro'), ('Casado', 'Casado'), ('Divorciado', 'Divorciado'), ('Viuvo', 'Viúvo')]
estados = [('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), 
           ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), 
           ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), 
           ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')
]


class CriarClienteForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cpf = forms.CharField(label='CPF', max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(label='Telefone', max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_nascimento = forms.DateField(label='Data de Nascimento', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    nacionalidade = forms.ChoiceField(label='Nacionalidade', choices=nacionalidades, widget=forms.Select(attrs={'class': 'form-control'}))
    estado_civil = forms.ChoiceField(label='Estado Civil', choices=estados_civis, widget=forms.Select(attrs={'class': 'form-control'}))
    renda_mensal = forms.DecimalField(label='Renda Mensal', max_digits=10, decimal_places=2, widget=forms.TextInput(attrs={'class': 'form-control'}))
    logradouro = forms.CharField(label='Logradouro', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    numero = forms.IntegerField(label='Número', widget=forms.TextInput(attrs={'class': 'form-control'}))
    complemento = forms.CharField(label='Complemento', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    bairro = forms.CharField(label='Bairro', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cidade = forms.CharField(label='Cidade', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    estado = forms.ChoiceField(label='Estado', choices=estados, widget=forms.Select(attrs={'class': 'form-control'}))
    cep = forms.CharField(label='CEP', max_length=8, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        # validações necessárias

        return cleaned_data