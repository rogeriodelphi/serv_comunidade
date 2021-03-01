from django.db import models


class Polo(models.Model):
    polo = models.CharField('Polo', max_length=60)
    unidade = models.CharField('Unidade', max_length=60)
    endereco = models.CharField('Endereço', max_length=150)
    telefone = models.CharField('Telefone', max_length=17)
    email = models.EmailField()

    def __str__(self):
        return self.polo

    class Meta:
        db_table = 'Polo'
        ordering = ['polo']
        verbose_name = 'Polo'
        verbose_name_plural = 'Polos'
