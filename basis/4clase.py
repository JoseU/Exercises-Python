class RetornaString :
	def __init__ (self, texto) :
		self.texto = texto

	def returnText(self) :
		conc = self.texto  + " paso por aqui un texto"
		return conc


parrafo = RetornaString('j')

print parrafo.returnText()

