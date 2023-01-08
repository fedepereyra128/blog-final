from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from App_gym.forms import *
from django.contrib.auth.decorators import login_required
from App_logueo.models import *
from App_logueo.forms import nutriForm
from App_logueo.views import obtenerAvatar
# Create your views here.
@login_required
def profesor(request):
    profesor1=Profesor(nombre="Federico" , area="musculacion" , email="fede@profe.com")
    profesor1.save()
    cadena="profe nuevo: " + profesor1.nombre + "" +profesor1.area + "" + profesor1.email
    return HttpResponse(cadena)

@login_required
def gimnasio(request):
    gym1=Gimnasio(nombre="onix" , direccion="espora 355" , email="onix@gym.com")
    gym1.save()
    cadena="gimnasio nuevo:"+ gym1.nombre +""+gym1.direccion+""+ gym1.email
    return HttpResponse(cadena)

@login_required
def inicio(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista) != 0:
        imagen=lista[0].imagen.url
    else:
        imagen=None

    return render(request, "App_gym/inicio.html", {"imagen":imagen})

def aboutme(request):
    return render(request,"App_gym/aboutme.html")


@login_required
def gimnasio(request):
    return render(request , "App_gym/gimnasio.html" )
@login_required
def profesores(request):
    return render(request,"App_gym/profesores.html")



@login_required
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


@login_required
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



@login_required
def leergim(request):
    gimnasio=Gimnasio.objects.all()
    return render(request , "App_gym/leergim.html", {"gimnasio": gimnasio})

@login_required
def leerprofesores(request):
    profe=Profesor.objects.all()
    return render(request ,"App_gym/leerprofesores.html" ,{"profe": profe} )


@login_required
def buscargimnasio(request):
    return render(request, "App_gym/buscargimnasio.html")

@login_required
def buscarprofesor(request):
    return render(request, "App_gym/buscarprofesor.html")
@login_required
def buscar(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        gimnasio=Gimnasio.objects.all()
        return render(request , "App_gym/resultadobusquedagim.html", {"gimnasio":gimnasio})

    else:
        return render(request ,"App_gym/buscargimnasio.html", {"mensaje":"gimnasio no encontrado"})

@login_required
def buscar1(request):
    if request.GET["area"]:
        area=request.GET["area"]
        profesor=Profesor.objects.all()
        return render(request , "App_gym/resultadobusquedaprofesor.html", {"profesor":profesor})

    else:
        return render(request ,"App_gym/buscarprofesor.html", {"mensaje":"profesor no encontrado"})

@login_required
def eliminarProfesor(request, id):
    profe=Profesor.objects.get(id=id)
    profe.delete()
    profe=Profesor.objects.all()
    return render( request ,"App_gym/leerprofesores.html", {"profe":profe})

@login_required
def eliminarGim(request, id):
    gim=Gimnasio.objects.get(id=id)
    gim.delete()
    gim=Gimnasio.objects.all()
    return render(request, "App_gym/leergim.html", {"gim":gim})


@login_required
def editarProfesor(request,id):
    profesor=Profesor.objects.get(id=id)
    if request.method=="POST":
        form=ProfesorForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            profesor.nombre=informacion["nombre"]
            profesor.area=informacion["area"]
            profesor.email=informacion["email"]
            profesor.save()
            profesor=Profesor.objects.all()
            return render(request,"App_gym/leerprofesores.html", {"mensaje":"Profesor editado correctamente"})
    else:
            formu=ProfesorForm (initial={"nombre":profesor.nombre , "area":profesor.area , "email": profesor.email})
       

    return render (request ,"App_gym/editarProfesor.html", {"form":formu , "profesor":profesor})

@login_required
def editarGimnasio(request,id):
    gimnasio=Gimnasio.objects.get(id=id)
    if request.method=="POST":
        form=GimnasioForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            gimnasio.nombre=informacion["nombre"]
            gimnasio.direccion=informacion["direccion"]
            gimnasio.email=informacion["email"]
            gimnasio.save()
            gimnasio=Gimnasio.objects.all()
            return render(request,"App_gym/leergim.html", {"mensaje":"Gimnasio editado correctamente"})
    else:
        formu=GimnasioForm (initial={"nombre":gimnasio.nombre , "direccion":gimnasio.direccion , "email": gimnasio.email})
       

    return render (request ,"App_gym/editargimnasio.html", {"form":formu , "gimnasio":gimnasio})


@login_required
def nutricion(request):
    return render(request,"App_gym/nutricion.html")

@login_required
def nutriform(request):
    if request.method=="POST":
        form=nutriForm(request.POST , files=request.FILES)
        if form.is_valid():
            informacion=form.cleaned_data
            autor=informacion["autor"]
            fecha=informacion["fecha"]
            titulo=informacion["titulo"]
            imagen=imagen=request.FILES["imagen"]
            cuerpo=informacion["cuerpo"]
            nutri1=Nutricion(autor=autor, fecha=fecha,titulo=titulo,imagen=imagen,cuerpo=cuerpo)
            nutri1.save()
            return render(request,"App_gym/inicio.html")
    else:
            form=nutriForm()
    return render(request, "App_gym/nutriform.html", {"form":form})



@login_required
def leernutricion(request):
    nutricion=Nutricion.objects.all()
    return render(request ,"App_gym/leerdieta.html" ,{"nutricion": nutricion} )



@login_required
def eliminarnutri(request, id):
    nutri=Nutricion.objects.get(id=id)
    nutri.delete()
    nutri=Nutricion.objects.all()
    return render(request, "App_gym/nutricion.html", {"nutri":nutri})
