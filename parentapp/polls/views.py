from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template, loader
from .models import familiar
from django.forms.models import model_to_dict


# Create your views here.
def index(request):
    parent = familiar(nombre='Francisco Nuñez Hernandez', edad= 37, nacimiento= '1985-02-19')
    parent.save()

    diccionario = model_to_dict(parent)
   
    plantilla = loader.get_template('template_uno.html')
    documento = plantilla.render(diccionario)
    
    # texto = f"Nombre: {parent_one.nombre} | Edad {parent_one.edad} | Fecha Nacimiento {parent_one.nacimiento}"
    return HttpResponse(documento)


'''# Create your views here.
def index(request):
    parent_one = familiar(nombre='Francisco Nuñez Hernandez', edad= 37, nacimiento= '1985-02-19')
    parent_two = familiar(nombre='Francisco Nuñez Alcala', edad= 3, nacimiento= '2019-08-02')
    parent_three = familiar(nombre='Fernanda Nuñez Alcala', edad= 11, nacimiento= '2011-05-03')

    parent_one.save()
    parent_two.save()
    parent_three.save()

    diccionario = {}
    texto = f"Nombre: {parent_one.nombre} | Edad {parent_one.edad} | Fecha Nacimiento {parent_one.nacimiento}"
    return HttpResponse(texto)
    
    
'''
