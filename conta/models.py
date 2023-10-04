from django.db import models

# Create your models here.

class Conta_bancaria(models.Model):
    numero = models.IntegerField(unique=True)
    id_cliente = models.ForeignKey('cliente.Cliente', related_name='contas_bancarias', on_delete=models.CASCADE)
    tipo_conta = models.CharField(choices=[('Poupança', 'Poupança'), ('Corrente', 'Corrente'), ('Salario', 'Salario')], max_length=8)
    agencia = models.IntegerField()
    gerente = models.ForeignKey('gerente.Gerente', related_name='contas_gerenciadas', on_delete=models.PROTECT)
    saldo = models.FloatField()
    limite_especial = models.FloatField()

    def __str__(self):
        return f'{self.numero}:{self.id_cliente}'