from django.db import models
from django.utils import timezone

nacionalidades = [('Brasileiro', 'Brasileiro'), ('Estrangeiro', 'Estrangeiro')]
estados_civis = [('Solteiro', 'Solteiro'), ('Casado', 'Casado'), ('Divorciado', 'Divorciado'), ('Viuvo', 'Viúvo')]
estados = [('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), 
           ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), 
           ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), 
           ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')
]

class Cliente(models.Model):
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=11, unique=True, primary_key=True)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    nacionalidade = models.CharField(choices= nacionalidades, max_length=11)
    estado_civil = models.CharField(choices= estados_civis, max_length=11)
    renda_mensal = models.FloatField()
    logradouro = models.CharField(max_length=200)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=50, blank=True)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(choices = estados, max_length=2)
    cep = models.CharField(max_length=8)
    data_entrada = models.DateTimeField(default=timezone.now)
    ultima_atualizacao = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email
