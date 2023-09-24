from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import FormCriarConta  # Importe o formulário personalizado
from .models import CustomUser  # Importe o modelo de usuário personalizado
from django.utils.datetime_safe import datetime

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')


# Classe de criar conta
def criar_conta(request):
    if request.method == 'POST':
        form = FormCriarConta(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')  # Use 'email' para coletar o email
            password = form.cleaned_data.get('password1')
            cpf = form.cleaned_data.get('cpf')
            nome = form.cleaned_data.get('nome')
            telefone = form.cleaned_data.get('telefone')
            data_nascimento = form.cleaned_data.get('data_nascimento')
            nacionalidade = form.cleaned_data.get('nacionalidade')
            estado_civil = form.cleaned_data.get('estado_civil')
            renda_mensal = form.cleaned_data.get('renda_mensal')
            logradouro = form.cleaned_data.get('logradouro')
            numero = form.cleaned_data.get('numero')
            complemento = form.cleaned_data.get('complemento')
            bairro = form.cleaned_data.get('bairro')
            cidade = form.cleaned_data.get('cidade')
            estado = form.cleaned_data.get('estado')
            cep = form.cleaned_data.get('cep')
            # Crie um novo usuário CustomUser com o email
            user = CustomUser.objects.create_user(email=email, 
                                                    password=password,
                                                    cpf=cpf,
                                                    nome=nome,
                                                    telefone=telefone,
                                                    data_nascimento=data_nascimento,
                                                    nacionalidade=nacionalidade,
                                                    estado_civil=estado_civil,
                                                    renda_mensal=renda_mensal,
                                                    logradouro=logradouro,
                                                    numero=numero,
                                                    complemento=complemento,
                                                    bairro=bairro,
                                                    cidade=cidade,
                                                    estado=estado,
                                                    cep=cep,
                                                    data_entrada=datetime.now(),
                                                    ultima_atualizacao=datetime.now()
                                                    )

            return redirect('homepage:login')  # Redirecionar para a página inicial ou outra página após o registro
    else:
        form = FormCriarConta()  # Use o formulário personalizado
    
    return render(request, 'criar_conta.html', {'form': form})


# login
def fazer_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')  # username pode ser email no seu caso
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Autenticação bem-sucedida, redirecione para a página desejada
                return redirect('homepage:homepage')  # Redirecionar para a página inicial ou outra página após o login
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})