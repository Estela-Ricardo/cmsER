from django.urls import path
from . import views

urlpatterns = [
    path('mine/',
         views.ManagePropriedadeListView.as_view(),
         name='gestao_propriedade_lista'),
    path('create/',
         views.PropriedadeCreateView.as_view(),
         name='propriedade_create'),
    path('<pk>/edit/',
         views.PropriedadeUpdateView.as_view(),
         name='propriedade_edit'),
    path('<pk>/delete/',
         views.PropriedadeDeleteView.as_view(),
         name='propriedade_delete'),
]