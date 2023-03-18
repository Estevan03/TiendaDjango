from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('productos/', include('appProductos.urls')),
    path('usuario/', include('appUsuarios.urls')),
    path('carro/<str:idProd>', views.agregarCarro, name='agregarCarro'),
    path('carrito/', views.verCarrito, name='carrito'),
    path('eliminar/<str:id>', views.eliminarCarrito, name='eliminar'),
    path('cambiarCantidad/', views.cambiarCantidad),
]
