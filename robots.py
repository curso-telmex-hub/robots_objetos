# se define la clase robot
import random

class Robot:
    x = 0
    y = 0
    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0

    def __init__ (self, max_x, max_y):
        self.x = random.randint (0, max_x - 1)
        self.y = random.randint (0, max_y - 1)
        self.max_x = max_x
        self.max_y = max_y
    
    # mueve el robot a la derecha una unidad y
    # verifica que no se puede salir de la maya
    def derecha (self):
        if self.x < self.max_x - 1:
            self.x += 1
        
    # mueve el robot a la izquierda una unidad
    def izquierda (self):
        if self.x > self.min_x:
            self.x -= 1
        
    # mueve el robot arriba una unidad
    def arriba (self):
        if self.y < self.max_y - 1:
            self.y += 1

    # mueve el robot para abajo una unidad
    def abajo (self):
        if self.y > self.min_y:
            self.y -= 1

    def mueve_hor (self):
        mov_hor = random.randint (1, 2)

        if mov_hor % 2 == 0:
            self.derecha ()
        else:
            self.izquierda ()

    def mueve_vert (self):
        mov_vert = random.randint (1, 2)

        if mov_vert % 2 == 0:
            self.arriba ()
        else:
            self.abajo ()

    def __str__ (self):
        return ("x = %d, y = %d, min_x = %d, min_y = %d, max_x = %d, max_y = %d" % 
                (self.x, self.y, self.min_x, self.min_y, self.max_x, self.max_y ))
