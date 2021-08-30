from django.shortcuts import render
from django.views import generic
from crud.models import Heroe
# Create your views here.

class MarvelList( generic.ListView ):
    paginate_by = 6
    model = Heroe
    queryset = Heroe.objects.filter( Publisher= 'Marvel')
    template_name = '04-Filtro/filtrados.html'


class DCList( generic.ListView ):
    paginate_by = 6
    model = Heroe
    queryset = Heroe.objects.filter( Publisher= 'DC')
    template_name = '04-Filtro/filtrados.html'