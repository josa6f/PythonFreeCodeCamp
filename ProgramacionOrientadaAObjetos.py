#Paradigma de programacion 
#Clases - tienen atributos (caracteristicas) y metodos (Funcionalidad)

#Clase - Cuenta Bancaria

#Atributos - Numero de cuenta, Nombre del titular, Balance inicial, Balance Actual, Fecha de apertura

#Metodos - retirar, depositar, generar balance, actualizar datos

#Instancia - es cada elemento creado apartir de la clase, en este caso serian las cuentas creadas - SELF es la instancia actual

class CuentaBancaria: #Clase
    def __init__(self, num_cuenta, nombre_titular, balance):
        self.num_cuenta = num_cuenta #Atributos
        self.nombre_titular = nombre_titular
        self.balance = balance

    def generar_balance(self): #Metodos
        print(self.balance)
    
    def depositar(self, Deposito):
        if Deposito > 0:
            self.balance += Deposito
    
    def retirar(self, Retiro):
        if Retiro <= self.balance:
            self.balance -= Retiro
        else:
            print("Cuenta sin fondos suficientes")


cuenta_1 = CuentaBancaria("0001", "Diego", 1000)

print(cuenta_1.balance)

cuenta_1.depositar(1500)

print(cuenta_1.balance)

cuenta_1.retirar(3000)

print(cuenta_1.balance)