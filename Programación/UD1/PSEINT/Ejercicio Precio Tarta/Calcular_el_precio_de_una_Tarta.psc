Algoritmo Calcular_Precio_de_una_Tarta
	
	Escribir "Escoja entre los tres sabores que le ofrecemos: Manzana, Fresa y Chocolate. Tenga en cuenta que solo tenemos estos sabores. (Escr�balo en min�sculas)"
	Leer sabor
	Segun sabor Hacer
		"manzana":
			tartaSola<-18
			Escribir "La tarta sola de: " sabor " te costar�: " tartaSola
		"fresa":
			tartaSola<-16
			Escribir "La tarta sola de: " sabor " te costar�: " tartaSola
		"chocolate":
			Escribir "�Qu� tipo de chocolate quieres? �Negro o Blanco? (escr�balo en min�sculas)"
			Leer tipo_chocolate
			si tipo_chocolate=blanco Entonces
				tartaSola<-15
				Escribir "La tarta sola de " sabor " te costar�: " tartaSola
			SiNo
				tartaSola<-14
				Escribir "La tarta sola de " sabor " te costar�: " tartaSola
			FinSi
	FinSegun
	Escribir "�Deseas nata? Responda con s� o no (Costar� 2.5 euros m�s)"
	Leer nata
	Escribir "�Deseas que pongamos su nombre? Responda con s� o no (Costar� 2.75 euros m�s)"
	Leer nombre
	Si nata="s�" Entonces
		Si nombre="s�" Entonces
			valortarta<- tartaSola+2.5+2.75
		SiNo
			valortarta<- tartaSola+2.5
		FinSi
	SiNo
		Si nombre="s�" Entonces
			valortarta<- tartaSola+2.75
		SiNo
			valortarta<- tartaSola
		FinSi
	FinSi
	
	Escribir "La tarta le costar� " valortarta " euros."
FinAlgoritmo
