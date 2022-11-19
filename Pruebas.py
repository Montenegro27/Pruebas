import modulos

salida = False 

while salida != True:
    opcion = input("Seleccione la funcion")

    if(opcion == "+"):
        valor1 = int(input("Ingrese un valor"))
        valor2 = int(input("Ingrese segundo valor"))
        print(modulos.suma(valor1, valor2))
    elif(opcion == "-"):
        valor1 = int(input("Ingrese un valor"))
        valor2 = int(input("Ingrese segundo valor"))
        print(modulos.resta(valor1,valor2))
    elif(opcion == "*"):
        valor1 = int(input("Ingrese un valor"))
        valor2 = int(input("Ingrese segundo valor"))
        print(modulos.multiplicacion(valor1,valor2))
    elif(opcion == "/"):
        valor1 = int(input("Ingrese un valor"))
        valor2 = int(input("Ingrese segundo valor"))
        print(modulos.divison(valor1,valor2))
    elif(opcion == "5"):
        salida = False
    else:
        print("Opción no Válida")
             