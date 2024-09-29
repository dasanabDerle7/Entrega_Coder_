"""
URL configuration for Proyecto5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from AppCoderC21.views import * ## puedo traer de a uno, o todos -- insertaCurso, listarCurso,profesores,estudiantes,cursos,entregables, inicio

urlpatterns = [
    path('', inicio,name="inicio"), 
    path('insertaCurso/<Nombre>/<Camada>', insertaCurso,name="insertaCurso"),
    path('insertaProfesor/<Nombre>/<Apellido>/<Email>/<Profesion>', insertaProfesor,name="insertaProfesor"),
    path('insertaEstudiante/<Nombre>/<Apellido>/<Email>', insertaEstudiante,name="insertaEstudiante"),
    path('profesores/', listarProfesores ,name="profesores"), 
    path('estudiantes/', estudiantes,name="estudiantes"),  
    path('cursos/', listarCurso,name="listaCursos"),
    path('entregable/', entregables,name="entregable"), 
    path('formularioCurso/', formularioCurso,name="formularioCurso"), 
    path('formularioProfesor/', formularioProfesor,name="formularioProfesor"), 
    path('busquedaCamada/', busquedaCamada,name="busquedaCamanda"), 
    path('buscarCamada/', buscarCamada,name="buscarCamada"),
    
    
]
