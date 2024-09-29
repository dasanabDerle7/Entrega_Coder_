from django.shortcuts import render
from AppCoderC21.models import Curso,Profesor, Estudiante
from django.http import HttpResponse
from AppCoderC21.forms import cursoFormulario,profesorFormulario
# Create your views here.


def insertaCurso(res, Nombre, Camada):
    
    nuevo_curso=Curso(nombre=Nombre, camada=Camada)
    nuevo_curso.save()
    return HttpResponse(f"""
                        <p>Curso: {nuevo_curso.nombre}  - Camada: {nuevo_curso.camada} creado exitosamente. </p>
                                              """)
    

def insertaProfesor(res, Nombre, Apellido, Email,Profesion):
    
    nuevo_profesor=Profesor(nombre=Nombre, apellido=Apellido, email=Email, profesion=Profesion)
    nuevo_profesor.save()
    return HttpResponse(f"""
                        <p>Nombre Profesor: {nuevo_profesor.nombre}  - Apellido: {nuevo_profesor.apellido} creado exitosamente. </p>
                                              """)  
    

def insertaEstudiante(res, Nombre, Apellido, Email):
    
    nuevo_estudiante=Estudiante(nombre=Nombre, apellido=Apellido, email=Email)
    nuevo_estudiante.save()
    return HttpResponse(f"""
                        <p>Nombre Estudiante: {nuevo_estudiante.nombre}  - Apellido: {nuevo_estudiante.apellido} creado exitosamente. </p>
                                              """)  


def listarCurso(req):
    lista=Curso.objects.all()
    return render(req,"listaCurso.html", {"Lista_Cursos":lista})


def listarProfesores(req):
    lista=Profesor.objects.all()
    return render(req,"profesores.html", {"Lista_Profesores":lista})


def inicio(req):
    #return HttpResponse('Vista de inicio')
    return render(req,"inicio.html",{})

def cursos(req):
    #return HttpResponse('Vista de cursos')
    return render(req,"cursos.html",{})

def profesores(req):
    #return HttpResponse('Vista de profesores')
     return render(req,"profesores.html",{})

def estudiantes(req):
    #return HttpResponse('Vista de estudiantes')
    return render(req,"estudiantes.html",{})
 
def entregables(req):
    #return HttpResponse('Vista entregable')
    return render(req,"entregables.html",{})

def formularioCurso(req):
    #print(req.method)
    #print(f'Formulario enviado correctamente.')
    #print('Metodo de envio: ',req.method)
    #print('Datos enviados',req.POST)
    
    if req.method=='POST':
        # Para validar los datos que nos ingresan debemos hacer lo siguiente
        mi_formulario=cursoFormulario(req.POST)
        
        if mi_formulario.is_valid():
            
            data=mi_formulario.cleaned_data
            
            nuevo_curso=Curso(nombre=data['curso'], camada=data['camada'])
            nuevo_curso.save()
            
            return render(req,"confirmacionFormCurso.html",{})
        else: 
            return render(req,"forumularioCurso.html",{"mi_formulario":mi_formulario})
    else: 
        mi_formulario=cursoFormulario() #Como el formulario esa vacio no le paso nada.
        return render(req,"forumularioCurso.html",{"mi_formulario":mi_formulario})
    
    
    
def formularioProfesor(req):

 if req.method=='POST':
        # Para validar los datos que nos ingresan debemos hacer lo siguiente
        mi_formulario=profesorFormulario(req.POST)
        
        if mi_formulario.is_valid():
            
            data=mi_formulario.cleaned_data
            
            nuevo_profesor=Profesor(nombre=data['nombre'], apellido=data['apellido'],email=data['email'], profesion=data['profesion'])
            nuevo_profesor.save()
            
            return render(req,"confirmacionFormProfesor.html",{"nombre":data['nombre'],"apellido":data['apellido'], "email": data['email'], "profesion": data['profesion'] })
        else: 
            return render(req,"forumularioProfesor.html",{"mi_formulario":mi_formulario})
 else: 
        mi_formulario=profesorFormulario() #Como el formulario esa vacio no le paso nada.
        return render(req,"forumularioProfesor.html",{"mi_formulario":mi_formulario})


    
def busquedaCamada(req):
    return render( req,'busquedaCamada.html')


def buscarCamada(req):
    
    num_camada=req.GET["Camada"]
    
    #curso=Curso.objects.get(camada=num_camada) #Aca tengo un solo curso, me trae un solo registro
    cursos=Curso.objects.filter(camada__icontains=num_camada) #Devuelve una lista
    return render(req, "listaCurso copy.html", {"cursos":cursos, "num_camada":num_camada})
  # return  HttpResponse(f'Estamos bucando  el curso con numero de camada {num_camada} con tipo {type(num_camada)}')






