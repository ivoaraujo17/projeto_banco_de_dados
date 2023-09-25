from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
#from .forms import FormCriarConta  # Importe o formulário personalizado
from django.utils.datetime_safe import datetime

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')


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