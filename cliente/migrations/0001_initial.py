# Generated by Django 4.2.5 on 2023-10-14 11:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=14)),
                ('data_nascimento', models.DateField()),
                ('nacionalidade', models.CharField(choices=[('Brasileiro', 'Brasileiro'), ('Estrangeiro', 'Estrangeiro')], max_length=11)),
                ('estado_civil', models.CharField(choices=[('Solteiro', 'Solteiro'), ('Casado', 'Casado'), ('Divorciado', 'Divorciado'), ('Viuvo', 'Viúvo')], max_length=11)),
                ('renda_mensal', models.FloatField()),
                ('logradouro', models.CharField(max_length=200)),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(blank=True, max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')], max_length=2)),
                ('cep', models.CharField(max_length=8)),
                ('data_entrada', models.DateTimeField(default=django.utils.timezone.now)),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
