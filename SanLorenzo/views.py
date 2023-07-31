from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from SanLorenzo.models import Futbolista, Socio, Autoridad
from SanLorenzo.forms import FutbolistaFormulario

def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    return http_response


def listar_futbolistas(request):
    contexto = {
        "futbolistas": Futbolista.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='templates_base/lista_futbolistas.html',
        context=contexto,
    )
    return http_response


def crear_futbolista(request):
    if request.method == "POST":
        formulario = FutbolistaFormulario(request.POST)
        if formulario.is_valid():
            data=formulario.cleaned_data
            nombre=data["nombre"]
            apellido=data["apellido"]
            posicion=data["posicion"]
            futbolista = Futbolista(nombre=nombre, apellido=apellido, posicion=posicion)
            futbolista.save()
            url_exitosa=reverse("SanLorenzo")
            return redirect(url_exitosa)
        else:
            formulario=FutbolistaFormulario()
        http_response=render(
            request=request,
            template_name="templates_base/formulario_futbolista.html",
            context={"formulario":formulario}
        )
        return http_response