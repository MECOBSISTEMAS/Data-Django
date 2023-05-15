from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Acesso

@receiver(post_save, sender=User)
def create_acesso(sender, instance, created, **kwargs):
    if created:
    	Acesso.objects.create(user=instance)
     
