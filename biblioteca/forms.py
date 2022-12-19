from dataclasses import field, fields
from django.forms import ModelForm
from .models import Cidades



class CidadeForm(ModelForm):
    class Meta:
        model = Cidades
        fields = ['id_cidade', 'nome_cidade']