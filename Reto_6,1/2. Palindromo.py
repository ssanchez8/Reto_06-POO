palabra = input("Ingrese su palabra aquí: ")

def detecta_palindromo(palabra):
    
    try: 
        if palabra.isnumeric() or palabra == "":
            raise ValueError("Por favor ingresa una palabra válida")
        palabra = str(palabra).lower()  
    
    except TypeError:
        print("Error: por favor ingresa una palabra válida")
        
    inicio = 0 
    final = len(palabra)-1 
    
    while inicio < final: 
        if palabra[inicio] != palabra[final]: 
            return False 
        inicio += 1 #Se comparan índices, si son iguales, se compara el segundo con el penúltimo. 
        final -= 1 #Se recorre la palabra completa, letra por letra, verificando si hay coincidencias
        
    return True 

try:
    if detecta_palindromo(palabra):
        print("Es palíndromo")
    else:
        print("No es palíndromo")

except ValueError as error:
    print("Error:", error)