from django.urls import path
from criarConta.views import criarConta

urlpatterns = [
    path('criarConta/', criarConta),
]