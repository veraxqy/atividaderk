import django_filters
from .models import Cidades, Bairros, Usuarios, Funcionarios, Generos, Est_Fisico, Livros, Emprestimos

class CidadesFilter(django_filters.FilterSet):

    class Meta: 
        model = Cidades
        fields = {'id_cidade' : ['exact'], 'nome_cidade' : ['icontains']}

class BairrosFilter(django_filters.FilterSet):

    class Meta: 
        model = Bairros
        fields = {'id_bairro' : ['exact'], 'nome_bairro' : ['icontains'], 'id_cidade_bairro' : ['exact']}

class UsuariosFilter(django_filters.FilterSet):

    class Meta: 
        model = Usuarios
        fields = {'id_usuario' : ['exact'], 'nome_usuario' : ['icontains'], 'dta_nasc_usuario' : ['icontains'], 'email_usuario' : ['icontains'], 'numero_usuario' : ['icontains'], 'logradouro_usuario' : ['icontains'], 'id_bairro_usuario' : ['exact']}

class FuncionariosFilter(django_filters.FilterSet):

    class Meta: 
        model = Funcionarios
        fields = {'id_funcionario' : ['exact'], 'nome_funcionario' : ['icontains'], 'dta_nasc_funcionario' : ['icontains'], 'telefone_funcionario' : ['icontains'], 'email_funcionario' : ['icontains'], 'numero_funcionario' : ['icontains'], 'logradouro_funcionario' : ['icontains'], 'id_bairro_funcionario' : ['exact']}

class GenerosFilter(django_filters.FilterSet):

    class Meta: 
        model = Generos
        fields = {'id_genero' : ['exact'], 'nome_genero' : ['icontains']}

class Est_FisicoFilter(django_filters.FilterSet):

    class Meta: 
        model = Est_Fisico
        fields = {'id_est_fisico' : ['exact'], 'est_fisico' : ['icontains']}

class LivrosFilter(django_filters.FilterSet):

    class Meta: 
        model = Livros
        fields = {'id_livro' : ['exact'], 'titulo_livro' : ['icontains'], 'editora_livro' : ['icontains'], 'autor_livro' : ['icontains'], 'dta_publicacao_livro' : ['icontains'], 'qtd_paginas_livro' : ['icontains'], 'id_genero_livro' : ['exact'], 'id_est_fisico_livro' : ['exact']}

class EmprestimosFilter(django_filters.FilterSet):

    class Meta: 
        model = Emprestimos
        fields = {'id_emprestimos' : ['exact'], 'dta_emprestimo' : ['icontains'], 'dta_devolucao' : ['icontains'],'id_usuario_emprestimos' : ['exact'], 'id_funcionario_emprestimos' : ['exact'], 'id_livro_emprestimos' : ['exact']}