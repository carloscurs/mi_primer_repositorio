from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.http import HttpResponse
# Create your views here.
def home_page_view(request):
   return render(request, 'hola_mundo.html')
def about_page_view(request):
   parametros = {'numero_favorito': 77}
   return render(request, 'about.html', parametros)