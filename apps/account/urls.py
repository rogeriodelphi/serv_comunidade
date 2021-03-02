from django.urls import path

app_name = 'account'

from . import views


urlpatterns = [
    path('login/', views.user_login, name='user_login'),
]