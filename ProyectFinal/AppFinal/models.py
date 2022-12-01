from django.db import models

class Personal(models.Model):
    nombres=models.CharField(max_length=40)
    apellidos=models.CharField(max_length=40)
    edad=models.IntegerField()
    nacionalidad=models.CharField(max_length=40)

class Estudios(models.Model):
    carrera=models.CharField(max_length=100)
    universidad=models.CharField(max_length=100)
    idiomas=models.CharField(max_length=40)

class Experiencia(models.Model):
    trabajos_anteriores=models.CharField(max_length=1000)
    años_experiencia=models.IntegerField()
    

