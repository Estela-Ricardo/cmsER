from django.shortcuts import render
from .models import Propriedade

def home(request):
    # Devolve todas as propriedades disponíveis
    propriedades_disponiveis = Propriedade.objects.filter(disponibilidade='Disponível').prefetch_related('mediaitem_set')
    return render(request, 'base.html',  {'propriedades_disponiveis': propriedades_disponiveis})