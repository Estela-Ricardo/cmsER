from django.urls import reverse
from django.utils.html import format_html
from django.contrib import admin
from .models import Mediador, Cliente, Propriedade, Proposta, BaseContent, Visita, Image, Video, File


admin.site.index_title = 'Inicio'
admin.site.site_title = 'Real Estate Pro'

class PropostaInline(admin.TabularInline):
    model = Proposta
    extra = 0  # Define o número de formulários em branco exibidos por padrão como 0

class VisitaInline(admin.TabularInline):
    model = Visita
    extra = 0

class BaseContentInline(admin.TabularInline):
    model = BaseContent
    extra = 0

class ImageInline(BaseContentInline):
    model = Image

class VideoInline(BaseContentInline):
    model = Video

class FileInline(BaseContentInline):
    model = File
    
@admin.register(Mediador)
class MediadorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone', 'morada', 'nif', 'iban']
    search_fields = ['nome', 'email', 'telefone', 'morada', 'nif', 'iban']
    list_filter = ['nif', 'nome']

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['leidc', 'nome', 'email', 'telefone', 'morada']
    search_fields = ['leidc', 'nome', 'email', 'telefone', 'morada']
    list_filter = ['nome']

@admin.register(Propriedade)
class PropriedadeAdmin(admin.ModelAdmin):
    list_display = ['id', 'mediador', 'venda', 'disponibilidade', 'estado', 'natureza', 'titulo']
    search_fields = ['id', 'mediador__nome', 'venda__nome', 'titulo', 'descricao']
    list_filter = ['disponibilidade', 'estado', 'natureza']
    inlines = [PropostaInline, VisitaInline]


    def save_model(self, request, obj, form, change):
        # Captura o utilizador autenticado
        user = request.user
        
        # Verifica se o mediador foi selecionado no formulário
        if form.cleaned_data['mediador']:
            # Se o mediador foi selecionado, salva a propriedade com o mediador selecionado
            obj.save()
        else:
            # Se o mediador não foi selecionado, associa o utilizador autenticado como mediador
            mediador = user.mediador if hasattr(user, 'mediador') else Mediador.objects.create(
                user=user,
                nome=user.username  # Define o nome do mediador como o nome de utilizador do utilizador
            )
            obj.save(mediador=mediador)
       
        super().save_model(request, obj, form, change)

# Vai ser usada para criar link para a Propriedade de Visita e Proposta
def link_to_propriedade(obj):
    if obj.propriedade:
        propriedade_id = obj.propriedade.id
        propriedade_titulo = obj.propriedade.titulo
        url = reverse("admin:realestatepro_propriedade_change", args=(propriedade_id,))
        return format_html('<a href="{}">{}</a>', url, propriedade_titulo)
    return None

link_to_propriedade.allow_tags = True
link_to_propriedade.short_description = 'Propriedade'

@admin.register(Proposta)
class PropostaAdmin(admin.ModelAdmin):
    list_display = ['id_proposta', 'cliente', link_to_propriedade, 'valor', 'data_proposta']
    search_fields = ['id_proposta', 'cliente__nome', 'propriedade__titulo']
    list_filter = ['cliente', 'data_proposta']

@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    list_display = ['id_visita', 'cliente', link_to_propriedade, 'data_visita']
    search_fields = ['id_visita', 'cliente__nome', 'propriedade__titulo']
    list_filter = ['cliente', 'data_visita']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    pass
