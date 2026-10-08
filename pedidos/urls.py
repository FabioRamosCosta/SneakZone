from django.urls import path

from . import views


urlpatterns = [
    path("carrinho/", views.carrinho, name="carrinho"),
    path("carrinho/adicionar/<int:id>/", views.adicionar_carrinho, name="adicionar_carrinho"),
    path("carrinho/remover/<int:id>/", views.remover_carrinho, name="remover_carrinho"),
    path("excluir   _carrinho/<int:id>/", views.excluir_carrinho, name="excluir_carrinho"),
]