from django.db import models

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.CharField(choices=[('Emprestimo', 'Emprestimo'), ('Financiamento', 'Financiamento'), ('Concorcio', 'Concorcio')], max_length=13)
    disponibilidade = models.IntegerField() #quanttidade de emprestimos que o banco pode fazer
    valor_maximo = models.FloatField()
    
    def __str__(self):
        return f'Nome: {self.nome} | Disponibilidade: {self.disponibilidade} | Valor Maximo: {self.valor_maximo}'