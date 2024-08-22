numero1 = (input("Por favor ingresa el primer número a operar: "))
operacion = input("Por favor selecciona la operación (+, -, *, /): ")
numero2 = (input("Por favor ingresa el segundo número a operar: "))

try: 
    numero1 = float(numero1)
    numero2 = float(numero2)
    
except ValueError: 
    print("Error: por favor ingresa un valor numérico")
    exit()

def calculos(numero1, numero2, operacion):
    if operacion == "+": 
        return numero1 + numero2
    elif operacion == "-":
        return numero1 - numero2
    elif operacion == "*":
        return numero1 * numero2
    elif operacion == "/":
        if numero2 !=0: 
            return numero1 / numero2
        else:
            raise ZeroDivisionError("No se puede dividir por cero") 
    else: 
        raise ValueError("Operación no válida, verifique el signo/símbolo requerido")   

try: 
    resultado = calculos(numero1, numero2, operacion) 
except ValueError as error: 
    print("Error:", error)
except ZeroDivisionError as error: 
    print("Error:", error)
except TypeError: 
    print("Error: no se puede realizar la operación con los tipos de datos ingresados, verifica que la operación sea entre dos números")
else: 
    if resultado is not None: 
        print(f"El resultado de {numero1} {operacion} {numero2} es {resultado}") 

