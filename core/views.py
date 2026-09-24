from urllib import request

from django.shortcuts import render

PRODUTOS = [
    {
        "id": 1,
        "name": 'Tênis Esportivo',
        "preco": 199.99,
        "descricao": 'Tênis confortável para atividades esportivas.',
        "categorias": "Esporte",
        "Estoque": 50
    },
    {
        "id": 2,
        "name": 'Runer Pro',
        "preco": 499.99,
        "descricao": 'Tênis profissional.',
        "categorias": "Corrida",
        "Estoque": 5
    },
    {
        "id": 3,
        "name": 'Tênis Casual',
        "preco": 299.99,
        "descricao": 'Tênis confortável casual.',
        "categorias": "Casual",
        "Estoque": 52
    }

 ]        


def home(request):
    content = {
        'titulo': 'Bem-vindo ao Primeiro Projeto',
        'Subtitulo': 'Aprendendo Django passo a passo',
        'nome': 'Primeiro Projeto',
        'descricao': 'Este é o meu primeiro projeto Django.',
    }

    return render(request, 'core/home.html', content)

   
def produtos(request):
    content = {
        "produtos": PRODUTOS
    }
    return render(request, 'core/produtos.html', content)

def sobre(request):
    return render(request, 'core/sobre.html')

def contato(request):
    return render(request, 'core/contato.html')

def produto_detalhe(request, id):
    produto = next((p for p in PRODUTOS if p["id"] == id), None)
    content = {
        "produto": produto
    }
    #return render(request, 'core/produto_detalhe.html', content)
    return render(request, 'core/produto_detalhe.html', {"produto": produto})
