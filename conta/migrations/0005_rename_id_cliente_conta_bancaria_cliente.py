# Generated by Django 4.2.3 on 2023-10-15 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0004_rename_cliente_conta_bancaria_id_cliente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conta_bancaria',
            old_name='id_cliente',
            new_name='cliente',
        ),
    ]
