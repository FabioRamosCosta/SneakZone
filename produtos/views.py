from django.shortcuts import render

from .models import Produto

def produtos(request):
    PRODUTOS = Produto.objects.all()
    contexto = {
        "produtos": PRODUTOS
    }
    return render(request, "produtos/produtos.html", contexto)
# Create your views here.
def produto_detalhe(request, id):
    produto = Produto.objects.get(id=id)
    return render(request, "produtos/produto_detalhe.html", {"produto": produto})
