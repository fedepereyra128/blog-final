from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm 
from django.contrib.auth import login, authenticate
from App_logueo.forms import RegistroUsuarioForm , UserEditForm ,AvatarForm
from django.contrib.auth.decorators import login_required
from .models import Avatar

# Create your views here.


def login_request(request):
    if request.method == "POST":
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password")
            usuario=authenticate(username=usu , password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request , "App_gym/inicio.html", {"mensaje":"binevenido"})
            else:
                return render(request, "App_logueo/login.html" , {"mensaje":"usuario o contraseña incorrecto", "form": form})
        else:
            return render(request, "App_logueo/login.html" , {"mensaje":"usuario o contraseña incorrecto", "form": form})
    else:
        form=AuthenticationForm()
        return render(request, "App_logueo/login.html",{"form": form})



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


@login_required
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
        imagen="/media/Avatares/avatar1.jpg"
        return imagen


        
