from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('<int:id>', views.ver_guia, name='ver_guia'),
    path('agregar/', views.agregar_guia, name='agregar_guia'),
    path('editar/<int:id>/', views.editar_guia, name='editar_guia'),
    path('borrar/<int:id>/', views.borrar_guia, name='borrar_guia'),
]