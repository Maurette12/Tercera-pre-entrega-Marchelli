from django.db import models

class Futbolista(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    posicion = models.CharField(max_length=256)
    altura = models.IntegerField(null=True)


class Socio(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField(blank=True)
    socio_n = models.IntegerField(null=True) 


class Autoridad(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    cargo = models.CharField(max_length=256)