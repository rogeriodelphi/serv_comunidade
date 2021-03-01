from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    telefone = models.CharField('Telefone', max_length=17, help_text='Informe o telefone com Whatsapp')
    eSupervisor = models.BooleanField(default=False)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    class Meta:
        ordering = ['username']
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
