from django.forms import ModelForm
from telainicial.models import Pets

class PetsForm(ModelForm):
     class Meta:
         model = Pets
         fields = ['nome', 'idade', 'sexo','especie','raca','porte','descricao','castrado','imagem']