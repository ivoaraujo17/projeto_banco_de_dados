# Generated by Django 4.2.5 on 2023-10-15 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerente', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gerente',
            name='id',
        ),
        migrations.AlterField(
            model_name='gerente',
            name='cpf',
            field=models.CharField(max_length=11, primary_key=True, serialize=False, unique=True),
        ),
    ]
