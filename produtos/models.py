from django.db import models

# Create your models here.
class Produto(models.Model):

    nome = models.CharField(
        max_length=100
    )

    descricao = models.TextField()

    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    categoria = models.CharField(
        max_length=50
    )

    estoque = models.PositiveIntegerField(
        default=0
    )

    imagem = models.CharField(
        max_length=255,
        blank=True
    )

    def __str__(self):
        return self.nome