from django.db import models

# Create your models here.

class Conta_bancaria(models.Model):
    numero = models.IntegerField(unique=True)
    id_cliente = models.ForeignKey('cliente.Cliente', related_name='contas_bancarias', on_delete=models.CASCADE)
    tipo_conta = models.CharField(choices=[('Poupança', 'Poupança'), ('Corrente', 'Corrente'), ('Salario', 'Salario')])
    agencia = models.IntegerField(max_length=4)
    gerente = models.ForeignKey('gerente.Gerente', related_name='contas_gerenciadas', on_delete=models.PROTECT)
    saldo = models.FloatField()
    limite_especial = models.FloatField()
