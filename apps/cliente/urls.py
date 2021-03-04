from django.urls import path

app_name = 'cliente'

from . import views

urlpatterns = [
    path('novo/', views.adicionar_cliente, name='adicionar_cliente'),
]
