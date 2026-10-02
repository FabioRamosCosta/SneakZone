from django.shortcuts import render

from .models import Produto, Categoria

def produtos(request):
    PRODUTOS = Produto.objects.all()
    contexto = {
        "produtos": PRODUTOS
    }
    return render(request, "produtos/produtos.html", contexto)
# Create your views here.
def produtos_detalhe(request, id):
    produto = Produto.objects.get(id=id)
    return render(request, "produtos/produto_detalhe.html", {"produto": produto})


def produtos_esgotados(request):
    produtos = Produto.objects.filter(estoque=0)
    return render(request, "produtos/produtos.html", {"produtos": produtos})

def produtos_categoria(request, categoria):
    
    produtos = Produto.objects.filter(categoria= Categoria.objects.get(nome=categoria))
    return render(request, "produtos/produtos.html", {"produtos": produtos, "titulo": f"Produtos da categoria {Categoria.objects.get(nome=categoria).nome}"})