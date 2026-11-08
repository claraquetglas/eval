'''
Implementa la simulació de l'exercici 3: La consulta de un metge.
'''

from Distribucions import uniforme_continua as UC
from Distribucions import Triangular as triang
from Distribucions import exponencial as exponencial
import random
import csv

mitjana = 1/18
minim=22
maxim=32
a=10
b=15
c=13
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
		if esdeveniment[1] == "Arribada_pacient":
			esdeveniment_arribada_pacient()
		if esdeveniment[1] == "Fi consulta":
			esdeveniment_fi_consulta()
		if esdeveniment[1] == "Fi proba":
			esdeveniment_fi_proba()

		# Escriu informacio intermedia
		#escriure_informacio(esdeveniment)

		# Determina el proper event
		esdeveniment = obtenir_esdeveniment_proper()
		#print(finalitzar_simulacio(esdeveniment)== False)
		
	#print(temps_espera/Npacients_atesos)
	#return (temps_espera_consulta/Npacients_consulta )
	return(temps_espera_proba/Npacients_proba)


def iniciar_variables():
	global maxim_temps
	global llista_esdeveniments
	global cua_1
	global cua_2
	global rellotge
	global temps_espera_consulta
	global temps_espera_proba
	global Npacients_consulta
	global Npacients_proba

        # Definició dels paràmetres de la simulació
	maxim_temps = 480
	

	# Initzalització del rellotge, de l'estat (nombre de maquines avariades) i llista d'esdeveniments
	llista_esdeveniments = []
	cua_1 = 0
	cua_2 = 0
	rellotge = 0.0
	temps_espera_consulta = 0
	temps_espera_proba = 0
	Npacients_consulta = 0
	Npacients_proba = 0

	afegir_esdeveniment_nou_pacient()
	


# Afegeix un esdeveniment de tipus avaria a la llista
def afegir_esdeveniment_nou_pacient():
	global llista_esdeveniments
	global rellotge
	# Crea l'esdeveniment nou
	temps_entre_trucades = exponencial(mitjana)
	temps_esdeveniment = rellotge + temps_entre_trucades
	tipus_esdeveniment = 'Arribada_pacient'
	nou_esdeveniment = temps_esdeveniment, tipus_esdeveniment

	# S'afegeix l'esdeveniment a la llista d'esdeveniments
	llista_esdeveniments += [nou_esdeveniment]



# Procesa l'esdeveniment del tipus avaria
def esdeveniment_arribada_pacient():
	global cua_1
	global rellotge
	global temps_espera_consulta
	global temps_espera_proba
	global Npacients_consulta
	global Npacients_proba

	
	# Afegeix nous esdeveniments
	if cua_1 < 2:
		afegir_esdeveniment_fi_consulta()
	else:
		temps_espera_consulta +=1

	afegir_esdeveniment_nou_pacient()

	# Actualitza l'estat del sistema
	cua_1 += 1
	Npacients_consulta +=1
	# Actualitza comptadors


def afegir_esdeveniment_fi_consulta():
	global llista_esdeveniments
	global rellotge

    # Crea l'esdeveniment nou
	temps_esdeveniment = rellotge + UC(minim,maxim)
	tipus_esdeveniment = 'Fi consulta'
	nou_esdeveniment = temps_esdeveniment, tipus_esdeveniment

	# S'afegeix l'esdeveniment a la llista d'esdeveniments
	llista_esdeveniments += [nou_esdeveniment]

def esdeveniment_fi_consulta():
	global cua_1
	global cua_2
	global rellotge
	global temps_espera_consulta
	global temps_espera_proba
	global Npacients_consulta
	global Npacients_proba
	# Crea l'esdeveniment nou
	if random.random() < 0.8:
		if cua_2 == 0:
			afegir_esdeveniment_fi_proba()
			cua_2 += 1
			Npacients_proba += 1
		else:
			temps_espera_proba +=1
			cua_2 += 1
			Npacients_proba += 1
	
	if cua_1 > 2:
		afegir_esdeveniment_fi_consulta()
	# Actualitza comptadors
	cua_1 -= 1
	

def afegir_esdeveniment_fi_proba():
	global llista_esdeveniments
	global rellotge

    # Crea l'esdeveniment nou
	temps_esdeveniment = rellotge + triang(a,b,c)
	tipus_esdeveniment = 'Fi proba'
	nou_esdeveniment = temps_esdeveniment, tipus_esdeveniment

	# S'afegeix l'esdeveniment a la llista d'esdeveniments
	llista_esdeveniments += [nou_esdeveniment]

def esdeveniment_fi_proba():
	global cua_2
	global rellotge
	global temps_espera_consulta
	global temps_espera_proba
	global Npacients_consulta
	global Npacients_proba
	# Crea l'esdeveniment nou
	
	if cua_2 > 1:
		afegir_esdeveniment_fi_proba()
	# Actualitza comptadors
	cua_2 -= 1
	
# Funcio per veure si finalitza la simulacio 
def finalitzar_simulacio(esdeveniment):
	global maxim_temps 
	temps_esdeveniment = esdeveniment[0]
	#print(temps_esdeveniment >= maxim_temps)
	return (temps_esdeveniment >= maxim_temps )


# Funcio que obté el proper esdeveniment
def obtenir_esdeveniment_proper():
	global llista_esdeveniments
	llista_esdeveniments.sort(key=lambda tup: tup[0]) # El primer element de la tupla fa referencia al temps
	esdeveniment_proper = llista_esdeveniments[0]
	llista_esdeveniments = llista_esdeveniments[1:]
	return esdeveniment_proper

# Funcio impressions intermedies
def escriure_informacio(esdeveniment):
	print ('{0:5.1f} {1:15}'.format(esdeveniment[0], esdeveniment[1]) + 'Cua1='+str(cua_1)+' cua2='+str(cua_2))

#Aquí podem la semilla que volem
random.seed(2**19-1)
#print(str(Simular_Exercici_1()[0]).replace('.',','))
nsim=10
Nlotes=100
f=open('Resultados3.txt','w')
for j in range(Nlotes):
	lote_media=0
	for n in range(nsim):
		lote_media+= Simular_Exercici_2()
	lote_media= lote_media/nsim
	f.write(str(lote_media).replace('.',',')+'\n')
	#print('he escrit algo')
f.close()
