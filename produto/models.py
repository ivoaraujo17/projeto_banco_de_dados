from django.db import models

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.CharField(choices=[('Emprestimo', 'Emprestimo'), ('Financiamento', 'Financiamento'), ('Concorcio', 'Concorcio')], 
                            max_length=13)
    disponibilidade = models.CharField(choices=[('Corrente, Poupança, Salario','Corrente, Poupança, Salario'), ('Corrente', 'Corrente'),
                                                ('Corrente, Salario', 'Corrente, Salario')], max_length=80)
    
    valor_maximo = models.FloatField()
    
    def __str__(self):
        return f'Nome: {self.nome} | Disponibilidade: {self.disponibilidade} | Valor Maximo: {self.valor_maximo}'