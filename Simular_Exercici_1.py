'''
Implementa la simulació de l'exercici 1: averies d'un sistema de producción
'''

from Distribucions import uniforme_discreta as UD
import random
import csv

# Funcio principal
def Simular_Exercici_1():
	global rellotge

	iniciar_variables()
	
	# Determina el proper event
	esdeveniment = obtenir_esdeveniment_proper()
	
	while not finalitzar_simulacio(esdeveniment):

		# Avanca rellotge
		rellotge = esdeveniment[0]

		# Actualitza l'estat del sistema i la llista de nous esdeveniments, depenent del tipus d'esdeveniment
		if esdeveniment[1] == "Avaria component":
			esdeveniment_avaria()
		if esdeveniment[1] == "Fi reparacio":
			esdeveniment_fi_reparacio()

		# Escriu informacio intermedia
		#escriure_informacio(estat, esdeveniment)

		# Determina el proper event
		esdeveniment = obtenir_esdeveniment_proper()

	return (temps_funcionament,estat)


def iniciar_variables():
	global maxim_temps
	global maxim_maquines_avariades
	global llista_esdeveniments
	global estat
	global temps_funcionament
	global rellotge

        # Definició dels paràmetres de la simulació
	maxim_temps = 1000.0
	maxim_maquines_avariades = 2

	# Initzalització del rellotge, de l'estat (nombre de maquines avariades) i llista d'esdeveniments
	estat = 0
	llista_esdeveniments = []
	rellotge = 0.0
	afegir_esdeveniment_avaria()
	temps_funcionament = 0.0
 

# Procesa l'esdeveniment del tipus avaria
def esdeveniment_avaria():
	global temps_funcionament
	global estat
	global maxim_maquines_avariades

	# Afegeix nous esdeveniments
	afegir_esdeveniment_fi_reparacio()
	afegir_esdeveniment_avaria()

	# Actualitza l'estat del sistema
	estat += 1

	# Actualitza comptadors
	if estat == maxim_maquines_avariades:
		temps_funcionament = rellotge


# Procesa l'esdeveniment del tipus fi de reparacio
def esdeveniment_fi_reparacio():
	global estat

	# Actualitza l'estat del sistema
	estat += -1


# Afegeix un esdeveniment de tipus fi de reparació a la llista
def afegir_esdeveniment_fi_reparacio():
	global llista_esdeveniments

        # Crea l'esdeveniment nou
	temps_esdeveniment = rellotge + 4.5
	tipus_esdeveniment = 'Fi reparacio'
	nou_esdeveniment = temps_esdeveniment, tipus_esdeveniment

	# S'afegeix l'esdeveniment a la llista d'esdeveniments
	llista_esdeveniments += [nou_esdeveniment]


# Afegeix un esdeveniment de tipus avaria a la llista
def afegir_esdeveniment_avaria():
	global llista_esdeveniments

	# Crea l'esdeveniment nou
	temps_entre_avaries = UD(3,8)
	temps_esdeveniment = rellotge + temps_entre_avaries
	tipus_esdeveniment = 'Avaria component'
	nou_esdeveniment = temps_esdeveniment, tipus_esdeveniment

	# S'afegeix l'esdeveniment a la llista d'esdeveniments
	llista_esdeveniments += [nou_esdeveniment]


# Funcio per veure si finalitza la simulacio 
def finalitzar_simulacio(esdeveniment):
	temps_esdeveniment = esdeveniment[0]
	return (temps_esdeveniment >= maxim_temps or estat >= maxim_maquines_avariades)


# Funcio que obté el proper esdeveniment
def obtenir_esdeveniment_proper():
	global llista_esdeveniments
	llista_esdeveniments.sort(key=lambda tup: tup[0]) # El primer element de la tupla fa referencia al temps
	esdeveniment_proper = llista_esdeveniments[0]
	llista_esdeveniments = llista_esdeveniments[1:]
	return esdeveniment_proper

# Funcio impressions intermedies
def escriure_informacio(estat, esdeveniment):
	print ('{0:5.1f} {1:15} {2:2d}'.format(esdeveniment[0], esdeveniment[1], estat))

#Aquí podem la semilla que volem
random.seed(2**19-1)
#print(str(Simular_Exercici_1()[0]).replace('.',','))
nsim=100
Nlotes=100
with open('ordinadors.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	for j in range(Nlotes):
		lote_media=0
		for n in range(nsim):
			lote_media+= Simular_Exercici_1()[0]

		lote_media= lote_media/nsim
		writer.writerow([str(lote_media).replace('.',',')])
		#print('he escrit algo')
	print('final')
		
