from django.shortcuts import render
from telainicial.models import Pets
from telainicial.forms import PetsForm
# Create your views here.
def index(request):
    dados = {}
    search = request.GET.get('search')
    if search:
        dados['db'] = Pets.objects.filter(modelo__icontains=search)
    else:
        dados['db'] = Pets.objects.all()
    return render(request, 'index.html')

def form(request):
    data = {}
    data['form'] = PetsForm()
    return render(request, 'form.html', data)
def adocao(request):
    return render(request, 'adocao.html')