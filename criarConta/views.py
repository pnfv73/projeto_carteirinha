from django.shortcuts import render

def criarConta(request):
    return render(request, 'criar_conta.html')