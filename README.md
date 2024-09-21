# Reto_06-POO

## 1. Operaciones
Para este programa se añadieron 4 excepciones. 
```python
try: 
    numero1 = float(numero1)
    numero2 = float(numero2)
    
except ValueError: 
    print("Error: por favor ingresa un valor numérico")
    exit()

```
La primera excepción se puede levantar si el usuario ingresa incorrectamente los valores numéricos que el programa debe operar. Al ingresar datos que no sean de tipo float, se levanta un ValueError. 

```python
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
```
La segunda excepción se presenta cuando se realiza la división. En caso de que el usuario haya ingresado un 0 como número 2 a operar, el progama levantará una excepción al presentarse una división por cero. 

``` python
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
```
La tercera excepción se levanta en caso de que el usuario no haya ingresado los caracteres correctos, definidos para las respetivas operaciones. 

``` python

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
```
Por último, en la ejecución del programa se presentará una última excepción general, en caso de que se presente algún tipo de error con los datos que se ingresaron por el usuario y el programa falle

## 2. Palíndromo

``` python
def detecta_palindromo(palabra):
    
    try: 
        if palabra.isnumeric() or palabra == "":
            raise ValueError("Por favor ingresa una palabra válida")
        palabra = str(palabra).lower()  
    
    except TypeError:
        print("Error: por favor ingresa una palabra válida")
```
Para este programa se decidió establecer dos excepciones. En primer lugar se levantó un ValueError en caso de que el usuario ingrese un dato numérico o que en su defecto sea una cadena vacía. Posterior a esto, se levantó otra excepción más general en caso de no detectar un string correctamente. 

## 3. Números Primos
``` python

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
```
Para este programa, en primer lugar se levantó una excepción para verificar el ingreso de los datos por parte del usuario. Debido a que para realizar el control del ingreso de datos se decidió romper la ejecución de la función cuando el programa reciba un 0 y los números ingresados deben ser positivos, es necesario levantar una excepción en caso de que el usuario ingrese valores negativos. 

``` python
def lista_de_primos(numeros):
  primos = [] 
  for num in numeros:
    try:
        if detecta_primos(num): 
            primos.append(num)  
    
    except TypeError:
        print("Error: al verificar si el número es primo")
      
  return primos
```
Luego, para la verificación del correcto funcionamiento de la función que detecta números primos dentro de la función que los agrega a la lista, se levanta una excepción en caso de que la ejecución de la función detecta_primos sea errónea. 

## 4. Suma mayor consecutiva

``` python
while True: 
    try:
        numero_ingresado=int(input("Número: "))              
        if numero_ingresado == 0: 
            break
        lista_de_numeros.append(numero_ingresado)  
    
    except ValueError:
        print("Error: por favor ingrese un número válido")
```
Para este programa se levantaron tres excepciones. La primera de ellas al momento de realizar la toma de los datos ingresados por parte del usuario. En caso de que no sean valores adecuados para el registro, se levanta un ValueError

``` python
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
```
Posteriormente dentro de la ejecución de la función principal suma_mayor_consecutiva, se realiza la verificación de los datos inicialmente, y se levanta una excepción para realizar la comprobación de los datos ingresados en caso de poseer algún tipo de error. Esta excepción también ayuda a realizar el control de datos que quizá se hayan podido filtrar de la primera excepción. Por último, en caso de presentar algún inconveniente al momento de realizar el acceso a los índices de la lista que contiene a los números, se levanta un IndexError para realizar la verificación adecuada de la lista creada a partir de los datos ingresados. 

## 5. Anagrama 
