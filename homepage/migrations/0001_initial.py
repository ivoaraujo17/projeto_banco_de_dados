# Generated by Django 4.2.5 on 2023-09-24 12:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('nome', models.CharField(blank=True, max_length=30)),
                ('telefone', models.CharField(max_length=14)),
                ('data_nascimento', models.DateField()),
                ('nacionalidade', models.CharField(choices=[('Brasileiro', 'Brasileiro'), ('Estrangeiro', 'Estrangeiro')], max_length=11)),
                ('estado_civil', models.CharField(choices=[('Solteiro', 'Solteiro'), ('Casado', 'Casado'), ('Divorciado', 'Divorciado'), ('Viúvo', 'Viúvo')], max_length=11)),
                ('renda_mensal', models.FloatField()),
                ('logradouro', models.CharField(max_length=200)),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(blank=True, max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=8)),
                ('data_entrada', models.DateTimeField(default=django.utils.timezone.now)),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
