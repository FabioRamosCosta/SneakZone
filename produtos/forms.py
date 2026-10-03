from django import forms
from .models import Produto, Categoria

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'nome', 
            'descricao', 
            'preco', 
            'categoria', 
            'estoque', 
            'imagem'
                ]
