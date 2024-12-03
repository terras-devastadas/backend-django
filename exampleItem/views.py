from django.shortcuts import render, get_object_or_404, redirect
from .models import Comunidade
from .forms import ComunidadeForm

# Create
def criar_comunidade(request):
    if request.method == 'POST':
        form = ComunidadeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_comunidades')
    else:
        form = ComunidadeForm()
    return render(request, 'criar_comunidade.html', {'form': form})

# Read
def listar_comunidades(request):
    comunidades = Comunidade.objects.all()
    return render(request, 'listar_comunidades.html', {'comunidades': comunidades})

# Update
def atualizar_comunidade(request, pk):
    comunidade = get_object_or_404(Comunidade, pk=pk)
    if request.method == 'POST':
        form = ComunidadeForm(request.POST, request.FILES, instance=comunidade)
        if form.is_valid():
            form.save()
            return redirect('listar_comunidades')
    else:
        form = ComunidadeForm(instance=comunidade)
    return render(request, 'atualizar_comunidade.html', {'form': form, 'comunidade': comunidade})

# Delete
def deletar_comunidade(request, pk):
    comunidade = get_object_or_404(Comunidade, pk=pk)
    if request.method == 'POST':
        comunidade.delete()
        return redirect('listar_comunidades')
    return render(request, 'deletar_comunidade.html', {'comunidade': comunidade})
