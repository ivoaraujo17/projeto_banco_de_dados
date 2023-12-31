# Generated by Django 4.2.5 on 2023-10-15 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id_produto', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(choices=[('Emprestimo', 'Emprestimo'), ('Financiamento', 'Financiamento'), ('Concorcio', 'Concorcio')], max_length=13)),
                ('disponibilidade', models.CharField(choices=[('Corrente, Poupança, Salario', 'Corrente, Poupança, Salario'), ('Corrente', 'Corrente'), ('Corrente, Salario', 'Corrente, Salario')], max_length=80)),
                ('valor_maximo', models.FloatField()),
            ],
        ),
    ]
