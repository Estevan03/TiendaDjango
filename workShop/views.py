from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def agregarCarro(request, idProd):
    idProd = int(idProd)
    regUsuario = request.user
    msj = None
    #leer reg del producto en Producto
    existe = Producto.objects.filter(id=idProd).exists()
    if existe:
        regProducto = Producto.objects.get(id=idProd)
        # si no existe en carrito:
        existe = Carro.objects.filter(producto=regProducto, estado= 'activo', usuario= 
regUsuario).exists()
        if existe:
            # instanciar un objeto de la clase Carrito
            regCarro = Carro.objects.get(producto=regProducto, estado= 'activo', usuario= regUsuario)
            #incrementar cantidad
            regCarro.cantidad += 1
        else:
            regCarro = Carro(producto=regProducto, usuario= regUsuario, valUnit = regProducto.precioUnitario)
        # guardar el registro
        regCarro.save()
    else: 
        # dar mensaje
        msj = 'Producto no disponible'
        # redireccionar a 'verProducto'
    return verProducto(request, idProd, msj) 