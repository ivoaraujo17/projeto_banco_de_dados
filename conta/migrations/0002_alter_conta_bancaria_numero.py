# Generated by Django 4.2.5 on 2023-10-14 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conta_bancaria',
            name='numero',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
