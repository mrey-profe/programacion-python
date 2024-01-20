class CuentaBancaria:
    nombre_titular: str
    numero_cuenta: str
    saldo: float

    def __init__(self, nombre_titular: str, numero_cuenta: str, saldo: float = 0) -> None:
        if len(nombre_titular) == 0:
            raise Exception("La cuenta debe tener titular")
        self.nombre_titular = nombre_titular
        if len(numero_cuenta) != 24:
            raise Exception("Número de cuenta erróneo")
        self.numero_cuenta = numero_cuenta
        if saldo < 0:
            self.saldo = 0
        else:
            self.saldo = saldo
        # self.saldo = math.max(saldo, 0)
    
    def __str__(self):
        return f"Titular: {self.nombre_titular}. \nNúmero de cuenta: {self.numero_cuenta}. \nSaldo: {self.saldo}"

    def movimiento(self, cantidad: float, ingreso: bool = True) -> bool: #Delvuelve False si la cuenta queda en números rojos
        if ingreso:
            self.saldo += cantidad
        else:
            self.saldo -= cantidad

        if saldo < 0:
            return False
        return True


if __name__ == "__main__":
    try:
        cuenta1 = CuentaBancaria("Pepe López", "ES3415755896242374115896", 200)
        print(cuenta1)
    except:
        print("No se ha podido crear la cuenta")
    try:
        cuenta2 = CuentaBancaria("María", "ES3414665896242374115896")
        print(cuenta2)
    except:
        print("No se ha podido crear la cuenta")

    if cuenta1.movimiento(100) == False:
        print("OJO, números rojos")
    print(cuenta1)
    if cuenta1.movimiento(200, False) == False:
        print("OJO, números rojos")
    print(cuenta1)