from django.shortcuts import render

from django.http import HttpResponse, Http404
from datetime import datetime

#Formuários
from .forms import CidadeForm
from .forms import EnderecoForm
from .forms import ClienteForm

# Create your views here.


def index(request):
    return render(request, "cliente/index.html", {})

def hora(request):

    context = {"hora":datetime.now()}
    return render(request, "cliente/hora.html", context)

def dados(request):
    nome = "Ingridi"
    dtNascimento = "08/05/1993"
    dog = "Penny"
    cidade = "Curitiba"
    cpf = "10"
    rg = "12"

    context = {
        "nome":nome,
        "dtNascimento":dtNascimento,
        "dog":dog,
        "cidade":cidade,
        "cpf":cpf,
        "rg":rg,
    }
    return render(request, "cliente/dados.html", context)

def cidadeView(request):

    form = CidadeForm()

    context = {"form":form}

    return render(request, "cliente/cidade.html", context)

def enderecoView(request):

    form = EnderecoForm()

    context = {"form":form}

    return render(request, "cliente/endereco.html", context)    

def clienteView(request):

    form = ClienteForm()

    context = {"form":form}

    return render(request, "cliente/cliente.html", context)      

def cadastra(request):
    pass      