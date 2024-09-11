from django.shortcuts import get_object_or_404,render,redirect
from django.views.generic import View
from .models import *
from django.core.paginator import Paginator
from .utils import get_rating

#Esta es la Vista inicial
class Catalogo(View): 
    def get(self,request,*args,**kwargs):
        lista = JUEGOS.objects.all().order_by('NOMBRE')
        anuales = JUEGOS.objects.filter(FECHA__icontains='2021').order_by('NOMBRE')
        paginacion = Paginator(lista.order_by('NOMBRE'),15)
        
        page_number = request.GET.get('page')
        page_obj = paginacion.get_page(page_number)
        context={
            'anuales':anuales,
            'lista':lista,
            'page_obj':page_obj,
            'page_number': page_number,
        }
        return render(request,'catalogo.html',context)


class JuegoDetailView(View):
    def get(self,request,*args,**kwargs):
        nombre = request.GET.get('content')
        page = request.GET.get('page')
        query = request.GET.get('query','')
        categ = request.GET.get('categ','')
        modo = request.GET.get('modo','')
        if page == None:
            page = 1
        juego = JUEGOS.objects.filter(NOMBRE__icontains=nombre)
        juego = juego[0]
        juego.actualizar_rating()
        premios = juego.PREMIOS.split('.')
        context ={
            'page':page,
            'premios': premios,
            'juego':juego,
            'query': query,
            'categ': categ,
            'modo': modo
        }
        return render(request,'preview.html',context)

class BusquedaView(View):
    def get(self,request):
        if request.method == 'GET':
            juegos =[]
            query = request.GET.get('query','')
            categ = request.GET.get('categ','')
            modo = request.GET.get('modo','')
            if not modo and not categ :
                juegos = JUEGOS.objects.filter(NOMBRE__icontains=query).order_by('NOMBRE')
            else:
                if not modo:
                    juegos = JUEGOS.objects.filter(GENERO__icontains=categ).order_by('NOMBRE')
                else:
                    if modo == 'single':
                        res = JUEGOS.objects.filter(GENERO__icontains=categ).order_by('NOMBRE')
                        juegos = res.filter(CANT_JUGADORES__icontains='1').order_by('NOMBRE')
                    else:
                        res = JUEGOS.objects.filter(GENERO__icontains=categ).order_by('NOMBRE')
                        for juego in res:
                            if juego.CANT_JUGADORES >= '2':
                                juegos.append(juego)

            paginacion = Paginator(juegos,15)
            page_number = request.GET.get('page')
            page_obj = paginacion.get_page(page_number)
            context={
                'query': query,
                'categ': categ,
                'modo': modo,
                'page_obj':page_obj,
                'page_number': page_number,
            }
        return render(request,'busqueda.html',context)