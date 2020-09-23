from django.shortcuts import render

# Create your views here.
def recetas_page_view(request):
   return render(request, 'recetas.html')
def canelones_page_view(request):
   return render(request, 'Canelones/index.html')
def carbonara_page_view(request):
   return render(request, 'carbonara/index.html')
def Receta_Facil_page_view(request):
   return render(request, 'Receta_Facil/index.html')