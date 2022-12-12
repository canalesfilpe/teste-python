
from django.shortcuts import render, redirect
from .models import Motorista

def home(request):
    motoristas = Motorista.objects.all()
    return render(request, "index.html", {"motoristas":motoristas })


def salvar(request):
    motorista = request.POST.get()
    Motorista.objects.create({motorista})
    motoristas = Motorista.objects.all()
    return render(request, "index.html", {"motoristas": motoristas})


def editar(request, id):
    motorista = Motorista.objects.get(id=id)
    return render(request, "update.html", {"motorista": motorista})


def update(request, id):
    vnome = request.POST.get('nome')
    vtelefone = request.POST.get('telefone')
    vcnh = request.POST.get('cnh')
    motorista = Motorista.objects.get(id=id)
    motorista.nome = vnome
    motorista.telefone = vtelefone
    motorista.cnh = vcnh
    motorista.save()
    return redirect(home)


def delete(request, id):
    motorista = Motorista.objects.get(id=id)
    motorista.delete()
    return redirect(home)
