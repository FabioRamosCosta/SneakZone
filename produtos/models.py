from django.db import models


class Categoria(models.Model):

    nome = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.nome


class Produto(models.Model):

    nome = models.CharField(
        max_length=100
    )

    descricao = models.TextField()

    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT
    )

    estoque = models.PositiveIntegerField(
        default=0
    )

    imagem = models.CharField(
        max_length=255,
        blank=True
    )

    data_cadastro = models.DateTimeField(
        auto_now_add=True
    )