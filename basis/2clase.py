class Humano : 
	def __init__ (self, edad, ciclo) :
		self.edad = edad
		self.ciclo = ciclo
		#print "Soy un nuevo objeto"

	def hablar(self, mensaje):
		print self.edad
		print self.ciclo
		print mensaje

pedro = Humano(26, 2)
jose = Humano(ciclo =3, edad=24)


pedro.hablar("ahi vamos pedro")
jose.hablar("ahi vamos jose")

