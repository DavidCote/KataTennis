import sys
sys.path.insert(0,'./src')
import unittest
from Tenis import Tenis

class PruebaTenis(unittest.TestCase):

		#gana un jugador (A=4,B=2)
	def test_uno(self):
		p = Tenis()

		p.puntoA()
		p.puntoA()
		p.puntoA()
		p.puntoA()

		p.puntoB()
		p.puntoB()

		self.assertEqual(True,p.existeGanador())

	#hay un Deuce
	def tes_cuatro(self):
		p = Tenis()

		p.puntoA()
		p.puntoA()
		p.puntoA()
		p.puntoA()

		p.puntoB()
		p.puntoB()
		p.puntoB()
		p.puntoB()

		self.assertEqual(True,p.existeDeuce())


	#jugador A tiene la ventaja (A=3,B=1)
	def tes_dos(self):
		p = Tenis()

		p.puntoA()
		p.puntoA()
		p.puntoA()

		p.puntoB()

		self.assertEqual(True,p.comprobarVentaja())

	#jugador B tiene la ventaja (A=0,B=2)
	def tes_tres(self):
		p = Tenis()

		p.puntoA()
		p.puntoA()

		self.assertEqual(False,p.comprobarVentaja())

	

	#el jugador A tiene mayor puntuacion que B (A=3,B=2)
	def tes_cinco(self):
		p = Tenis()

		p.puntoA()
		p.puntoA()

		p.puntoB()

		self.assertEqual(True,p.mayorPuntuacion())