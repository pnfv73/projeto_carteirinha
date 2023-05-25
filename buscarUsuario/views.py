from django.shortcuts import render

def buscarUsuario(request):
    return render(request, 'buscarUsuario/buscar_usuario.html')