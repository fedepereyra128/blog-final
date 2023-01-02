from django.urls import path
from App_gym.views import *

urlpatterns=[
    path("profesor/", profesor , name="profesor"),
    path("gimnasio/", gimnasio, name="gimnasio"),
    path("gimnasioform/",gimnasioform ,name="gimnasioform"),
    path("profeform/", profeform, name="profeform"),
    path("",inicio, name="inicio"),
    path("leergim/", leergim , name="leergim"),
    path("leerprofesores/", leerprofesores , name="leerprofesores"),
    path("buscar/", buscar , name="buscar"),
    path("buscargimnasio/", buscargimnasio, name="buscargimnasio"),
    path("buscarprofesor/", buscarprofesor , name="buscarprofesor"),
    path("buscar1/", buscar1 , name="buscar1"),
    path("profesores/", profesores , name="profesores"),
    path("eliminarProfesor/<id>", eliminarProfesor , name="eliminarProfesor"),
    path("eliminarGim/<id>", eliminarGim, name="eliminarGim"),
    path("editarProfesor/<id>", editarProfesor , name="editarProfesor"),
    path("editargimnasio/<id>", editarGimnasio , name="editargimnasio"),
    path("nutricion/", nutricion , name="nutricion"),
    path("nutriform/", nutriform , name="nutriform"),
    path("leernutricion/", leernutricion, name="leernutricion"),
    path("eliminarnutri/<id>", eliminarnutri , name="eliminarnutri"),





]