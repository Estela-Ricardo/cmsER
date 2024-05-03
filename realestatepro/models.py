from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
import re

class Mediador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, blank=True)
    telefone = models.CharField(max_length=15, blank=True)
    morada = models.CharField(max_length=100, blank=True)
    nif = models.IntegerField(blank=True, null=True)
    iban = models.CharField(max_length=34, blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Mediador"
        verbose_name_plural = "Mediadores"

class Cliente(models.Model):
    def generate_custom_id():
        prefixo = 'CLI'
        numero_autoincrement = Propriedade.objects.count()
        return f"{prefixo}{numero_autoincrement:04}"
    
    leidc = models.CharField(max_length=20, primary_key=True, default=generate_custom_id)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, blank=True)
    telefone = models.CharField(max_length=15, blank=True)
    morada = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nome


class Propriedade(models.Model):
    DISPONIBILIDADE_CHOICES = [
        ('Retirado', 'Retirado'),
        ('Reservado', 'Reservado'),
        ('Vendido', 'Vendido'),
        ('Disponível', 'Disponível'),
    ]
    NATUREZA_CHOICES = [
        ('Escritório', 'Escritório'),
        ('Herdade', 'Herdade'),
        ('Armazém', 'Armazém'),
        ('Casa Antiga', 'Casa Antiga'),
        ('Bloco de apartamentos', 'Bloco de apartamentos'),
        ('Residencial', 'Residencial'),
        ('Apartamento', 'Apartamento'),
        ('Moradia', 'Moradia'),
    ]
    ESTADO_CHOICES = [
    ('Recuperado', 'Recuperado'),
    ('Por recuperar', 'Por recuperar'),
    ('Em construção', 'Em construção'),
    ('Renovado', 'Renovado'),
    ('Novo', 'Novo'),
    ]
   
    def generate_custom_id():
        prefixo = 'REP'
        numero_autoincrement = Propriedade.objects.count() + 1000
        return f"{prefixo}{numero_autoincrement:04}"

    id = models.CharField(primary_key=True, max_length=10, default=generate_custom_id)
    natureza = models.CharField(max_length=50, choices=NATUREZA_CHOICES, blank=True)
    mediador = models.ForeignKey(Mediador, null=True, blank=True, related_name='propriedades_criadas', on_delete=models.SET_NULL)
    disponibilidade = models.CharField(max_length=50, choices=DISPONIBILIDADE_CHOICES, blank=True)
    estado = models.CharField(max_length=150, choices=ESTADO_CHOICES, blank=True)
    titulo = models.CharField(max_length=150, blank=True)
    descricao = models.TextField(max_length=150, blank=True)
    quartos = models.IntegerField(blank=True, null=True)
    area_privativa_bruta = models.IntegerField(blank=True, null=True)
    area_util = models.IntegerField(blank=True, null=True)
    preco = models.IntegerField(blank=True, null=True)
    ano_construcao = models.IntegerField(blank=True, null=True, default=timezone.now())
    contrato_mediacao = models.CharField(max_length=100, blank=True)
    morada = models.CharField(max_length=100, blank=True)
    codigo_postal = models.CharField(max_length=10, blank=True)
    numero = models.IntegerField(blank=True, null=True)
    piso = models.CharField(max_length=10, blank=True)
    fracao = models.CharField(max_length=10, blank=True)
    distrito = models.CharField(max_length=50, blank=True)
    concelho = models.CharField(max_length=50, blank=True)
    freguesia = models.CharField(max_length=50, blank=True)
    zona = models.CharField(max_length=50, blank=True)
    certificado_energetico = models.CharField(max_length=100, blank=True)
    # imagens = models.FileField(upload_to='media/images/', blank=True, null=True)
    # video = models.FileField(upload_to='media/videos/', blank=True, null=True)
    venda = models.ForeignKey(Cliente, blank=True, null=True, on_delete=models.CASCADE)
    criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criacao']

    def save(self, *args, mediador=None, **kwargs):

        # Se o mediador não estiver definido e o mediador não for None, associa-o como mediador
        if not self.mediador_id and mediador is not None:
            self.mediador = mediador
                
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
    

class Proposta(models.Model):
    id_proposta = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, related_name='propostas_feitas', on_delete=models.CASCADE)
    propriedade = models.ForeignKey(Propriedade, on_delete=models.CASCADE)
    data_proposta = models.DateField(default=timezone.now)
    valor = models.IntegerField()
    criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criacao']

    def __str__(self):
        return f"Proposta {self.id_proposta}"


class Visita(models.Model):
    id_visita = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, related_name='visitas_efetuadas', on_delete=models.CASCADE)
    propriedade = models.ForeignKey(Propriedade, on_delete=models.CASCADE)
    data_visita = models.DateField(default=timezone.now)
    criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criacao']

    def __str__(self):
        return f"Visita {self.id_visita}"

# Models para conteúdo polimorfico (imagens, videos, files)
class MediaItem(models.Model):
    MEDIA_CHOICES = [
        ('imagem', 'Imagem'),
        ('video', 'Vídeo'),
        ('arquivo', 'Arquivo'),
    ]

    propriedade = models.ForeignKey(Propriedade, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=MEDIA_CHOICES)
    imagem = models.ImageField(upload_to='images/', null=True, blank=True)
    video = models.URLField(null=True, blank=True)
    arquivo = models.FileField(upload_to='files/', null=True, blank=True)

    def __str__(self):
        return f"{self.get_tipo_display()} para {self.propriedade}"