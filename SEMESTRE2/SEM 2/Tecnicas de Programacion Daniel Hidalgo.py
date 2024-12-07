class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def mostrar_producto(self):
        print(f"{self.nombre} - Precio: ${self.precio} - Stock: {self.cantidad}")
    
    def actualizar_stock(self, cantidad):
        self.cantidad += cantidad
        print(f"Stock actualizado de {self.nombre}: {self.cantidad}")
    
    def vender(self, cantidad):
        if self.cantidad >= cantidad:
            self.cantidad -= cantidad
            print(f"Se vendieron {cantidad} unidades de {self.nombre}.")
        else:
            print(f"No hay suficiente stock de {self.nombre}. Solo quedan {self.cantidad} unidades.")

class Tienda:
    def __init__(self):
        self.inventario = []
    
    def agregar_producto(self, producto):
        self.inventario.append(producto)
    
    def mostrar_inventario(self):
        if not self.inventario:
            print("El inventario está vacío.")
        else:
            for producto in self.inventario:
                producto.mostrar_producto()
    
    def valor_total_inventario(self):
        total = sum(p.precio * p.cantidad for p in self.inventario)
        print(f"Valor total del inventario: ${total}")

# Crear productos
producto_1 = Producto("Camiseta", 20, 50)
producto_2 = Producto("Auriculares", 50, 30)

# Crear tienda y agregar productos
tienda = Tienda()
tienda.agregar_producto(producto_1)
tienda.agregar_producto(producto_2)

# Mostrar inventario
tienda.mostrar_inventario()

# Actualizar stock y vender
producto_1.actualizar_stock(10)
producto_2.vender(5)

# Mostrar inventario actualizado
tienda.mostrar_inventario()

# Calcular valor total del inventario
tienda.valor_total_inventario()