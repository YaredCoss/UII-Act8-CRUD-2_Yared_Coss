from django.shortcuts import render, redirect, get_object_or_404
from .models import Guia

# Listar guias
def index(request):
    guias = Guia.objects.all()
    return render(request, 'listar_guia.html', {'guia': guias})

# Ver guia (opcional, puedes usarlo si quieres detalle)
def ver_guia(request, id):
    guia = get_object_or_404(Guia, id=id)
    return render(request, 'ver_guia.html', {'guia': guia})

# Agregar guia
def agregar_guia(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        experiencia = request.POST['experiencia']
        idiomas = request.POST['idiomas']
        especialidad = request.POST['especialidad']
        calificacion = request.POST['calificacion']
        Guia.objects.create(nombre=nombre, apellido=apellido, experiencia=experiencia, idiomas=idiomas, especialidad=especialidad, calificacion=calificacion)
        return redirect('inicio')
    return render(request, 'agregar_guia.html')

# Editar guia
def editar_guia(request, id):
    guia = get_object_or_404(Guia, id=id)
    if request.method == 'POST':
        guia.nombre = request.POST['nombre']
        guia.apellido = request.POST['apellido']
        guia.experiencia = request.POST['experiencia']
        guia.idiomas = request.POST['idiomas']
        guia.especialidad = request.POST['especialidad']
        guia.calificacion = request.POST['calificacion']
        guia.save()
        return redirect('inicio')
    return render(request, 'editar_guia.html', {'guia': guia})

# Borrar guia
def borrar_guia(request, id):
    guia = get_object_or_404(Guia, id=id)
    if request.method == 'POST':
        guia.delete()
        return redirect('inicio')
    return render(request, 'borrar_guia.html', {'guia': guia})