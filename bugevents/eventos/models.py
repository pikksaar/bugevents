from django.db import models
from django.utils import timezone

class Ambiente(models.Model):
    nombre = models.CharField(max_length=80)
    ubicacion = models.CharField(max_length=80)
    aforo = models.PositiveIntegerField(default=40)

    def __str__(self):
        return f"{self.nombre}: Sala {self.ubicacion} con un aforo de {self.aforo} personas."

class Evento(models.Model):
    nombre = models.CharField(max_length=80)
    ubicacion = models.CharField(max_length=80)
    fecha_inicio = models.DateField(default=timezone.now)
    fecha_fin = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Evento {self.nombre} con lugar en {self.ubicacion}."

class Actividad(models.Model):
    nombre = models.CharField(max_length=80)
    tipo = models.CharField(max_length=30)
    evento = models.ForeignKey(Evento,  on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Actividades"

    def __str__(self):
        return f"{self.tipo}: {self.nombre}."

class Ponente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    class Meta:
        ordering = ['apellido']

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Turno(models.Model):
    nombre = models.CharField(max_length=10)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    ponentes = models.ManyToManyField(Ponente)

    def __str__(self):
        return f"{self.nombre}"