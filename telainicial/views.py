from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Pet
from django.contrib.auth import logout
# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def set_pet(request):
    nome = request.POST.get('nome')
    idade = request.POST.get('idade')
    sexo = request.POST.get('sexo')
    especie = request.POST.get('especie')
    raca = request.POST.get('raca')
    porte = request.POST.get('porte')
    descricao = request.POST.get('descricao')
    castrado = request.POST.get('castrado')
    email = request.POST.get('email')
    telefone = request.POST.get('telefone')
    bairro = request.POST.get('bairro')
    file = request.FILES.get('file')
    user = request.user
    pet_id = request.POST.get('pet_id')
    if pet_id:
        pet = Pet.objects.get(id=pet_id)
        if user == pet.user:
            pet.nome = nome
            pet.idade = idade
            pet.sexo = sexo
            pet.especie = especie
            pet.raca = raca
            pet.porte = porte
            pet.descricao = descricao
            pet.castrado = castrado
            pet.email = email
            pet.telefone = telefone
            pet.bairro = bairro
            if file:
                pet.foto = file
            pet.save()
    else:
        pet = Pet.objects.create(nome=nome, idade=idade, sexo=sexo, especie=especie, raca=raca, porte=porte, descricao=descricao, castrado=castrado, email=email, telefone=telefone, bairro=bairro,
                                user=user, foto=file)
    url = '/pet/detail/{}/'.format(pet.id)
    return redirect(url)

@login_required(login_url='/login/')
def register_pet(request):
    pet_id = request.GET.get('id')
    if pet_id:
        pet = Pet.objects.get(id=pet_id)
        if pet.user == request.user:
            return render(request, 'register-pet.html', {'pet':pet})
    return render(request, 'register-pet.html')

@login_required(login_url='/login/')
def pet_detail(request, id):
    pet = Pet.objects.get(ativo=True, id=id)
    return render(request, 'pet.html', {'pet':pet})

@login_required(login_url='/login/')
def list_all_pets(request):
    pet = Pet.objects.filter(ativo=True)
    return render(request, 'list.html', {'pet':pet})

@login_required(login_url='/login/')
def list_user_pets(request):
    pet = Pet.objects.filter(ativo=True, user=request.user)
    return render(request, 'list.html', {'pet':pet})

@login_required(login_url='/login/')
def delete_pet(request, id):
    pet = Pet.objects.get(id=id)
    if pet.user == request.user:
        pet.delete()
    return redirect('/')

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/pet/all/')
        else:
            messages.error(request, 'Usuário/Senha inválidos. Favor tentar novamente.')
    return redirect('/login/')

def sobre(request):
    return render(request, 'sobre.html')

def noticias(request):
    return render(request, 'noticias.html')