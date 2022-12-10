from django.shortcuts import render, redirect
from telainicial.models import Pets
from telainicial.forms import PetsForm
from django.http import Http404
# Create your views here.
def index(request):
    dados = {}
    search = request.GET.get('search')
    if search:
        dados['db'] = Pets.objects.filter(modelo__icontains=search)
    else:
        dados['db'] = Pets.objects.all()
    pets = Pets.objects.all()
    return render(request, 'index.html', {'pets': pets})
    #return render(request, 'index.html', dados)

def form(request):
    data = {}
    data['form'] = PetsForm()
    return render(request, 'form.html', data)
def adocao(request):
    return render(request, 'adocao.html')

def pet_detial(request, id):
    try:
        pet = Pets.objects.get(id=id)
    except Pets.DoesNotExist:
        raise Http404('pet not found')
    return render(request,'pet_detail.html', {'pet': pet})

def create(request):
    form = PetsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Pets.objects.get(pk=pk)
    return render(request, 'view.html',data)

def edit(request, pk):
    data = {}
    data['db'] = Pets.objects.get(pk=pk)
    data['form'] = PetsForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Pets.objects.get(pk=pk)
    form = PetsForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Carros.objects.get(pk=pk)
    db.delete()
    return redirect('home')