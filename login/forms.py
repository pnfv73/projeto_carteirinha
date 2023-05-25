from django import forms
from criarConta.models import Funcionario

class loginForm(forms.ModelForm):
    class Meta:
        # Modelo base
        model = Funcionario
        fields = ['email', 'senha']