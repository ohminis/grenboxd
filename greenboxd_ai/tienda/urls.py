from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('registro/', views.registro_usuario, name='registro'),
    path('ingreso/', views.ingreso_usuario, name='ingreso'),
    path('salir/', views.salir_usuario, name='salir'),
    path('consulta/', views.crear_consulta, name='consulta'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/editar/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),
    
    # Rutas para el Carrito
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/limpiar/', views.limpiar_carrito, name='limpiar_carrito'),
]
