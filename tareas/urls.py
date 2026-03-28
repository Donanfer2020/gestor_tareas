from django.urls import path
from . import views

urlpatterns = [
    path('/', views.lista_tareas),
    path('tareas/', views.crear_tarea),
]