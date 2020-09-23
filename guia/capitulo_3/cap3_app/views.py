from django.shortcuts import render

# Create your views here.
def home_page_view(request):
   return render(request, 'hola_mundo.html')
