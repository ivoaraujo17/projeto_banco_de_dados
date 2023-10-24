from django.db import models

# Create your models here.
class Boleto(models.Model):
    numero = models.AutoField(primary_key=True)
    valor = models.FloatField(null=False, blank=False)
    data_vencimento = models.DateField(null=False, blank=False)
    data_pagamento = models.DateField(null=True, blank=True)
    pago = models.BooleanField(default=False, null=True)
    conta = models.ForeignKey('conta.Conta_bancaria', on_delete=models.CASCADE, to_field='numero')

    def __str__(self):
        return self.numero