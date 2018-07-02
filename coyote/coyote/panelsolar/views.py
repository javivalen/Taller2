from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import Formulario
from django.core.files.storage import FileSystemStorage


#definimos las funciones que serán redirigidas a los templates. 
#Recuerden que generamos un diccionario y luego en el template debemos llamar a las llaves
def index(request):
	bienvenida={'titulo': 'Coyote','intro':'¿Has pensado cuánto dinero ahorrarías al año si implementas paneles solares?'}
	return render(request, 'panelsolar/index.html', bienvenida)

def contacto(request):
    info={'titulo':'Ups! Aún estamos trabajando en la página', 'mensaje': 'Ingresa tu teléfono y correo, te contactaremos lo antes posible'} 
    return render(request,'panelsolar/contacto.html', info)
    