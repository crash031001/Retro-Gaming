from django.views.generic import View
from django.shortcuts import redirect,render

class HomeView(View):
    def get(self,request):
        context={

        }
        return render(request,"index.html",context)