from django.db import models

# Create your models here.
class Concessao(models.Model):
    concessao = models.AutoField(primary_key=True)
    cliente = models.ForeignKey('cliente.Cliente', related_name='cliente', on_delete=models.PROTECT, to_field='cpf')
    conta = models.ForeignKey('conta.Conta_bancaria', related_name='conta_bancaria', on_delete=models.PROTECT, to_field='numero')
    produto = models.ForeignKey('produto.Produto', related_name='produtos', on_delete=models.PROTECT, to_field='produto')
    gerente = models.ForeignKey('gerente.Gerente', related_name='gerente', on_delete=models.PROTECT, to_field='cpf')
    valor_contratado = models.FloatField()
    data_primeiro_vencimento = models.DateField(format('%d/%m/%Y'))
    qtd_parcelas = models.IntegerField()
    juros = models.FloatField()
    valor_parcela = models.FloatField()
    valor_total = models.FloatField()
    status = models.CharField(choices=[('Aprovado', 'Aprovado'), ('Negado', 'Negado'), ('Em Analise', 'Em Analise')], max_length=15)

def __str__(self):
        return self.id_concessao