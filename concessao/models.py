from django.db import models

# Create your models here.
class Concessao(models.Model):
    id_concessao = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey('cliente.Cliente', related_name='', on_delete=models.PROTECT, to_field='cpf')
    id_conta = models.ForeignKey('conta_bancaria.Conta_bancaria', related_name='contas_bancarias', on_delete=models.PROTECT, to_field='numero')
    id_produto = models.ForeignKey('produto.Produtos', related_name='contas_bancarias', on_delete=models.PROTECT, to_field='id_produto')
    id_gerente = models.ForeignKey('gerente.Gerente', related_name='contas_bancarias', on_delete=models.PROTECT, to_field='cpf')
    valor_contratado = models.FloatField()
    data_primeiro_vencimento = models.DateField()
    qtd_parcelas = models.IntegerField()
    juros = models.FloatField()
    valor_parcela = models.FloatField()
    valor_total = models.FloatField()
    status = models.CharField(choices=[('Aprovado', 'Aprovado'), ('Negado', 'Negado')], max_length=8)

def __str__(self):
        return self.id_concessao