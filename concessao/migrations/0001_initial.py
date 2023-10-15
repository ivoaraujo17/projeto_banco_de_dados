# Generated by Django 4.2.5 on 2023-10-15 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conta', '0003_alter_conta_bancaria_gerente'),
        ('produto', '0001_initial'),
        ('cliente', '0001_initial'),
        ('gerente', '0002_remove_gerente_id_alter_gerente_cpf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concessao',
            fields=[
                ('concessao', models.AutoField(primary_key=True, serialize=False)),
                ('valor_contratado', models.FloatField()),
                ('data_primeiro_vencimento', models.DateField()),
                ('qtd_parcelas', models.IntegerField()),
                ('juros', models.FloatField()),
                ('valor_parcela', models.FloatField()),
                ('valor_total', models.FloatField()),
                ('status', models.CharField(choices=[('Aprovado', 'Aprovado'), ('Negado', 'Negado'), ('Em Analise', 'Em Analise')], max_length=15)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cliente', to='cliente.cliente')),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='conta_bancaria', to='conta.conta_bancaria')),
                ('gerente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='gerente', to='gerente.gerente')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='produto', to='produto.produto')),
            ],
        ),
    ]
