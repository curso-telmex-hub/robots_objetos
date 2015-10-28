# archivo que tiene funciones para pintar la posicion de un robot

class Malla:
    car_rep_primero = "-"
    car_rep_ultimo = "-"
    car_rep_relleno = " "
    car_rep_posicion = "*"

    def __init__ (self, robot):
        self.robot = robot

    def pinta_simple (self, maximo_x, caracter):
        print ("|%s|" % (caracter * (maximo_x - 2)))

    def pinta_primero (self, maximo_x):
        self.pinta_simple (maximo_x, self.car_rep_primero)

    def pinta_ultimo (self, maximo_x):
        self.pinta_simple (maximo_x, self.car_rep_ultimo)

    def pinta_relleno (self, maximo_x):
        self.pinta_simple (maximo_x, self.car_rep_relleno)

    def pinta_posicion (self, maximo_x, caracter, posicion, caracter_pos):
        if posicion == 0:
            print ("%s%s|" % (caracter_pos, caracter * (maximo_x - 2)))
        elif posicion == maximo_x - 1:
            print ("|%s%s" % (caracter * (maximo_x - 2), caracter_pos))
        else:
            print ("|%s%s%s|" % (caracter * (posicion - 1), caracter_pos,
                                 caracter * (maximo_x - posicion - 2)))

    def pinta_malla (self):
        
        # el contador va al reves
        for i in range (self.robot.max_y-1, -1, -1):
            # se verifica si se tiene que dibujar la posicion del robot o no
            if i == self.robot.y:
                if i == 0 or i == self.robot.max_x - 1:
                    self.pinta_posicion (self.robot.max_x, "-", self.robot.x, "*")
                else:
                    self.pinta_posicion (self.robot.max_x, " ", self.robot.x, "*")
            else:
                if i == 0:
                    self.pinta_primero (self.robot.max_x)
                elif i == self.robot.max_x - 1:
                    self.pinta_ultimo (self.robot.max_x)
                else:
                    self.pinta_simple (self.robot.max_x, " ")


