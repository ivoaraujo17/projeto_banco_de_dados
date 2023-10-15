from django.db import models
from django import forms

# Create your models here.
class CederConcessaoForm(forms.Form):
    valor_contratado = forms.DecimalField(label='Valor Contratado', max_digits=10, decimal_places=2, widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_primeiro_vencimento = forms.DateField(label='Data do Primeiro Vencimento', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    qtd_parcelas = forms.IntegerField(label='Quantidade de Parcelas', widget=forms.TextInput(attrs={'class': 'form-control'}))
