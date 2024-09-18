import math

class Point:
    def __init__(self, x:int, y:int):
        #Se levanta una excepción para asegurar que los valores de x, y sean enteros
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Los valores de las coordenadas x e y deben ser enteros")        
        self._x = x
        self._y = y
        
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def compute_distance(self, other_point):
        #Se levanta una excepción para asegurar que el punto 2 sea una instancia de la clase Point
        if not isinstance(other_point, Point):
            raise ValueError("El punto 2 debe ser una instancia de la clase Point")
        
        return ((self._x - other_point.get_x())**2 + (self._y - other_point.get_y())**2)**0.5

class Line:
    def __init__(self, point1:Point, point2:Point):
        #Se levanta una excepción para verificar que los dos puntos no sean iguales, y poder definir una línea correctamente.
        if point1.get_x() == point2.get_x() and point1.get_y() == point2.get_y():
            raise ValueError("Para poder definir una línea, los puntos no pueden ser iguales")
        self._length = point1.compute_distance(point2)
        self._start = point1
        self._end = point2
    
    def get_start(self):
        return self._start
    
    def get_end(self):
        return self._end
    
    def get_length(self):
        return self._length    
    
class Shape:
    def __init__(self, vertices):
        #Se verifica que haya al menos 3 vértices para poder definir una polígono, si no, se levantra una excepción
        if len(vertices) < 3:
            raise ValueError("Para poder definir una polígono, se necesitan al menos 3 vértices")
        self._vertices = vertices
        self._edges = [Line(vertices[i], vertices[(i+1)%len(vertices)]) for i in range(len(vertices))] #Cierra la figura con el primer punto (resto de la división de i entre el número de vértices)
        self._inner_angles = self.inner_angles()
        self._is_regular = self.is_regular()
        
    def inner_angles(self):
        self._inner_angles = []
        for i in range(len(self._vertices)):
            prev_point = self._vertices[i-1]
            current_point = self._vertices[i]
            next_point = self._vertices[(i+1)%len(self._vertices)]
            a = prev_point.compute_distance(current_point)
            b = current_point.compute_distance(next_point)
            c = next_point.compute_distance(prev_point)
            
            #Se levanta una excepción si hay divisiones por cero
            try:
                angle_radians = math.acos((a**2 + b**2 - c**2)/(2*a*b))
            except ZeroDivisionError:
                raise ValueError("No se puede dividir por cero")   
                            
            angle_degrees = round(math.degrees(angle_radians))  
            self._inner_angles.append(angle_degrees)
        return self._inner_angles
                
    def is_regular(self):
        first_angle = self._inner_angles[0]
        for angle in self._inner_angles:
            if angle != first_angle:
                return False
        return True        
    
    def get_edges(self):
        return self._edges
    
    def get_vertices(self):
        return self._vertices
    
    def get_inner_angles(self):
        return self._inner_angles
    
    def compute_area(self):
        pass
    
    def compute_perimeter(self):
        pass
    
    def compute_inner_angles(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, vertices):
        #Se levanta una excepción si los vértices no forman un rectángulo, se necesitan 4 vértices
        if len(vertices) != 4:
            raise ValueError("Para poder definir un rectángulo, se necesitan 4 vértices")
        super().__init__(vertices)
        
    def compute_area(self):
        print(self._edges[0].get_length())
        return self._edges[0].get_length() * self._edges[1].get_length()
    
    def compute_perimeter(self):
        return 2*self._edges[0].get_length() + 2*self._edges[1].get_length()
    
    def compute_inner_angles(self):
        return self._inner_angles
        
class Square(Rectangle):
    def __init__(self, vertices):
        #Se levanta una excepción si los vértices no forman un cuadrado, se necesitan 4 vértices
        if len(vertices) != 4:
            raise ValueError("Para poder definir un cuadrado, se necesitan 4 vértices")
        super().__init__(vertices)
    
    def compute_area(self):
        return self._edges[0].get_length()**2
    
    def compute_perimeter(self):
        return 4*self._edges[0].get_length()
    
    def compute_inner_angles(self):
        return self._inner_angles
   
class Triangle(Shape):
    def __init__(self, vertices):
        #Se levanta una excepción si los vértices no forman un triángulo, se necesitan 3 vértices
        if len(vertices) != 3:
            raise ValueError("Para poder definir un triángulo, se necesitan 3 vértices")
        super().__init__(vertices)
        
    def compute_area(self):
        s = self.compute_perimeter()/2
        a = self._edges[0].get_length()
        b = self._edges[1].get_length()
        c = self._edges[2].get_length()
        return (s*(s-a)*(s-b)*(s-c))**0.5
    
    def compute_perimeter(self):
        pass

