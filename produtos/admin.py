from django.contrib import admin

from .models import Produto, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):

    list_display = (
        "nome",
        "categoria",
        "preco",
        "estoque",
    )

    search_fields = (
        "nome",
        "categoria",
    )

    list_filter = (
        "categoria",
    )

    ordering = (
        "nome",
    )