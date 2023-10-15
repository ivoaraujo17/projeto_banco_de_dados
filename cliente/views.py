from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from django.http import HttpResponse
from django.views import View
from .forms import CriarContaForm, CriarClienteForm
from .models import Cliente
from django.utils import timezone


def criar_usuario(request):
    if request.method == 'POST':
        form = CriarContaForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, password=password, email=username)
                messages.success(request, 'Usuário criado com sucesso!')
                return redirect('cliente:login')
            else:
                return render(request, 'criar_conta.html', {'form': form, 'erro': 'Usuário já existe.'})
        else:
            return render(request, 'criar_conta.html', {'form': form})     
    else:
        form = CriarContaForm()

    return render(request, 'criar_conta.html', {'form': form})


def criar_cliente(request):
    # Verificar se o cliente já tem cadastro
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM cliente_cliente WHERE email = %s", [request.user.email])
        cliente_existe = cursor.fetchone()[0]

    if cliente_existe:
        return redirect('conta_bancaria:pagina_inicial')

    if request.method == 'POST':
        form = CriarClienteForm(request.POST)
        if form.is_valid():
            dados_formulario = form.cleaned_data

            consulta_sql = """
                INSERT INTO cliente_cliente (email, cpf, nome, telefone,data_nascimento, nacionalidade, estado_civil, renda_mensal, 
                                            logradouro, numero, complemento, bairro, cidade, estado, cep, data_entrada, 
                                            ultima_atualizacao)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
            """
            
            # Parâmetros para a consulta SQL
            parametros = [
                request.user.email,
                dados_formulario['cpf'],
                dados_formulario['nome'],
                dados_formulario['telefone'],
                dados_formulario['data_nascimento'],
                dados_formulario['nacionalidade'],
                dados_formulario['estado_civil'],
                dados_formulario['renda_mensal'],
                dados_formulario['logradouro'],
                dados_formulario['numero'],
                dados_formulario['complemento'],
                dados_formulario['bairro'],
                dados_formulario['cidade'],
                dados_formulario['estado'],
                dados_formulario['cep'],
                timezone.now(),
                timezone.now()
            ]

            with connection.cursor() as cursor:
                cursor.execute(consulta_sql, parametros)
            
            return redirect('conta_bancaria:pagina_inicial')
    else:
        form = CriarClienteForm()
    return render(request, 'cadastrar_cliente.html', {'form': form})
