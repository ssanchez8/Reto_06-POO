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



