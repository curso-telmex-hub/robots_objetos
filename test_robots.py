from unittest import TestCase
import robots


# test para probar los movimientos de un robot en una malla
class movimientos_tests(TestCase):
    """supone que las posiciones de las x's y y's son mayores iguales  a cero"""
    max_x = 30
    max_y = 30

    def inicia_valores (self, robot, x, y, max_x = 0, max_y = 0):
        robot.x = x
        robot.y = y
        robot.min_x = 0
        robot.min_y = 0
        if max_x == 0:
            robot.max_x = self.max_x
        else:
            robot.max_x = max_x
        
        if max_y == 0:
            robot.max_y = self.max_y
        else:
            robot.max_y = max_y

    # def test_movimientos(self):
    #     pos_x = 10
    #     pos_y = 15    

    #     robot1 = robots.Robot (self.max_x, self.max_y)
    #     self.inicia_valores (robot1, pos_x, pos_y)
    #     print (robot1)

    #     # se prueba la funcion a la derecha
    #     self.inicia_valores (robot1, pos_x, pos_y)
    #     robot1.derecha ()
    #     self.assertEqual(robot1.x, 11)

    #     # se prueba la funcion a la izquierda
    #     self.inicia_valores (robot1, pos_x, pos_y)
    #     robot1.izquierda ()
    #     self.assertEqual(robot1.x, 9)

    #     # se prueba la funcion a la arriba
    #     self.inicia_valores (robot1, pos_x, pos_y)
    #     robot1.arriba ()
    #     self.assertEqual(robot1.y, 16)

    #     # se prueba la funcion a la abajo
    #     self.inicia_valores (robot1, pos_x, pos_y)
    #     robot1.abajo ()
    #     self.assertEqual(robot1.y, 14)
    
    def test_movimientos_acotados (self):
        pos_x = 10
        max_x_1 = pos_x + 1
        max_x_2 = pos_x + 2

        pos_y = 15
        max_y_1 = pos_y + 1
        max_y_2 = pos_y + 2

        robot1 = robots.Robot (max_x_1, max_y_1)
        self.inicia_valores (robot1, pos_x, pos_y)

        # se prueba la funcion a la derecha
        # no se puede mover
        self.inicia_valores (robot1, pos_x, pos_y, pos_x + 1, max_y_1)
        robot1.derecha ()
        self.assertEqual(robot1.x, pos_x)
        # si se puede mover
        self.inicia_valores (robot1, pos_x, pos_y, pos_x + 2, max_y_1)
        robot1.derecha ()
        self.assertEqual(robot1.x, pos_x + 1)

        # se prueba la funcion a la izquierda
        # no se puede mover
        self.inicia_valores (robot1, 0, pos_y, max_x_1, max_y_1)
        print (robot1)
        robot1.izquierda ()
        self.assertEqual(robot1.x, 0)
        # si se puede mover
        self.inicia_valores (robot1, 1, pos_y, max_x_1, max_y_1)
        robot1.izquierda ()
        self.assertEqual(robot1.x, 0)

        # se prueba la funcion a la arriba
        # no se puede mover
        self.inicia_valores (robot1, pos_x, pos_y, max_y_1, max_y_1)
        robot1.arriba ()
        self.assertEqual(robot1.y, pos_y)
        self.inicia_valores (robot1, pos_x, pos_y, max_y_2, max_y_2)
        # si se puede mover
        robot1.arriba ()
        self.assertEqual(robot1.y, pos_y + 1)

        # se prueba la funcion a la abajo
        # no se puede mover
        self.inicia_valores (robot1, pos_x, 0, max_y_1, max_y_1)
        robot1.abajo ()
        self.assertEqual(robot1.y, 0)
        # si se puede mover
        self.inicia_valores (robot1, pos_x, 1, max_y_1, max_y_1)
        robot1.abajo ()
        self.assertEqual(robot1.y, 0)
