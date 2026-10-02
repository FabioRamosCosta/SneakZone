from django.urls import path
from . import views

urlpatterns = [
    path("", views.produtos, name="produtos"),
    path("<int:id>/", views.produtos_detalhe, name="produtos_detalhe"),
    path("esgotados/", views.produtos_esgotados, name="produtos_esgotados"),
    path("categoria/<str:categoria>/", views.produtos_categoria, name="produtos_categoria"),
]