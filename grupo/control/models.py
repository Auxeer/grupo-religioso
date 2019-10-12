from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from datetime import datetime, date

# Create your models here.
class Comunidad(models.Model):
    nombre_comunidad = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Persona(update etc)
        """
        return reverse('control:comunidad-detail', args=[str(self.id)])

    def __str__(self):
        return self.nombre_comunidad

class Persona(models.Model):
    nombre_persona = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField()

    comunidad = models.ForeignKey(Comunidad, on_delete=models.SET_NULL, null=True)
    
    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Persona(update etc)
        """
        return reverse('control:persona-detail', args=[str(self.id)])

    def __str__(self):
        return self.nombre_persona

class Actividad(models.Model):
    nombre_actividad = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    fecha = models.DateField(default=datetime.now, null=True, blank=True)
    lugar = models.CharField(max_length=200)

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Persona(update etc)
        """
        return reverse('control:actividad-detail', args=[str(self.id)])

    def __str__(self):
        return self.nombre_actividad

class Participantes_Actividad(models.Model):
    actividad = models.ForeignKey(Actividad, db_column='actividad_id', on_delete=models.SET_NULL, null=True)
    persona = models.ForeignKey(Persona, db_column='persona_id', on_delete=models.SET_NULL, null=True, verbose_name='Participantes')
