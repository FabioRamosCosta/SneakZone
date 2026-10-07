from django.shortcuts import render

from produtos.models import Categoria, Produto

from django.contrib.auth.decorators import login_required





def home(request):
    categorias = Categoria.objects.all()
    produtos = Produto.objects.select_related('categoria').all()
    contexto = {
        "titulo": "Os melhores tênis para o seu estilo",
        "subtitulo": "Encontre seu próximo par.",
        "categorias": categorias,
        "produtos": produtos
    }
    return render(request, "core/home.html", contexto)



def sobre(request):
    return render(request, "core/sobre.html")

def contato(request):
    return render(request, "core/contato.html")

@login_required
def perfil(request):

    return render(
        request,
        "usuarios/perfil.html"
    )

