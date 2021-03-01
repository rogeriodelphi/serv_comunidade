from django.contrib import admin

from .models import Reserva, Atendimento


@admin.register(Reserva)
class Reserva(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'atendimento', 'data', 'confirmado')


@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'supervisor', 'polo', 'vagas', 'tipo', 'data', 'valor', 'termo')
