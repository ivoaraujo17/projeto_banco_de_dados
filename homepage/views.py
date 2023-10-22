from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
#from .forms import FormCriarConta  # Importe o formulário personalizado
from django.utils.datetime_safe import datetime

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect('conta_bancaria:pagina_inicial')
    return render(request, 'homepage.html')
