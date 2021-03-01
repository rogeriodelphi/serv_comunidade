from django.db import models

from ..account.models import User
from ..cliente.models import Cliente
from ..polo.models import Polo


class Atendimento(models.Model):
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE)
    polo = models.ForeignKey(Polo, on_delete=models.CASCADE)
    vagas = models.IntegerField()
    tipo = models.CharField('Tipo de Atendimento', max_length=60)
    data = models.DateTimeField()
    valor = models.CharField('Valor do Atendimento', max_length=60)
    # polo = models.CharField('Polo de Atendimento', max_length=60)
    termo = models.TextField('termo de Aceite', help_text='Informe nesse campo todas as condições que o cliente deve'
                                                          ' aceitar para o atendimento')

    def __str__(self):
        return self.tipo + ' - ' + self.data.strftime('%d%m%Y, %H:%M') + ' -' + self.valor

    class Meta:
        db_table = 'Atendimento'
        ordering = ['-data']
        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservas')
    atendimento = models.ForeignKey(Atendimento, on_delete=models.CASCADE, related_name='reservas')
    data = models.DateTimeField(auto_now=True)
    confirmado = models.BooleanField(default=False)

    def __str__(self):
        return '%s - %s' % (self.atendimento, self.cliente)

    class Meta:
        db_table = 'Reserva'
        ordering = ['cliente']
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
