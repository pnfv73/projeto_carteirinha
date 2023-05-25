from django.urls import path
from login.views import login
from login.views import credencial

urlpatterns = [
    #path('', login, name='login_funcionario'), #name = nome da path para indicar em outra página que eu vou clicar e ir para essa página
    path('', credencial, name='credencial'),
]