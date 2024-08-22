def detecta_primos(num):
  if num < 2: 
    return False
  for i in range(2, num):  
    if num % i == 0:  
      return False 
  return True

print("Ingrese por favor una lista de números (0 para terminar): ") 

numeros = []

while True: 
    try:
        numero_ingresado=int(input("Número: ")) 
        
        if numero_ingresado < 0: 
            raise ValueError("Por favor ingrese un número positivo")
        
        if numero_ingresado == 0: 
            break
        
        numeros.append(numero_ingresado) 
    
    except ValueError as error: 
        print("Error:", error)

numeros.sort() 

def lista_de_primos(numeros):
  primos = [] 
  for num in numeros:
    try:
        if detecta_primos(num): 
            primos.append(num)  
    
    except TypeError:
        print("Error: al verificar si el número es primo")
      
  return primos
      
      
print("La lista de números del usuario es: ", numeros)

primos = lista_de_primos(numeros) 

print("De esa lista de  números, los primos son: ", primos)