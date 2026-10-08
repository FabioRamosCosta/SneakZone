from django.shortcuts import render
from django.shortcuts import get_object_or_404
from produtos.models import Produto
from django.shortcuts import redirect



def carrinho(request):

    carrinho = request.session.get(
        "carrinho",
        {}
    )

    produtos = []
    total = 0

    for id_produto, quantidade in carrinho.items():
        # verifica se o produto ainda existe no banco de dados
        produto = get_object_or_404(
            Produto,
            id=id_produto
        )
        subtotal = produto.preco * quantidade
        total += subtotal
        # adiciona o produto à lista de produtos do carrinho
        produtos.append({
            "produto": produto,
            "quantidade": quantidade,
            "subtotal": subtotal
        })


    return render(
        request,
        "pedidos/carrinho.html",
        {
            "produtos": produtos,
            "total": total
        }
    )

def adicionar_carrinho(request, id):

    produto = get_object_or_404(
        Produto,
        id=id
    )

    carrinho = request.session.get(
        "carrinho",
        {}
    )

    id_produto = str(produto.id)

    if id_produto in carrinho:

        carrinho[id_produto] += 1

    else:

        carrinho[id_produto] = 1

    request.session["carrinho"] = carrinho

    return redirect("carrinho")

def remover_carrinho(request, id):
    produto = get_object_or_404(
        Produto,
        id=id
    )

    carrinho = request.session.get(
        "carrinho",
        {}
    )

    id_produto = str(produto.id)

    if id_produto in carrinho:

        carrinho[id_produto] -= 1
        if carrinho[id_produto] <= 0:
            del carrinho[id_produto]


    request.session["carrinho"] = carrinho

    return redirect("carrinho")

def excluir_carrinho(request, id):
    produto = get_object_or_404(
        Produto,
        id=id
    )

    carrinho = request.session.get(
        "carrinho",
        {}
    )

    id_produto = str(id)

    if id_produto in carrinho:

        del carrinho[id_produto]

    request.session["carrinho"] = carrinho

    return redirect("carrinho")

def contador_carrinho(request):
    carrinho = request.session.get(
        "carrinho",
        {}
    )
    quantidade = sum(carrinho.values())
    return {"total_itens": quantidade}
