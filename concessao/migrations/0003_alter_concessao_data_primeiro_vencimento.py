# Generated by Django 4.2.5 on 2023-10-19 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concessao', '0002_alter_concessao_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concessao',
            name='data_primeiro_vencimento',
            field=models.DateField(verbose_name='%d/%m/%Y'),
        ),
    ]