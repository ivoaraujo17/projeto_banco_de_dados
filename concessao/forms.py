from django import forms

datas_vencimento = [('30', '30 dias'), ('45', '45 dias'), ('60', '60 dias')]

quantidade_parcelas_emprestimo = [(1, '1 mês'), (2, '2 meses'), (3, '3 meses'), (4, '4 meses'), (5, '5 meses'), (6, '6 meses'), 
                                  (7, '7 meses'), (8, '8 meses'), (9, '9 meses'), (10, '10 meses'), (11, '11 meses'), (12, '12 meses'), 
                                  (18, '18 meses'), (24, '24 meses'), (30, '30 meses'), (36, '36 meses'), (42, '42 meses'), (48, '48 meses'), 
                                  (54, '54 meses'), (60, '60 meses'), (66, '66 meses'), (72, '72 meses')]


quantidade_parcelas_financiamento = [(12, '12 meses'), (24, '24 meses'), (36, '36 meses'), (48, '48 meses'), (60, '60 meses'), 
                                    (72, '72 meses'), (84, '84 meses'), (96, '96 meses'), (108, '108 meses'), (120, '120 meses'), 
                                    (240, '240 meses'), (300, '300 meses'), (360, '360 meses')]


quantidade_parcelas_consorcio = [(12, '12 meses'), (24, '24 meses'), (36, '36 meses'), (48, '48 meses'), (60, '60 meses'), 
                                 (72, '72 meses'), (84, '84 meses'), (96, '96 meses'), (108, '108 meses'), (120, '120 meses')]


valor_do_emprestimo = [(1000, '1000'), (2000, '2000'), (3000, '3000'), (4000, '4000'), (5000, '5000'), (10000, '10000'), 
                       (15000, '15000'), (20000, '20000'), (25000, '25000'), (30000, '30000')]

valor_do_financiamento = [(50000, '50000'), (60000, '60000'), (70000, '70000'), (80000, '80000'), (90000, '90000'), 
                         (100000, '100000'), (150000, '150000'), (200000, '200000'), (250000, '250000'), (300000, '300000'),
                         (400000, '400000'), (500000, '500000'), (600000, '600000'), (700000, '700000'), (800000, '800000'),
                         (900000, '900000'), (1000000, '1000000')]

valor_do_consorcio = [(20000, '20000'), (30000, '30000'), (40000, '40000'), (50000, '50000'), (60000, '60000'), 
                      (70000, '70000'), (80000, '80000'), (90000, '90000'), (100000, '100000'), (150000, '150000'), 
                      (200000, '200000')]


class EmprestimoForm(forms.Form):
    valor_contratado = forms.ChoiceField(label='Valor Contratado', choices= valor_do_emprestimo, 
                                                 widget=forms.Select(attrs={'class': 'form-control'}))
    data_primeiro_vencimento = forms.ChoiceField(label='Data do Primeiro Pagamento', choices= datas_vencimento, 
                                                 widget=forms.Select(attrs={'class': 'form-control'}))
    qtd_parcelas = forms.ChoiceField(label='Quantidade de Parcelas', choices= quantidade_parcelas_emprestimo, 
                                                 widget=forms.Select(attrs={'class': 'form-control'}))
    valor_total_pago = forms.DecimalField(label='Valor a Pagar', max_digits=10, decimal_places=2,
                                          widget=forms.TextInput(attrs={'class': 'form-control', 'required':False, 'disabled': True}))
    taxa_juros = forms.DecimalField(label='Taxa de Juros', max_digits=5, decimal_places=2,
                                    widget=forms.TextInput(attrs={'class': 'form-control', 'required':False, 'disabled': True}))
    valor_parcela = forms.DecimalField(label='Valor da Parcela', max_digits=10, decimal_places=2,
                                       widget=forms.TextInput(attrs={'class': 'form-control',  'required':False, 'disabled': True}))
    
    def clean(self):
        cleaned_data = super().clean()
        # validações necessárias

        return cleaned_data
    
class FinanciamentoForm(forms.Form):
    valor_contratado = forms.ChoiceField(label='Valor Contratado', choices= valor_do_financiamento, 
                                                 widget=forms.Select(attrs={'class': 'form-control'}))
    data_primeiro_vencimento = forms.ChoiceField(label='Data do Primeiro Pagamento', choices= datas_vencimento, 
                                                 widget=forms.Select(attrs={'class': 'form-control'}))
    qtd_parcelas = forms.ChoiceField(label='Quantidade de Parcelas', choices= quantidade_parcelas_financiamento, 
                                                 widget=forms.Select(attrs={'class': 'form-control'}))
    valor_total_pago = forms.DecimalField(label='Valor a Pagar', max_digits=10, decimal_places=2,
                                          widget=forms.TextInput(attrs={'class': 'form-control', 'required':False, 'disabled': True}))
    taxa_juros = forms.DecimalField(label='Taxa de Juros', max_digits=5, decimal_places=2,
                                    widget=forms.TextInput(attrs={'class': 'form-control', 'required':False, 'disabled': True}))
    valor_parcela = forms.DecimalField(label='Valor da Parcela', max_digits=10, decimal_places=2,
                                       widget=forms.TextInput(attrs={'class': 'form-control',  'required':False, 'disabled': True}))
    
    def clean(self):
        cleaned_data = super().clean()
        # validações necessárias

        return cleaned_data
    
class ConsorcioForm(forms.Form):
    valor_contratado = forms.ChoiceField(label='Valor Contratado', choices= valor_do_consorcio, 
                                                 widget=forms.Select(attrs={'class': 'form-control'}))
    data_primeiro_vencimento = forms.ChoiceField(label='Data do Primeiro Pagamento', choices= datas_vencimento, 
                                                 widget=forms.Select(attrs={'class': 'form-control'}))
    qtd_parcelas = forms.ChoiceField(label='Quantidade de Parcelas', choices= quantidade_parcelas_consorcio, 
                                                 widget=forms.Select(attrs={'class': 'form-control'}))
    valor_total_pago = forms.DecimalField(label='Valor a Pagar', max_digits=10, decimal_places=2,
                                          widget=forms.TextInput(attrs={'class': 'form-control', 'required':False, 'disabled': True}))
    taxa_juros = forms.DecimalField(label='Taxa de Juros', max_digits=5, decimal_places=2,
                                    widget=forms.TextInput(attrs={'class': 'form-control', 'required':False, 'disabled': True}))
    valor_parcela = forms.DecimalField(label='Valor da Parcela', max_digits=10, decimal_places=2,
                                       widget=forms.TextInput(attrs={'class': 'form-control',  'required':False, 'disabled': True}))
    
    def clean(self):
        cleaned_data = super().clean()
        # validações necessárias

        return cleaned_data

