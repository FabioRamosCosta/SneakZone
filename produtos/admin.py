from django.contrib import admin

from .models import Produto


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