from django.db import models
import uuid
from stdimage.models import StdImageField

# Create your models here.
def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename
class Pets(models.Model):
    MF = [('M', 'Macho'), ('F', 'Fêmea')]
    Especies = [('Cão','Cão'), ('Gato','Gato')]
    Tamanhos = [('XP','Mini'),('P','Pequeno'),('M','Médio'),('G','Grande'),('XG','Extra Grande')]
    Castracao = [('S', 'Sim'), ('N', 'Não')]
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(null=True)
    sexo = models.CharField(choices=MF, max_length=1)
    especie = models.CharField(choices=Especies, max_length=4)
    raca = models.CharField(max_length=30)
    porte = models.CharField(choices=Tamanhos, max_length=2)
    descricao = models.TextField()
    castrado = models.CharField(choices=Castracao, max_length=1)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})