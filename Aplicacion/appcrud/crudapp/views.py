from django.shortcuts import render, redirect
from .models import Tablaagenda
from .forms import AgendaForm
from django.shortcuts import redirect

from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("crudapp")


def select(request):
    modelo = Tablaagenda.objects.all()
    return render(request, "select.html", {"modelo": modelo})


def create(request):
    if request.method == "POST":
        form = AgendaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect("select")
            except:
                pass
    else:
        form = AgendaForm()
    return render(request, "create.html", {"form": form})


def update(request, id):
    modelo = Tablaagenda.objects.get(id=id)
    form = AgendaForm(
        initial={
            "Nombre": modelo.nombre,
            "Apellido": modelo.apellido,
            "Email": modelo.email,
            "Telefono": modelo.telefono,
            "Direccion": modelo.direccion,
        }
    )
    if request.method == "POST":
        form = AgendaForm(request.POST, instance=modelo)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect("/select")
            except Exception as e:
                pass
    return render(request, "update.html", {"form": form})


def delete(request, id):
    modelo = Tablaagenda.objects.get(id=id)
    try:
        modelo.delete()
    except:
        pass
    return redirect("select")
