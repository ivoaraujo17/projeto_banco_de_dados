from django import forms


class FormTransferencia(forms.Form):
    numero_conta = forms.IntegerField(label='Número da conta', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    valor = forms.FloatField(label='Valor', widget=forms.NumberInput(attrs={'class': 'form-control'}))
