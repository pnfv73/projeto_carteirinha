from django.shortcuts import render

def buscarUsuario(request):
    return render(request, 'buscar_usuario.html')