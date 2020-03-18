class Tenis:
    def __init__(self):
        self.__jugadorA=0
        self.__jugadorB=0

    def existeGanador(self):
        if self.__jugadorA >=4 and self.__jugadorA >= self.__jugadorB+2:
            return True
        if self.__jugadorB >=4 and self.__jugadorB >= self.__jugadorA+2:
            return True
        return False

    def comprobarVentaja(self):
        if self.__jugadorA and self.__jugadorB >=3 and self.__jugadorA == self.__jugadorB+1:
            return True
        if self.__jugadorB and self.__jugadorA >=3 and self.__jugadorB == self.__jugadorA+1:
            return True
        return False

    def mayorPuntuacion(self):
        if self.__jugadorA>self.__jugadorB:
            return "Jugador A"
        else:
            return "Jugador B"

    def existeDeuce(self):
        return self.__jugadorB and self.__jugadorB >=4 and self.__jugadorA is self.__jugadorB

    def puntoA(self):
        self.__jugadorA+=1

    def puntoB(self):
        self.__jugadorB+=1

    def marcador(self):
        
        if self.existeGanador():
            return self.mayorPuntuacion() + " Gana!"
        if self.comprobarVentaja():
            return  self.mayorPuntuacion() + " tiene la ventaja"
        if self.existeDeuce():
            return 'Deuce'
        if self.__jugadorA is self.__jugadorB:
            return str(self.__jugadorA) + ' all'

        return str(self.__jugadorA) + ',' + str(self.__jugadorB)