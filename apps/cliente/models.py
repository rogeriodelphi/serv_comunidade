from django.db import models


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=60)
    telefone = models.CharField('Telefone', max_length=17, help_text='Informe o telefone com Whatszapp')

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'Cliente'
        ordering = ['nome']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
