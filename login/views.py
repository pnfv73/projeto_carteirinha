from django.contrib import messages
from django.shortcuts import render, redirect
from criarConta.models import Funcionario
from login.forms import loginForm
from django.contrib import auth

def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')            
            senha = form.cleaned_data.get("senha")             
            error_messages = []

            user = auth.authenticate(username=email, password=senha) 

            if user is not None:
                if user.is_active:
                    print ("Você forneceu um username e senha corretos!")
                else:
                   print ("Sua conta foi desabilitada!")
            else:
                print ("Seu username e senha estavam incorretos.")


#            if user is not None:
#                print('passou')
#                auth.login(request, user)
#                # Session is created here
#                #return redirect('logado')
#                #if Funcionario.objects.filter(email=email, senha=senha).exists():
#                error_messages.append('Logado!')
#            else:
#                error_messages.append('Email ou senha incorreto!')                                  
#
#            if error_messages:
#                error_message = '<br>'.join(error_messages)
#                messages.error(request, error_message)
    else:
        form = loginForm()
    
    return render(request, 'login/login.html', {'form': form})

def logado(request):
    return render(request, 'criarConta/sucesso.html')


def credencial(request):
    return render (request, 'criarUsuario/credencial_v2.html')
