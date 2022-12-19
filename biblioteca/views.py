from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from .models import Cidades
from .forms import CidadeForm

# Create your views here.

# Inicial:
def index(request):
    return render(request, 'index.html')

def grupo(request):
    return render(request, 'grupo.html')

def consulta(request):
    return render(request, 'consulta.html')

def busca(request):
    buscar = request.GET.get('busca')
    resultados = Cidades.objects.filter(nome_cidade__icontains=buscar)
    return render(request, 'busca.html', {'resultados': resultados})

# CRUD  Cidade:
def listar_Cidade(request):
    data = {}
    data['cidade'] = Cidades.objects.all().order_by('nomecidade')
    return render(request, 'listar_cidades.html', data)

def criar_Cidade(request):
    data = {}
    form = CidadeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listar_cidades')
    data['form'] = form
    return render(request, 'criar_cidade.html', data)

def update_Cidade(request, pk):
    data = {}
    cidade = Cidades.objects.get(pk=pk)
    form = CidadeForm(request.POST or None, instance=cidade)

    if form.is_valid():
        form.save()
        return redirect('url_listar_cidades')
    data['form'] = form
    return render(request, 'criar_cidade.html', data)

def delete_Cidade(request, pk):
    cidade = Cidades.objects.get(pk=pk)
    cidade.delete()
    return redirect('url_listar_cidades')