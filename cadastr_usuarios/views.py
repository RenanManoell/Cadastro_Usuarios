from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    #Salva os dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    #exibe os dados
    usuarios = {
        'usuarios' : Usuario.objects.all()
    }

    #returna os dados para a pagina
    return render(request,'usuarios/usuarios.html', usuarios)