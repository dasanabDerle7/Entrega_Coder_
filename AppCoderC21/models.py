from django.db import models

# Create your models here.
from datetime import datetime

# Create your models here.
## con el comando python magane.py makemigrations creo el metodo de migracion

class Curso(models.Model):
    nombre=models.CharField(max_length=50)
    camada=models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre} - {self.camada}'
    
    class Meta():        
            ordering=('nombre',)
    
   
    
    
class Estudiante(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField (max_length=254)
    
    def __str__(self):
        return f'{self.nombre} - {self.apellido}'


class Profesor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    profesion=models.CharField(max_length=30)
    
    def __str__(self):
      return f'{self.nombre} {self.apellido} - {self.profesion}'
    
    class Meta():   
            verbose_name='Profesor'  
            verbose_name_plural='Profesores'     
    
    

class Entregable(models.Model):
    nombre=models.CharField(max_length=30)
    fechaDeEntrega=models.DateField()
    entregado=models.BooleanField()
    estudiante=models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nombre} - Fecha Entrega {self.fechaDeEntrega}'   