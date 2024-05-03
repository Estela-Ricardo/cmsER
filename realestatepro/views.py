from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Propriedade
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class MediadorMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)

class MediadorEditMixin:
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class MediadorPropriedadeMixin(MediadorMixin,
                               LoginRequiredMixin,
                               PermissionRequiredMixin):
    model = Propriedade
    fields = ['natureza', 'mediador', 'disponibilidade', 'estado', 'titulo', 'descricao', 'quartos', 
              'area_privativa_bruta', 'area_util', 'preco', 'ano_construcao', 'contrato_mediacao', 
              'morada', 'codigo_postal', 'numero', 'piso', 'fracao', 'distrito', 'concelho', 'freguesia', 
              'zona', 'certificado_energetico', 'venda']
    success_url = reverse_lazy('gestao_propriedade_lista')

class MediadorPropriedadeEditMixin(MediadorPropriedadeMixin, MediadorEditMixin):
    template_name = 'propriedades/gestao/propriedade/form.html'

class ManagePropriedadeListView(MediadorPropriedadeMixin, ListView):
    model = Propriedade
    template_name = 'propriedades/gestao/propriedade/list.html'
    permission_required = 'propriedades.view_propriedade'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            if hasattr(self.request.user, 'mediador'):
                return qs.filter(mediador=self.request.user.mediador)
            else:
                return qs.none()  # Retorna um queryset vazio se o usuário não for um mediador
        else:
            return qs.none()  # Retorna um queryset vazio se o usuário não estiver autenticado


class PropriedadeCreateView(MediadorPropriedadeEditMixin, CreateView):
    permission_required = 'propriedades.add_propriedade'

class PropriedadeUpdateView(MediadorPropriedadeEditMixin, UpdateView):
    permission_required = 'propriedades.change_propriedade'

class PropriedadeDeleteView(MediadorPropriedadeMixin, DeleteView):
    template_name = 'propriedades/gestao/propriedade/delete.html'
    permission_required = 'propriedades.delete_propriedade'