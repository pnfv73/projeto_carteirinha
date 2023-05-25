from django.db import models

# Criar tabelas do banco. Cada tabela corresponde a uma classe e as colunas ficam dentro dentro de cada classe.
# null = não pode ser nulo, blank = não pode ser vazio/preenchido com espaços

class Funcionario(models.Model):
    idfunc = models.AutoField(primary_key=True) #chave primária
    registro_funcional = models.CharField(max_length=10, null=False, blank=False) #registro funcional
    nome_completo = models.CharField(max_length=100, null=False, blank=False) #nome
    email = models.EmailField(max_length=30)
    senha = models.CharField(max_length=15) #senha 

    def __str__(self):
        return self.nome