from django.shortcuts import render


PRODUTOS =[
    {
        "id": 1,
        "nome": "Air Run",
        "preco": 299.90,
        "descricao": "Tênis confortável para corrida.",
        "categoria": "Corrida",
        "estoque": 10,
        "imagem": "core/images/Tenis_abobora.jpeg"
    },
    {
        "id": 2,
        "nome": "Street Max",
        "preco": 399.90,
        "descricao": "Tênis urbano para o dia a dia.",
        "categoria": "Streetwear",
        "estoque": 5,
        "imagem": "core/images/Tenis_azul.jpeg"
    },
    {
        "id": 3,
        "nome": "Runner Pro",
        "preco": 499.90,
        "descricao": "Tênis profissional.",
        "categoria": "Corrida",
        "estoque": 0,
        "imagem": "core/images/Tenis_verde.jpeg"

    },
]


def produtos(request):
    contexto = {
        "produtos": PRODUTOS
    }
    return render(request, "core/produtos.html", contexto)
# Create your views here.
def produto_detalhe(request, id):
    produto = None
    
    for item in PRODUTOS :
        if item["id"] == id:
            produto = item
            break
    return render(request, "core/produto_detalhe.html",{"produto": produto})
