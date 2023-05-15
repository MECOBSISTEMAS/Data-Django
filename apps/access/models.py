from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Acesso(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name=_("Esse campo serve para identificar os usuarios"),
        related_name='acesso',
        on_delete=models.CASCADE,
        blank=True, 
        null=True
    )
    permissao = models.CharField(
        verbose_name=_("Esse campo serve para identificar as permissões de cada usuario"),
        choices=(('consulta','consulta'),('alimentacao','alimentacao')),
        default='consulta',
        max_length=32,
        blank=True, 
        null=True
    )
    

    class Meta:
        verbose_name = _("acesso")
        verbose_name_plural = _("acessos")
        db_table = 'acessos'
        managed = True
        ordering = ['user']
        

    def __str__(self):
        return f'{self.user} : {self.permissao}'

    def get_absolute_url(self):
        return reverse("acesso_detail", kwargs={"pk": self.pk})
