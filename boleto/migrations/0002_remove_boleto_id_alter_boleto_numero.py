# Generated by Django 4.2.3 on 2023-10-24 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boleto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boleto',
            name='id',
        ),
        migrations.AlterField(
            model_name='boleto',
            name='numero',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
