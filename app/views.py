from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request,'home.html')

#Formulário de cadastro de usuarios
def create(request):
    return render(request,'create.html')

#Inserção dos dados dos usuarios no banco
def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request,'create.html',data)