class EquilateralTriangle(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
    
    def compute_area(self):
        return (3**0.5/4) * self._edges[0].get_length()**2 #Deducción a partir de partir el triángulo en dos triángulos rectángulos de 30° y 60°
    
    def compute_perimeter(self):
        return 3*self._edges[0].get_length()
    
    def compute_inner_angles(self):
        return self._inner_angles
    
class IsoscelesTriangle(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        
    def compute_perimeter(self):
        return self._edges[0].get_length() + self._edges[1].get_length() + self._edges[2].get_length()
    
    def compute_area(self):
        return Triangle.compute_area(self)
    
    def compute_inner_angles(self):
        return self._inner_angles


class ScaleneTriangle(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        
    def compute_perimeter(self):
        return self._edges[0].get_length() + self._edges[1].get_length() + self._edges[2].get_length()
    
    def compute_area(self):
        return Triangle.compute_area(self)
    
    def compute_inner_angles(self):
        return self._inner_angles

class RectangleTriangle(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        
    def compute_perimeter(self):
        return self._edges[0].get_length() + self._edges[1].get_length() + self._edges[2].get_length()
    
    def compute_area(self):
        return Triangle.compute_area(self)
    
    def compute_inner_angles(self):
        return self._inner_angles
    
### Test
try:
    ## Square
    square = Square([Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0)])
    print("Cuadrado")
    print(f"El área del cuadrado es {square.compute_area()}")
    print(f"El perímetro del cuadrado es {square.compute_perimeter()}")
    print(f"Los ángulos internos son {square.compute_inner_angles()}\n")

    ## Rectangle
    print("Rectángulo")
    rectangle = Rectangle([Point(0, 0), Point(0, 4), Point(2, 4), Point(2, 0)])
    print(f"El área del rectángulo es {rectangle.compute_area()}")
    print(f"El perímetro del rectángulo es {rectangle.compute_perimeter()}")
    print(f"Los ángulos internos son {rectangle.compute_inner_angles()}\n")

    ## Equilateral Triangle
    print("Triángulo Equilátero")
    eq_triangle = EquilateralTriangle([Point(2, 0), Point(4, 0), Point(3, 2)])
    print(f"El área del triángulo equilátero es {eq_triangle.compute_area()}")
    print(f"El perímetro del triángulo equilátero es {eq_triangle.compute_perimeter()}")
    print(f"Los ángulos internos son {eq_triangle.compute_inner_angles()}\n")

    ## Isosceles Triangle
    iso_triangle = IsoscelesTriangle([Point(3, 1), Point(9, 1), Point(6, 4)])
    print("Triángulo Isósceles")
    print(f"El área del triángulo isósceles es {iso_triangle.compute_area()}")
    print(f"El perímetro del triángulo isósceles es {iso_triangle.compute_perimeter()}")
    print(f"Los ángulos internos son {iso_triangle.compute_inner_angles()}\n")

    ## Scalene Triangle
    sca_triangle = ScaleneTriangle([Point(3, 5), Point(11, 6), Point(8, 8)])
    print("Triángulo Escaleno")
    print(f"El área del triángulo escaleno es {sca_triangle.compute_area()}")
    print(f"El perímetro del triángulo escaleno es {sca_triangle.compute_perimeter()}")
    print(f"Los ángulos internos son {sca_triangle.compute_inner_angles()}\n")

    ## Rectangle Triangle
    rect_triangle = RectangleTriangle([Point(6, 3), Point(12, 3), Point(6, 8)])
    print("Triángulo Rectángulo")
    print(f"El área del triángulo rectángulo es {rect_triangle.compute_area()}")
    print(f"El perímetro del triángulo rectángulo es {rect_triangle.compute_perimeter()}")
    print(f"Los ángulos internos son {rect_triangle.compute_inner_angles()}")

    #Ejemplo con error. Se intenta crear un cuadrado con 3 vértices
    square = Square([Point(0, 0), Point(0, 1), Point(1, 1)])

except ZeroDivisionError as e:
    print(f"Error al crear la polígono: {e}")

except ValueError as e:
    print(f"Error al crear la polígono: {e}")

