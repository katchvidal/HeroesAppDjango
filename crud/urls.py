from django.contrib import admin
from django.urls import path,include
from django.conf import settings

from crud.views import HeroesListView, HeroesCreateView, HeroesUpdateView, HeroesDeleteView

from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('', login_required(HeroesListView.as_view()), name='ListaHeroes' ),
    path('crear', login_required(HeroesCreateView.as_view()), name='CreateHeroes' ),
    path('update/<int:pk>/', login_required(HeroesUpdateView.as_view()), name='UpdateHeroes' ),
    path('delete/<int:pk>/', login_required(HeroesDeleteView.as_view()), name='DeleteHeroes' ),

]


# Django no es Capas de leer ficheros de Media
    #   Configuracion para Cargar Ficheros crendo una ruta

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)