from django import forms

datas_vencimento = [('30', '30'), ('45', '45'), ('60', '60')]

quantidade_parcelas_emprestimo = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), 
                       ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('18', '18'), ('24', '24'), ('30', '30'),
                       ('36', '36'), ('42', '42'), ('48', '48'), ('54', '54'), ('60', '60'), ('66', '66'), ('72', '72')]

quantidade_parcelas_financiamento = [('12','12'), ('24','24'), ('36','36'), ('48','48'), ('60','60'), ('72','72'), ('84','84'), 
                                     ('96','96'), ('108','108'), ('120','120'), ('240', '240'), ('300', '300'), ('360', '360')]

quantidade_parcelas_consorcio = [('12','12'), ('24','24'), ('36','36'), ('48','48'), ('60','60'), ('72','72'), ('84','84'),
                                    ('96','96'), ('108','108'), ('120','120')]


class CederConcessaoEmprestimoForm(forms.Form):
    valor_contratado = forms.DecimalField(label='Valor Contratado', max_digits=10, decimal_places=2, 
                                          widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_primeiro_vencimento = forms.ChoiceField(label='Data do Primeiro Pagamento', choices= datas_vencimento, 
                                                 widget=forms.Select(attrs={'class': 'form-control'}))
    qtd_parcelas = forms.ChoiceField(label='Quantidade de Parcelas', choices= quantidade_parcelas_emprestimo, 
                                                 widget=forms.Select(attrs={'class': 'form-control'}))
    def clean(self):
        cleaned_data = super().clean()
        # validações necessárias

        return cleaned_data

class CederConcessaoFinanciamentoForm(forms.Form):
    valor_contratado = forms.DecimalField(label='Valor Contratado', max_digits=10, decimal_places=2, 
                                          widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_primeiro_vencimento = forms.ChoiceField(label='Data do Primeiro Pagamento', choices= datas_vencimento, 
                                                 widget=forms.Select(attrs={'class': 'form-control'}))
    qtd_parcelas = forms.ChoiceField(label='Quantidade de Parcelas', choices= quantidade_parcelas_financiamento, 
                                                 widget=forms.Select(attrs={'class': 'form-control'}))
    
    def clean(self):
        cleaned_data = super().clean()
        # validações necessárias

        return cleaned_data
    
class CederConcessaoConsorcioForm(forms.Form):
    valor_contratado = forms.DecimalField(label='Valor Contratado', max_digits=10, decimal_places=2, 
                                          widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_primeiro_vencimento = forms.ChoiceField(label='Data do Primeiro Pagamento', choices= datas_vencimento, 
                                                 widget=forms.Select(attrs={'class': 'form-control'}))
    qtd_parcelas = forms.ChoiceField(label='Quantidade de Parcelas', choices= quantidade_parcelas_consorcio, 
                                                 widget=forms.Select(attrs={'class': 'form-control'}))
    
    def clean(self):
        cleaned_data = super().clean()
        # validações necessárias

        return cleaned_data
