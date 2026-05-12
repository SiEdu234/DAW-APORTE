from django.http import HttpResponse
from django.shortcuts import render
from portafolio.models import Portafolio

def home(request):
    return render(request, template_name = 'core/home.html')
def about(request):
    return render(request, template_name = 'core/about.html')
def portafolio(request):
    proyectos = Portafolio.objects.all()
    return render(request, template_name ='core/portafolio.html', context={'proyectos': proyectos})
def contacto(request):
    return render(request, template_name='core/contacto.html')
