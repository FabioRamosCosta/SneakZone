from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User

from .forms import CadastroUsuarioForm


def cadastro(request):

    if request.method == "POST":

        form = CadastroUsuarioForm(request.POST)

        if form.is_valid():

            usuario = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                password=form.cleaned_data["senha"]
            )

            login(request, usuario)

            return redirect("home")

    else:

        form = CadastroUsuarioForm()

    return render(
        request,
        "usuarios/cadastro.html",
        {
            "form": form
        }
    )
