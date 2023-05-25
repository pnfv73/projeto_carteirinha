from django.contrib import messages
from django.shortcuts import render, redirect
from criarConta.models import Funcionario
from .forms import InsereFuncionarioForm

def criarConta(request):
    if request.method == 'POST':
        form = InsereFuncionarioForm(request.POST)

        if form.is_valid():
            registro_funcional = form.cleaned_data.get('registro_funcional')
            nome_completo = form.cleaned_data.get('nome_completo')
            email = form.cleaned_data.get('email')            
            senha1 = request.POST.get("senha1")
            senha2 = request.POST.get("senha2")
            # A variável senha recebe senha1, mas pode ser senha2.
            # A gravação dos dados só acontece se senha1 for igual a senha2.
            senha = request.POST.get("senha1")             
            error_messages = []            

            if Funcionario.objects.filter(registro_funcional=registro_funcional).exists():
                error_messages.append('O registro funcional já foi usado.')

            if Funcionario.objects.filter(email=email).exists():
                error_messages.append('O email digitado já foi usado.') 

            if senha1 != senha2:                
                error_messages.append('As senhas não são as mesmas.')                

            if error_messages:
                error_message = '<br>'.join(error_messages)
                messages.error(request, error_message)

            else:
                gravaDados = Funcionario(registro_funcional=registro_funcional, nome_completo=nome_completo, email=email, senha=senha)
                gravaDados.save()

                return redirect('sucesso')

    else:
        form = InsereFuncionarioForm()
    
    return render(request, 'criarConta/criar_conta.html', {'form': form})

def sucesso(request):
    return render(request, 'criarConta/sucesso.html')
