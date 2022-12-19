from django.db import models

# Create your models here.

class Cidades(models.Model):
    id_cidade = models.AutoField(primary_key=True)
    nome_cidade = models.CharField(max_length=126)
    class Meta:
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return self.nome_cidade