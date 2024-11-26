from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastro_list, name='cadastro_list'),
    path('cadastro/nova/', views.criar_cadastro, name='criar_cadastro'),
]