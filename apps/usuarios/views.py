from django.shortcuts import render, redirect
from apps.usuarios.forms import UsuarioForms, CadastroForm

from django.contrib.auth.models import User

from django.contrib import auth

from django.contrib import messages

def login (request):
    form = UsuarioForms()

    if request.method == 'POST':
        form = UsuarioForms(request.POST)


        if form.is_valid():

            nome = form['nome_login'].value()
            senha = form['senha'].value()


        usuario = auth.authenticate(
            request,
            username= nome,
            password= senha


        )

        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f"{usuario} logado com sucesso")
            return redirect('index')

        else:
            messages.error(request, "Erro ao efetuar login")
            return redirect('login')




    return render(request, "usuarios/login.html", {"form":form})
def cadastro(request):
    form = CadastroForm()

    if request.method == 'POST':
        form = CadastroForm (request.POST)
        if form.is_valid():




            nome = form["nome_cadastro"].value()
            email = form["email"].value()
            senha = form['senha_1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, "O nome de usuário já foi cadastrado")
                return redirect('cadastro')


            usuario = User.objects.create_user(
            username=nome,
            email=email,
            password=senha


            )

            usuario.save()
            messages.success(request, "Cadastro efetuado com sucesso")
            return redirect("login")


    return render(request, "usuarios/cadastro.html", {"form":form})


def logout(request):
    auth.logout(request)
    messages.success(request,"Logout efetuado com sucesso")
    return redirect('login')
