from django.shortcuts import render, get_object_or_404, redirect
from .models import Maquinaria
from .forms import MaquinariaForm

def lista_maquinarias(request):
    maquinarias = Maquinaria.objects.all()
    for maquinaria in maquinarias:
        maquinaria.caracteristicas_list = maquinaria.caracteristicas.split('\n')
    return render(request, 'maquinarias/lista_maquinarias.html', {'maquinarias': maquinarias})

def crear_maquinaria(request):
    if request.method == 'POST':
        form = MaquinariaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_maquinarias')
    else:
        form = MaquinariaForm()
    return render(request, 'maquinarias/crear_maquinaria.html', {'form': form})

def editar_maquinaria(request, pk):
    maquinaria = get_object_or_404(Maquinaria, pk=pk)
    if request.method == 'POST':
        form = MaquinariaForm(request.POST, request.FILES, instance=maquinaria)
        if form.is_valid():
            form.save()
            return redirect('lista_maquinarias')
    else:
        form = MaquinariaForm(instance=maquinaria)
    return render(request, 'maquinarias/editar_maquinaria.html', {'form': form})

def eliminar_maquinaria(request, pk):
    maquinaria = get_object_or_404(Maquinaria, pk=pk)
    if request.method == 'POST':
        maquinaria.delete()
        return redirect('lista_maquinarias')
    return render(request, 'maquinarias/eliminar_maquinaria.html', {'maquinaria': maquinaria})
