ganancias = float(input("Indica tus ganancias (eh thalers): "))
if ganancias <= 85528:
    impuesto = 0.18 * ganancias - 556.02
else:
    impuesto = 14839.02 + 0.32 * (ganancias - 85528)

if impuesto < 0:
    print("No tienes que pagar impuestos")
else:
    print("El impuesto es", round(impuesto))
