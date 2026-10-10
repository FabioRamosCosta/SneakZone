from django.contrib import admin

from .models import Pedido, ItemPedido

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 0 # número de linhas extras para adicionar (exclui linhas vazias na tabela caso exista linhas automaticas criadas)

    readonly_fields = ("preco_unitario",)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "usuario",
        "data_criacao",
        "status",
        "total"
    )

    search_fields = (
        "usuario__username",
    )

    list_filter = (
        "status",
        "data_criacao"
    )

    inlines = [ItemPedidoInline]

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = (
        "pedido",
        "produto",
        "quantidade",
        "preco_unitario"
    )

   
