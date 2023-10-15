from django.db import models


estados = [('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), 
           ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), 
           ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), 
           ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')
]

# Create your models here.
class Gerente(models.Model):
    cpf = models.CharField(max_length=11, unique=True, primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.EmailField(unique = True)
    telefone = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    salario = models.FloatField()
    logradouro = models.CharField(max_length=200)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(choices=estados, max_length=2)

    def __str__(self):
        return f'{self.email}'