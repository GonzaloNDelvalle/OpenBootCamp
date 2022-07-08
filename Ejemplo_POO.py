"""Este es un ejemplo de composición de clases con una BBDD"""

class Categorias:
    idCategoria = 0
    nombre = ""

class Proveedores:
    idProveedor = 0
    nombre = ""

class Productos:
    idProducto = 0
    categoriaProducto = Categorias()
    precio = 0
    tamanio = 0
    tipoDeProducto = 0
    cifProvedor = Proveedores()

termo = Productos()
termo.cifProvedor.nombre
termo.categoriaProducto.idCategoria