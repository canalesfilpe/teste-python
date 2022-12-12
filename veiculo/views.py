from django.shortcuts import render, redirect
from .models import Veiculo

def home(request):
    veiculos = Veiculo.objects.all()
    return render(request, "index.html", {"veiculos": veiculos})


def salvar(request):
    veiculo = request.POST.get()
    Veiculo.objects.create({veiculo})
    veiculos = Veiculo.objects.all()
    return render(request, "index.html", {"veiculos": veiculos})


def editar(request, id):
    veiculo = Veiculo.objects.get(id=id)
    return render(request, "update.html", {"veiculo": veiculo})


def update(request, id):
    vplaca = request.POST.get('placa')
    vmarca = request.POST.get('marca')
    vveiculo = request.POST.get('veiculo')
    vkm_troca_oleo = request.POST.get('km_troca_oleo')
    veiculo = Veiculo.objects.get(id=id)
    veiculo.placa = vplaca
    veiculo.marca = vmarca
    veiculo.veiculo = vveiculo
    veiculo.km_troca_oleo = vkm_troca_oleo
    veiculo.save()
    return redirect(home)


def delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    veiculo.delete()
    return redirect(home)
