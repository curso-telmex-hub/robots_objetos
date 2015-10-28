"""programa que va pintando el movimiento de un robot"""
import random
import robots
import malla

# se inicializa aleatoriamente la posicion de un robot
max_x = 10
max_y = 10
x = random.randint (0, max_x - 1)
y = random.randint (0, max_y - 1)

robot1 = robots.Robot (max_x, max_y)
robot1.x = x
robot1.y = y

malla1 = malla.Malla (robot1)
# va pintando la posicion de un robot, sale del ciclo con la letra q
print ("Sale del ciclo con la letra 'q'")

while True:
    
    malla1.pinta_malla ()
    cadena = str (input (">>> "))
    if cadena == "q":
        break
    else:
        # se obtiene el siguiente moviento
        mov_hor = random.randint (1, 2)

        if mov_hor % 2 == 0:
            robot1.derecha ()
        else:
            robot1.izquierda ()
        print ()

        mov_vert = random.randint (1, 2)
        if mov_vert % 2 == 0:
            robot1.arriba ()
        else:
            robot1.abajo ()

