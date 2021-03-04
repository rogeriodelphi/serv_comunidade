from django.urls import path

app_name = 'account'

from . import views


urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('area-logada/', views.area_logada, name='area_logada'),
    path('logout/', views.user_logout, name='user_logout'),
]