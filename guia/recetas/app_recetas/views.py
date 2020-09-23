from django.shortcuts import render

# Create your views here.
def recetas_page_view(request):
   return render(request, 'recetas.html')