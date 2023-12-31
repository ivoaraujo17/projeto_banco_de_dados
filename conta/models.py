from django.db import models

# Create your models here.

class Conta_bancaria(models.Model):
    numero = models.AutoField(primary_key=True)
    cliente = models.ForeignKey('cliente.Cliente', related_name='contas_bancarias', on_delete=models.CASCADE, to_field='cpf')
    tipo_conta = models.CharField(choices=[('Poupança', 'Poupança'), ('Corrente', 'Corrente'), ('Salario', 'Salario')], max_length=8)
    agencia = models.IntegerField()
    gerente = models.ForeignKey('gerente.Gerente', related_name='contas_gerenciadas', on_delete=models.PROTECT, to_field='cpf')
    saldo = models.FloatField()
    limite_especial = models.FloatField()

    def __str__(self):
        return f'Conta: {self.numero} | Tipo: {self.tipo_conta} | Cliente: {self.cliente}'

class Transacao(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(choices=[('entrada', 'entrada'), ('saida', 'saida')], max_length=7)
    conta = models.ForeignKey('conta.Conta_bancaria', related_name='transacoes_origem', on_delete=models.PROTECT, to_field='numero')
    valor = models.FloatField()
    descricao = models.CharField(max_length=100)
    data_hora = models.DateTimeField(auto_now_add=True)


