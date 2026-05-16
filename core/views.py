from django.shortcuts import render
from .models import persona
from portafolio.models import Portafolio

def home(request):
    person = persona.objects.first()
    return render(request, template_name='core/home.html', context={'person': person})

def about(request):
    person = persona.objects.first()
    return render(request, template_name='core/about.html', context={'person': person})

def portafolio(request):
    person = persona.objects.first()
    proyectos = Portafolio.objects.all()
    return render(request, template_name='core/portafolio.html', context={'proyectos': proyectos, 'person': person})

def contacto(request):
    person = persona.objects.first()
    return render(request, template_name='core/contacto.html', context={'person': person})