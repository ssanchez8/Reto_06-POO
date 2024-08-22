print("Ingrese por favor una lista de números (digitar 0 para terminar): ") 

lista_de_numeros = [] 

while True: 
    try:
        numero_ingresado=int(input("Número: "))              
        if numero_ingresado == 0: 
            break
        lista_de_numeros.append(numero_ingresado)  
    
    except ValueError:
        print("Error: por favor ingrese un número válido")

def suma_mayor_consecutiva (lista_de_numeros):
    
    mayor = 0 
    
    try:
        for i in range(len(lista_de_numeros)-1):  
            suma = lista_de_numeros[i] + lista_de_numeros[i+1] 
            if suma > mayor: 
                mayor = suma
    
    except TypeError:
        print("Error: vuelve a verificar que los números ingresados sean enteros")
    except IndexError:
        print("Error: no se accedió a un índice válido")
        
    return mayor

mayor = suma_mayor_consecutiva(lista_de_numeros)

print("La lista entregada por el usuario es: ", lista_de_numeros)

print("La suma de mayor valor es:", mayor)