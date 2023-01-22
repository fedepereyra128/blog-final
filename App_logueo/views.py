from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm 
from django.contrib.auth import login, authenticate
from App_logueo.forms import RegistroUsuarioForm , UserEditForm ,AvatarForm
from django.contrib.auth.decorators import login_required
from .models import Avatar, Nutricion, MiPerfil

from .forms import *

# Create your views here.


def login_request(request):
    if request.method == "POST":
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password")

            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render (request, "App_gym/inicio.html", {"mensaje":f"bienvenido {usuario}"})
            else:
                return render(request, "App_logeo/login.html", {"mensaje": "usuario o contraseña incorrecta"})
        else:
            return render (request, "App_logueo/login.html", {"mensaje": "ususario o conrtaseña incorrecta" , "form":form})


        
    else:
        form= AuthenticationForm()
    return render(request, "App_logueo/login.html", {"form":form})


    


def register(request):
    if request.method =="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
            return render(request , "App_logueo/login.html", {"mensaje": f"usuario{username} creado correctamente "})
        else:
            return render(request , "App_logueo/register.html", {"form":form, "mensaje":"Error al crear el usuario"})
    else:
        form=RegistroUsuarioForm()
        return render (request, "App_logueo/register.html", {"form":form})



def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request,"App_gym/inicio.html" ,{"mensaje": "Perfil editado correctamente"})
        else:
            return render(request,"App_logueo/editarUsuario.html",{"form":form, "nombreuduario": usuario.username, "mensaje":"Error al editar el perfil"}) 


    else:
        form=UserEditForm(instance=usuario)
        return render(request, "App_logueo/editarUsuario.html", {"form":form, "nombreusuario":usuario.username})


@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)!= 0:
                avatarViejo[0].delete()
            avatar=Avatar(user=request.user , imagen=request.FILES["imagen"])
            avatar.save()
            return render(request, "App_gym/inicio.html", {"mensaje":"Avatar agregado correctamente"})
        else:
            return render (request,"App_logueo/agregaravatar.html", {"formulario":form, "usuario": request.user} )   
    else:
        form= AvatarForm()
        return render (request, "App_logueo/agregarAvatar.html", {"formulario":form, "usuario":request.user})
        

def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len (lista)!= 0:
        imagen=lista[0].imagen.url
    else:
        imagen="/media/Avatares/avatardefecto.png"
        return imagen



def Miperfil(request):
    return render(request, "App_logueo/MiPerfil.html")

@login_required
def miperfilform(request):
    
    if request.method == "POST":
        form=MiPerfilForm(request.POST, files=request.FILES)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            descripcion=informacion["descripcion"]
            email=informacion["email"]
            imagen=request.FILES["imagen"]
            usuario=MiPerfil(nombre=nombre, descripcion=descripcion,email=email,imagen=imagen)
            usuario.save()
            return render(request,"App_gym/inicio.html")
    else:
            form=MiPerfilForm()
    return render(request, "App_logueo/miperfilform.html", {"form":form})


def leerperfil(request):
    
    usuario=MiPerfil.objects.all()
    return render(request, "App_logueo/leerperfil.html",{"usuario":usuario})

@login_required
def modificarPerfil(request):
    perfil=request.user
    if request.method == "POST":
        form=MiPerfilForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            perfil.nombre=info["nombre"]
            perfil.descripcion=info["descripcion"]
            perfil.email=info["email"]
            perfil.imagen=info["imagen"]
            
            perfil.save()
            return render(request,"App_loguee/leerperfil.html", {"mensaje":"perfil editado correctamente"})
    else:
        form=MiPerfilForm(initial={"email":perfil.email})
        return render(request, "App_logueo/modificarperfil.html",{"form":form})

def eliminarperfil(request):
    usuario=MiPerfil.objects.get()
    usuario.delete()
    usuario=MiPerfil.objects.all()
    return render(request, "App_logueo/leerperfil.html", {"usuario":usuario})