from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.produtos, name="produtos"),
    path("<int:id>/", views.produtos_detalhe, name="produtos_detalhe"),
    path("esgotados/", views.produtos_esgotados, name="produtos_esgotados"),
    path("produto/novo/", views.produto_novo, name="produto_novo"),
    path("produto/<int:id>/editar/", views.produto_editar, name="produto_editar"),
    path("produto/<int:id>/excluir/", views.produto_excluir, name="produto_excluir"),
    path("categoria/<str:categoria>/", views.produtos_categoria, name="produtos_categoria"),
]