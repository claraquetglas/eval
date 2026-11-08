'''
Implementa la simulació de l'exercici 2: averies d'un sistema de producción
'''
from Distribucions import uniforme_discreta as UD
from Distribucions import bernoulli as ber
import random
import csv

# Funcio principal
def Simular_Exercici_2():
	global rellotge

	iniciar_variables()
	
	# Determina el proper event
	esdeveniment = obtenir_esdeveniment_proper()
	
	while not finalitzar_simulacio(esdeveniment):

		# Avanca rellotge
		rellotge = esdeveniment[0]

		# Actualitza l'estat del sistema i la llista de nous esdeveniments, depenent del tipus d'esdeveniment
		if esdeveniment[1] == "Arribada Trucada":
			esdeveniment_arribada_trucada()
		if esdeveniment[1] == "Fi trucada":
			esdeveniment_fi_trucada()

		# Escriu informacio intermedia
		#escriure_informacio(estat, esdeveniment)

		# Determina el proper event
		esdeveniment = obtenir_esdeveniment_proper()

	return (temps_promig_espera)


def iniciar_variables():
	global maxim_temps
	global llista_esdeveniments
	global estat
	global temps_promig_espera
	global Nclients

        # Definició dels paràmetres de la simulació
	maxim_temps = 720
	

	# Initzalització del rellotge, de l'estat (nombre de maquines avariades) i llista d'esdeveniments
	estat = []
	llista_esdeveniments = []
	rellotge = 0.0
	afegir_esdeveniment_arribada_trucada()
	temps_promig_espera=0
	Nclients = 0
 
# Afegeix un esdeveniment de tipus avaria a la llista
def afegir_esdeveniment_arribada_trucada():
	global llista_esdeveniments

	# Crea l'esdeveniment nou
	temps_entre_trucades = UD(14,19)
	temps_esdeveniment = rellotge + temps_entre_trucades
	tipus_esdeveniment = 'Arribada Trucada'
	nou_esdeveniment = temps_esdeveniment, tipus_esdeveniment

	# S'afegeix l'esdeveniment a la llista d'esdeveniments
	llista_esdeveniments += [nou_esdeveniment]

# Funcio que obté el proper esdeveniment
def obtenir_esdeveniment_proper():
	global llista_esdeveniments
	llista_esdeveniments.sort(key=lambda tup: tup[0]) # El primer element de la tupla fa referencia al temps
	esdeveniment_proper = llista_esdeveniments[0]
	llista_esdeveniments = llista_esdeveniments[1:]
	return esdeveniment_proper


# Procesa l'esdeveniment del tipus avaria
def esdeveniment_arribada_trucada():
	
	global estat
	
	# Afegeix nous esdeveniments
	if(len(estat)==0):
		afegir_esdeveniment_fi_trucada()
	
	afegir_esdeveniment_arribada_trucada()

	# Actualitza l'estat del sistema
	estat.append(rellotge)

	# Actualitza comptadors

# Afegeix un esdeveniment de tipus fi de reparació a la llista
def afegir_esdeveniment_fi_reparacio():
	global llista_esdeveniments

        # Crea l'esdeveniment nou
	temps_esdeveniment = rellotge + ber(0.5,13,16)												###nem per aqui
	tipus_esdeveniment = 'Fi reparacio'
	nou_esdeveniment = temps_esdeveniment, tipus_esdeveniment

	# S'afegeix l'esdeveniment a la llista d'esdeveniments
	llista_esdeveniments += [nou_esdeveniment]


# Procesa l'esdeveniment del tipus fi de reparacio
def esdeveniment_fi_trucada():
	global estat
	# Afegeix nous esdeveniments
	if (len(estat)>1):
		afegir_esdeveniment_fi_trucada()
	#actualitzar els comptadors
	
	# Actualitza l'estat del sistema
	estat += estat[1:]








# Funcio per veure si finalitza la simulacio 
def finalitzar_simulacio(esdeveniment):
	temps_esdeveniment = esdeveniment[0]
	return (temps_esdeveniment >= maxim_temps or estat >= maxim_maquines_avariades)




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
	print('Final')
		