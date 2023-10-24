from django import forms

class BoletoForm(forms.Form):
    valor = forms.FloatField(label='Valor', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    data_vencimento = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))


class PagarBoleto(forms.Form):
    numero_boleto = forms.IntegerField(label='Número do boleto', widget=forms.NumberInput(attrs={'class': 'form-control'}))