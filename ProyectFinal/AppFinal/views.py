from django.shortcuts import render
from django.http import HttpResponse
from AppFinal.models import *
from django.core import serializers
from AppFinal.forms import *

def inicio(request):
    return render(request,'AppFinal/padre.html')

def busquedaEdad(request):
    return render(request,'AppFinal/busquedaEdad.html')

def edad(request):
    edad_views = request.GET["edad"]
    personal_todos=Personal.objects.filter(edad=edad_views)
    return render(request,"AppFinal/resultadoEdad.html",{"edad":edad_views,"personal":personal_todos})

def busquedaAños(request):
    return render(request,'AppFinal/busquedaAños.html')

def años(request):
    años_views = request.GET["años"]
    experiencia_todos=Experiencia.objects.filter(años_experiencia=años_views)
    return render(request,"AppFinal/resultadoAños.html",{"años":años_views,"experiencia":experiencia_todos})

def personal(request):
    if request.method == "POST":
        miPersonal = PersonalForm(request.POST)
        print(miPersonal)
        
        if miPersonal.is_valid:
            informacion1 = miPersonal.cleaned_data
            personal = Personal(
                nombres=informacion1["nombres"], 
                apellidos=informacion1["apellidos"], 
                edad=informacion1["edad"],
                nacionalidad=informacion1["nacionalidad"])
            personal.save()
            return render(request, "AppFinal/padre.html")
        
    else:
        miPersonal=PersonalForm()
    return render(request, "AppFinal/personal.html", {"miPersonal": miPersonal})

def estudios(request):
    if request.method == "POST":
        miEstudios = EstudiosForm(request.POST)
        print(miEstudios)
        
        if miEstudios.is_valid:
            informacion2 = miEstudios.cleaned_data
            estudios = Estudios(
                carrera=informacion2["carrera"], 
                universidad=informacion2["universidad"], 
                idiomas=informacion2["idiomas"])
            estudios.save()
            return render(request, "AppFinal/padre.html")
        
    else:    
        miEstudios=EstudiosForm()
    return render(request, "AppFinal/estudios.html", {"miEstudios": miEstudios})

def experiencia(request):
    if request.method == "POST":
        miExperiencia = ExperienciaForm(request.POST)
        print(miExperiencia)
        
        if miExperiencia.is_valid:
            informacion3 = miExperiencia.cleaned_data
            experiencia = Experiencia(
                trabajos_anteriores=informacion3["trabajos_anteriores"], 
                años_experiencia=informacion3["años_experiencia"],)
            experiencia.save()
            return render(request, "AppFinal/padre.html")
    else:
        miExperiencia=ExperienciaForm
    return render(request, "AppFinal/experiencia.html", {"miExperiencia": miExperiencia})

def informacion(request):
    return render(request,'AppFinal/informacion.html')

def personalApi(request):
    cursos_todos = Personal.objects.all()
    return HttpResponse(serializers.serialize('json',cursos_todos))

def estudiosApi(request):
    estudios_todos = Estudios.objects.all()
    return HttpResponse(serializers.serialize('json',estudios_todos))

def experienciaApi(request):
    experiencia_todos = Experiencia.objects.all()
    return HttpResponse(serializers.serialize('json',experiencia_todos))
