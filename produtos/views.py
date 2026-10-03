from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Categoria



from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProdutoForm

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

@login_required # Fez o efeito de proteger a view, para que apenas usuários logados possam acessar.
def produto_novo(request):

    if request.method == "POST":

        form = ProdutoForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Produto cadastrado com sucesso!"
            )

            return redirect("produtos")

    else:

        form = ProdutoForm()

    return render(
        request,
        "produtos/produto_form.html",
        {
            "form": form
        }
    )

@login_required # Fez o efeito de proteger a view, para que apenas usuários logados possam acessar.
def produto_editar(request, id):

    produto = get_object_or_404(
        Produto,
        id=id
    )

    if request.method == "POST":

        form = ProdutoForm(
            request.POST,
            instance=produto
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Produto atualizado com sucesso!"
            )

            return redirect(
                "produto_detalhe",
                id=produto.id
            )

    else:

        form = ProdutoForm(
            instance=produto
        )

    return render(
        request,
        "produtos/produto_form.html",
        {
            "form": form,
            "titulo": "Editar produto",
            "botao": "Salvar alterações"
        }
    )

@login_required
def produto_excluir(request, id):

    produto = get_object_or_404(
        Produto,
        id=id
    )

    if request.method == "POST":

        produto.delete()

        messages.success(
            request,
            "Produto excluído com sucesso!"
        )

        return redirect("produtos")

    return render(
        request,
        "produtos/produto_confirmar_exclusao.html",
        {
            "produto": produto
        }
    )