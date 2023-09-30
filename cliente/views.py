from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CriarContaForm  # Importe o formulário CriarContaForm do seu aplicativo

def criar_usuario(request):
    if request.method == 'POST':
        # Crie uma instância do formulário com os dados enviados pelo usuário
        form = CriarContaForm(request.POST)

        if form.is_valid():
            # Se o formulário for válido, obtenha os dados do formulário
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Crie um novo usuário com os dados fornecidos
            user = User.objects.create_user(username=username, password=password)

            # Outras operações, como fazer login automaticamente, podem ser realizadas aqui

            # Redirecione para uma página de sucesso ou faça o que for necessário
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('homepage:homepage')  # Certifique-se de que você tem uma URL nomeada 'pagina_de_sucesso'
    
    else:
        # Se a solicitação não for um POST, crie uma instância vazia do formulário
        form = CriarContaForm()

    return render(request, 'criar_conta.html', {'form': form})
