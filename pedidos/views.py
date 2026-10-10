from decimal import Decimal

from django.contrib import messages
from django.db import transaction
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from produtos.models import Produto
from .models import ItemPedido, Pedido



def carrinho(request):

    carrinho, total = obter_dados_carrinho(request)
    return render(
        request,
        "pedidos/carrinho.html",
        {
            "produtos": carrinho,
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



def obter_dados_carrinho(request):

    carrinho = request.session.get("carrinho", {})
    produtos = []
    total = Decimal("0.00")

    for id_produto, quantidade in carrinho.items():

        produto = get_object_or_404(
            Produto,
            id=id_produto
        )

        subtotal = produto.preco * quantidade
        total += subtotal

        produtos.append({
            "produto": produto,
            "quantidade": quantidade,
            "subtotal": subtotal,
        })

    return produtos, total



@login_required
@require_POST
def finalizar_pedido(request):

    carrinho = request.session.get("carrinho", {})

    if not carrinho:
        messages.warning(request, "Seu carrinho está vazio.")
        return redirect("carrinho")

    try:
        with transaction.atomic():

            produtos_pedido = []
            total = Decimal("0.00")

            # Conferir estoque e preços atuais
            for id_produto, quantidade in carrinho.items():

                produto = Produto.objects.select_for_update().get(
                    id=int(id_produto)
                )

                if quantidade <= 0 or quantidade > produto.estoque:
                    raise ValueError(
                        f"Estoque insuficiente para {produto.nome}."
                    )

                subtotal = produto.preco * quantidade
                total += subtotal

                produtos_pedido.append({
                    "produto": produto,
                    "quantidade": quantidade,
                    "preco": produto.preco,
                })

            # Criar o pedido
            pedido = Pedido.objects.create(
                usuario=request.user,
                total=total,
            )

            # Criar itens e baixar o estoque
            for item in produtos_pedido:

                ItemPedido.objects.create(
                    pedido=pedido,
                    produto=item["produto"],
                    quantidade=item["quantidade"],
                    preco_unitario=item["preco"],
                )

                item["produto"].estoque -= item["quantidade"]
                item["produto"].save(update_fields=["estoque"])

    except Produto.DoesNotExist:
        messages.error(
            request,
            "Um produto do carrinho não está mais disponível."
        )
        return redirect("carrinho")

    except ValueError as erro:
        messages.error(request, str(erro))
        return redirect("carrinho")

    request.session["carrinho"] = {}

    messages.success(
        request,
        f"Pedido #{pedido.id} realizado com sucesso!"
    )
    return redirect("pedido_sucesso", id=pedido.id)


@login_required
def pedido_sucesso(request, id):
    pedido = get_object_or_404(Pedido, id=id, usuario=request.user)
    return render(request, "pedidos/pedido_sucesso.html", {"pedido": pedido})


@login_required
def meus_pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user).order_by("-data_criacao")
    return render(request, "pedidos/meus_pedidos.html", {"pedidos": pedidos})


@login_required
def pedido_detalhe(request, id):
    pedido = get_object_or_404(
        Pedido.objects.prefetch_related("itens__produto"),
        id=id,
        usuario=request.user,
    )
    return render(request, "pedidos/pedido_detalhe.html", {"pedido": pedido})