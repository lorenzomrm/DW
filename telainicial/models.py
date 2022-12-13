from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pet(models.Model):
    MF = [('Macho', 'Macho'), ('Fêmea', 'Fêmea')]
    Especies = [('Cão','Cão'), ('Gato','Gato')]
    Tamanhos = [('Mini','Mini'),('Pequeno','Pequeno'),('Médio','Médio'),('Grande','Grande'),('Extra Grande','Extra Grande')]
    Castracao = [('Sim', 'Sim'), ('Não', 'Não')]
    nome = models.CharField(max_length=25, null=True)
    idade = models.PositiveIntegerField(null=True)
    sexo = models.CharField(choices=MF, max_length=5, null=True)
    especie = models.CharField(choices=Especies, max_length=4, null=True)
    raca = models.CharField(max_length=30, null=True)
    porte = models.CharField(choices=Tamanhos, max_length=12, null=True)
    descricao = models.TextField()
    castrado = models.CharField(choices=Castracao, max_length=3, null=True)
    telefone = models.CharField(max_length=11, null=True)
    email = models.EmailField(null=True, blank=True)
    bairro = models.CharField(max_length=30, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='pet', blank=True, null=True)
    
    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'ficha_pet'

class Noticia(models.Model):
    titulo = models.CharField(max_length=50, null=True)
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'noticia'