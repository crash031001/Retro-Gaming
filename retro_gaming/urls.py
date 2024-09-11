from django.urls import path,include
from .views import Catalogo
from .views import JuegoDetailView
from .views import BusquedaView

app_name="retro_gaming"

#Esta son las Url de la app Blog
urlpatterns =[
    path('catalogo/',Catalogo.as_view(),name='catalogo'),
    path('busqueda/', BusquedaView.as_view(),name='busqueda'),
    path('preview/',JuegoDetailView.as_view(),name='preview'),
]