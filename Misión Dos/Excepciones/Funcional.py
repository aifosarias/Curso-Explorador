import Calculadora as cd
def Menu():
    while True:
        try:

            opc1 = (int(input("introduce el primer número: ")))
            opc2 = (int(input("introduce el primer segundo: ")))
            operacion = input("introduce la operación a realizar(Suma,Resta,Multipliación,División):")
            operacion.lower()
            return opc1,opc2,operacion
            break
        except ValueError:
            print("debes ingresar un numero: ")
            
def OPERACIONES(opc1,opc2,operacion):
    if operacion == "suma":
        print(cd.suma(opc1, opc2))
    elif operacion == "resta":
        print(cd.resta(opc1, opc2))
    elif operacion == "multiplicacion":
        print(cd.multiplicacion(opc1, opc2))
    elif operacion == "division":
        print(cd.division(opc1, opc2))
    else:
        print("Texto")

while True:
    try:
        print("Programa calculadora: ")
        respuesta= input("Desea realizar una operación? (Y/N): ")
        r=respuesta.lower()
        if r == "y":
            opc1,opc2,operacion= Menu()
            OPERACIONES(opc1,opc2,operacion)
        else:
            break
    except:
        print("Termino")

print("Programa Finalizada")