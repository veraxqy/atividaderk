"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from biblioteca.views import index
from biblioteca.views import listar_Cidade
from biblioteca.views import criar_Cidade
from biblioteca.views import update_Cidade
from biblioteca.views import delete_Cidade
from biblioteca.views import consulta
from biblioteca.views import busca
from biblioteca.views import grupo

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', index, name='url_inicial'),
    path('grupo/', grupo, name='url_grupo'),
    path('consulta/', consulta, name='url_consulta'),
    path('busca/', busca, name='url_busca'),
    path('listar_cidades/', listar_Cidade, name='url_listar_cidades'),
    path('criar_cidade/', criar_Cidade, name='url_criar_cidades'),
    path('update_cidade/<int:pk>/', update_Cidade, name='url_update_cidade'),
    path('delete_cidade/<int:pk>/', delete_Cidade, name='url_delete_cidade'),
]