'''
Crear un programa que permita crear objetos de la clase CuentaBancaria, cuyos atributos son: numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion.
Aplicar encapsulamiento y definir los métodos apropiados para controlar y gestionar los atributos de los objetos creados.
Utilizar un menu para las diferentes opciones, tales como aperturaCta, consignar, retirar y transferencia entre otros.
'''
class CuentaBancaria:
    def __init__(self, numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion):
        set (numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion)
    
    def set (self, numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion):
        self.__numeroCta = numeroCta
        self.__nombreCliente = nombreCliente
        self.__saldoCta = saldoCta
        self.__fechaApertura = fechaApertura
        self.__ultimoRetiro = ultimoRetiro
        self.__ultimaConsignacion = ultimaConsignacion
    
    def set_numeroCta(self, x):
        self.__numeroCta = x 
    
    def set_nombreCliente (self , x):
        self.__nombreCliente = x 
        
    def set_saldoCta (self, x):
        self.__saldoCta = x
   
    def set_fechaApertura (self , x):
        self.__fechaApertura = x
    
    def set_ultimoRetiro (self , x):
        self.__ultimoRetiro = x
    
    def set_ultimaConsignacion (self , x):
        self.__ultimaConsignacion = x 
    
    # Metodos para acceder
    
    def get__numeroCta (self):
        return self.__numeroCta
        
    def get_nombreCliente(self):
        return self.__nombreCliente
    
    def get_saldoCta(self):
        return self.__saldoCta
    
    def get_fechaApertura(self):
        return self.__fechaApertura
    
    def get_ultimoRetiro(self):
        return self.__ultimoRetiro
    
    def get_ultimaConsignacion(self):
        return self.__ultimaConsignacion
    
    def mostrar_informacion(self):
        print(f"Cuenta: {self.__numeroCta}, Cliente: {self.__nombreCliente}, Saldo: {self.__saldoCta}, Fecha Apertura: {self.__fechaApertura}")

#Funcion para crear un menu
def menu ():
    cuentas = {}
    while True:
        print ("\n=== BANCO MINÚ ===")
        print ("1.Crear Cuenta Bancaria.")
        print ("2.Depositar")
        print ("3.Retirar.")
        print ("4.Mostrar informacion Bancaria.")
        print ("5.Salir.")
        
        opcion = imput ("Digite una opcion.")
        
        if opcion == "1":
            numeroCta = input("Ingrese el número de cuenta: ")
            nombreCliente = input("Ingrese su nombre completo: ")
            saldoCta = float(input("Ingrese su monto inicial: "))
            fechaApertura = input("Ingrese la fecha de apertura (dd/mm/yyyy): ")
            cuenta = CuentaBancaria(numeroCta, nombreCliente, saldoCta, fechaApertura)
            cuentas[numeroCta] = cuenta
            print("Cuenta creada exitosamente.")
        
         elif opcion == "2":
            numeroCta = input("Ingrese el número de cuenta: ")
            if numeroCta in cuentas:
                monto = float(input("Ingrese el monto a consignar: "))
                cuentas[numeroCta].consignar(monto)
            else:
                print("Cuenta no encontrada.")
    
        
