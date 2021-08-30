from .models import Heroe
from .form import HeroeForm

from django.shortcuts import render

#   Creando Vistas
from django.views import generic
from django.urls import reverse_lazy






#   Vistas Genericas 

class HeroesListView( generic.ListView ):
    paginate_by = 6
    model = Heroe
    template_name = '02-Crud/Read.html'


class HeroesCreateView( generic.CreateView ):
    model = Heroe
    form_class = HeroeForm
    template_name = '02-Crud/Create.html'
    success_url = reverse_lazy('ListaHeroes')


class HeroesUpdateView( generic.UpdateView ):
    model=Heroe
    form_class = HeroeForm
    template_name = '02-Crud/Create.html'
    success_url = reverse_lazy('ListaHeroes')


class HeroesDeleteView( generic.DeleteView ):
    model=Heroe
    template_name = '02-Crud/Delete.html'
    success_url = reverse_lazy('ListaHeroes')
