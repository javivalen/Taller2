from django import forms



class Formulario(forms.Form):
	#opciones para campo de genero
	OPCIONES_GENERO = (
		(1,"Masculino"),
		(2,"Femenino"),
		(3,"No responde")
	)

	#opciones para campo de tragos
	OPCIONES_TRAGOS = (
		(1, "Bebida"),
		(2, "Agua"),
		(3, "Jugo")
	)

	#opciones para campo de cursos
	OPCIONES_CURSOS = (
		(1, "Sección 1"),
		(2, "Sección 2"),
		(3, "Ayudantes y Auxiliares")
	)

	#nombre es un CharField: un campo de texto
	nombre = forms.CharField(label='Ingrese nombre' )

	#edad es un IntegerField: un campo numerico
	edad = forms.IntegerField(label='Ingrese edad')

	#Genero es un ChoiceField: un campo de opciones
	#Su widget, o como se visualiza a travez de html es un boton tipo radio
	Género = forms.ChoiceField(label='Ingrese el género con el que se identifica:', 
			choices=OPCIONES_GENERO, widget=forms.RadioSelect)

	#tomar es un Choice field: un campo de opciones
	#su widget corresponde a un campo de seleccion, este tiene parentesis por que 
	#	posee opciones, en este caso dejaremos todo como default
	tomar = forms.ChoiceField(choices = OPCIONES_TRAGOS, label='¿Qué quieres tomar?:',
			initial='', widget=forms.Select(), required=True)

	#personas es un multipleChoiceField: es decir se puede escoger mas de un opcion
	#su widget es un CheckBoxSelect, son botones que si estan apretados marcan verdadero
	personas=forms.MultipleChoiceField(choices=OPCIONES_CURSOS, 
		label='¿Con quiénes quiere compartir en el carrete?', widget=forms.CheckboxSelectMultiple)

	#acepto terminos es un BooleanField: tiene un valor de True o False
	#su widget se deja por defecto
	Acepto_terminos= forms.BooleanField(label='Me comprometo a bailar toda la noche')
	
	#si ya comprendio esta parte dirijase a ejemplo3/urls.py linea 11

