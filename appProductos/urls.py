from django.urls import path
from . import views
urlpatterns = [
    path('categorias/', views.verCategorias, name='categorias'), 
    path('productos/<str:idCategoria>', views.verProductosCategoria, name='productos'),
    path('producto/<str:idProd>', views.verProducto, name='un_producto'),
]

def verProducto(request, idProd, msj = None):
    #Consultar 
    idProd = int(idProd)
    regProducto = Producto.objects.get(id= idProd)
    #ensamblar context
    context = {
        'producto': regProducto,
        'titulo': 'Detalles de ' + str(regProducto.nombre),
    }
    if msj:
        context['mensaje']= msj
        #renderizar
        return render(request, 'productos/producto.html', context)
