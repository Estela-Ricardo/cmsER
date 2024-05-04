from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
from .models import Propriedade

@receiver(post_delete, sender=Propriedade)
def delete_propriedade_image(sender, instance, **kwargs):
    if instance.imagem:
        if os.path.isfile(instance.imagem.path):
            os.remove(instance.imagem.path)
