from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_maquinarias, name='lista_maquinarias'),
    path('crear/', views.crear_maquinaria, name='crear_maquinaria'),
    path('editar/<int:pk>/', views.editar_maquinaria, name='editar_maquinaria'),
    path('eliminar/<int:pk>/', views.eliminar_maquinaria, name='eliminar_maquinaria'),
]
