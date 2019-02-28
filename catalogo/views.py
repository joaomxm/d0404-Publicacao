from django.shortcuts import render
from catalogo.models import Filme
from catalogo.forms import Adicionar_filme
# Create your views here.

def catalogo_view(request):

    filmes= Filme.objects.all()

    contexto ={
        'filmes': filmes

    }
    return render(request,'catalogo.html', contexto)


def adicionar_filmes(request):
    add= Adicionar_filme(request.POST or None)

    if add.is_valid():
        add.save()
        add=Adicionar_filme()

    context={

        'form': add
        }
        
    return render(request,'filmes.html',context)