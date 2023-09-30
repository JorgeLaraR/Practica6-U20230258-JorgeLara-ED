class Articulo:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio


    def vender(self, cantidad_vendida):
        if cantidad_vendida <= self.cantidad:
            self.cantidad -= cantidad_vendida
            total_de_venta = cantidad_vendida * self.precio
            return f"Venta hecha. Total de pagar: ${total_de_venta}"
        else:
            return "No hay suficiente material para la venta."



producto1 = Articulo("Pantalón", 50, 42.50)
print(producto1.vender(15)) 