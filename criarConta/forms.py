from django import forms
from criarConta.models import Funcionario

class InsereFuncionarioForm(forms.ModelForm):
  class Meta:
    # Modelo base
    model = Funcionario

    # Colocar em fields apenas os campos presentes no models.py
    # Colocar em exclude os campos idfunc, senha1 e senha2
    # idfunc porque é chave primária
    # senha1 e senha2 porque estão no template html
    fields = ['registro_funcional', 'nome_completo', 'email'] 
    exclude = ['idfunc', 'senha1' 'senha2']