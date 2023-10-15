from django.shortcuts import render

# Create your views here.

def emprestimo(request):
    return render(request, 'emprestimo_detalhes.html')

def financiamento(request):
    return render(request, 'financiamento_detalhes.html')

def consorcio(request):
    return render(request, 'consorcio_detalhes.html')

    