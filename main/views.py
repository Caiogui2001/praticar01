from django.shortcuts import render, get_object_or_404, redirect
from .models import Cadastro

# Listar todos os cadastros
def cadastro_list(request):
    cadastros = Cadastro.objects.all()
    return render(request, 'cadastro/cadastro_list.html', {'cadastros': cadastros})


# Criar um novo cadastro (simplificado, sem formulário)
def criar_cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        data_nascimento = request.POST['data_nascimento']
        
        Cadastro.objects.create(nome=nome, cpf=cpf, data_nascimento=data_nascimento)
        return redirect('cadastro_list')
    return render(request, 'cadastro/criar_cadastro.html')
