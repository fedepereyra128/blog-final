from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from App_gym.forms import *

# Create your views here.
def profesor(request):
    profesor1=Profesor(nombre="Federico" , area="musculacion" , email="fede@profe.com")
    profesor1.save()
    cadena="profe nuevo: "+ profesor1.nombre + "especializado en " +profesor1.area + "contactalo al" + profesor1.email
    return HttpResponse(cadena)


def gimnasio(request):
    gym1=Gimnasio(nombre="onix" , direccion="espora 355" , email="onix@gym.com")
    gym1.save()
    cadena="gimnasio nuevo:"+ gym1.nombre +""+gym1.direccion+""+ gym1.email
    return HttpResponse(cadena)


def inicio(request):
    return render(request, "App_gym/inicio.html")

def gimnasio(request):
    return render(request , "App_gym/gimnasio.html")

def profesores(request):
    return render(request,"App_gym/profesores.html")




def gimnasioform(request):
    if request.method=="POST":
        form=GimnasioForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data

            nombre1=informacion["nombre"] 
            direccion1=informacion["direccion"]
            email1=informacion["email"]
            gimnasio1=Gimnasio(nombre=nombre1 ,direccion=str(direccion1) , email=email1)
            gimnasio1.save()
            return render(request, "App_gym/inicio.html")

    else:
            formulario=GimnasioForm()
    return render(request, "App_gym/gimnasioform.html", {"form":formulario})



def profeform(request):
    if request.method=="POST":
        form=ProfesorForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data

            nombre1=informacion["nombre"] 
            area=informacion["area"]
            email1=informacion["email"]
            profe1=Profesor(nombre=nombre1 ,area=area , email=email1)
            profe1.save()
            return render(request, "App_gym/inicio.html")

    else:
            formulario=ProfesorForm()
    return render(request, "App_gym/profeform.html", {"form":formulario})




def leergim(request):
    gimnasio=Gimnasio.objects.all()
    return render(request , "App_gym/leergim.html", {"gimnasio": gimnasio})


def leerprofesores(request):
    profe=Profesor.objects.all()
    return render(request ,"App_gym/leerprofesores.html" ,{"profe": profe} )



def buscargimnasio(request):
    return render(request, "App_gym/buscargimnasio.html")


def buscarprofesor(request):
    return render(request, "App_gym/buscarprofesor.html")

def buscar(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        gimnasio=Gimnasio.objects.all()
        return render(request , "App_gym/resultadobusquedagim.html", {"gimnasio":gimnasio})

    else:
        return render(request ,"App_gym/buscargimnasio.html", {"mensaje":"gimnasio no encontrado"})


def buscar1(request):
    if request.GET["area"]:
        area=request.GET["area"]
        profesor=Profesor.objects.all()
        return render(request , "App_gym/resultadobusquedaprofesor.html", {"profesor":profesor})

    else:
        return render(request ,"App_gym/buscarprofesor.html", {"mensaje":"profesor no encontrado"})


def eliminarProfesor(request, id):
    profe=Profesor.objects.get(id=id)
    profe.delete()
    profe=Profesor.objects.all()
    return render( request ,"App_gym/leerprofesores.html", {"profe":profe})


def eliminarGim(request, id):
    gim=Gimnasio.objects.get(id=id)
    gim.delete()
    gim=Gimnasio.objects.all()
    return render(request, "App_gym/leergim.html", {"gim":gim})



def editarProfesor(request,id):
    profesor=Profesor.objects.get(id=id)
    if request.method=="POST":
        form=profeform(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            profesor.nombre=informacion["nombre"]
            profesor.area=informacion["area"]
            profesor.email=informacion["emal"]
            return render(request,"App_gym/leerprofesores.html", {"mensaje":"profesor editado correctamente"})
    else:
        formulario= profeform(initial={"nombre":profesor.nombre , "area":profesor.area , "email": profesor.email})
    return render (request ,"App_gym/editarProfesor.html", {"form":formulario , "profesor":profesor})
                




