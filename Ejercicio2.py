class Usuario:
    def __init__(self, nombre, correo, saldo_inicial):
        self.nombre = nombre
        self.correo = correo
        self.saldo = saldo_inicial


    def depositar(self, monto):
        self.saldo += monto
        return f"Se ha depositado ${monto}. Saldo actual: ${self.saldo}"


    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return f"Se ha retirado ${monto}. Saldo actual: ${self.saldo}"
        else:
            return "Saldo insuficiente para el retiro."


usuario1 = Usuario("Jorge Lara", "jorge@outlook.com", 20000)

print(usuario1.depositar(560))  
print(usuario1.retirar(250))    