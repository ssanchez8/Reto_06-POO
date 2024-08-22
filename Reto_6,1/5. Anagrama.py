def encuentra_anagramas(lista_palabras):
    diccionario_anagramas = {} 
    for palabra in lista_palabras:  
        try:
            if not isinstance(palabra, str):
                raise ValueError("Por favor ingrese palabras válidas")
            palabras_ordenadas = tuple(sorted(palabra)) 
            if palabras_ordenadas in diccionario_anagramas: 
                diccionario_anagramas[palabras_ordenadas].append(palabra) 
            else:
                diccionario_anagramas[palabras_ordenadas] = [palabra] 
        
        except ValueError as error:
            print("Error:", error)
   
    resultado = []    
    
    for grupo_palabras in diccionario_anagramas.values(): 
        if len(grupo_palabras) > 1: 
            for palabra in grupo_palabras: 
                resultado.append(palabra)
                
    return resultado
     

try:    
    lista_palabras = input("Ingrese las palabras separadas por espacios: ").split()
    if not lista_palabras:
        raise ValueError("La lista no puede estar vacía")
    print("Los anagramas de la lista ingresada son: ", encuentra_anagramas(lista_palabras))  

except ValueError as error:
    print("Error:", error)