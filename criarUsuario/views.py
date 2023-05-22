from django.shortcuts import render

def criarUsuario(request):
    return render(request, 'passo1_dadospessoais.html')