from django.urls import path

app_name = 'atendimento'

from . import views


urlpatterns = [
    path('', views.home, name='home'),
]
