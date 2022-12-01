'''
Autores:
Esta librería esta diseñada y trabajada en colaboración con los alumnos 
de la primera Edición de Big Data Tenerife el 01 de diciembre de 2022.

Ibon Reinoso Isasi - https://ibonreinoso.com/
BigBayData.com - https://www.bigbaydata.com/

'''

import random

def seleccionarYActualizar(tematica,listaAlumnos):
    
    alumno1 = random.choice(listaAlumnos)
    listaAlumnos.remove(alumno1)
    print('Alumno seleccionado:',alumno1)


def asignarTemasAAlumnos(tematica, listaAlumnos, numeroGrupos):
	for tematica in listaTematicas:
	    if(len(listaAlumnos) >= numeroGrupos):
	    	for i in (0,numeroGrupos + 1):
	        	seleccionarYActualizar(tematica, listaAlumnos)
	    else:
	    	print('TEMATICA:',tematica)
	    	print(listaAlumnos)

'''
listaTematicas = [ 'Regresión Lineal', 'Regresión Logística', 'Naive Bayes', 'Supervisado: Knn', 'no Supervisado: KMeans' ]
listaAlumnos = [1,2,3,4,5,6,7,8,9,10,11,24,575,211,7878,112,232]

asignarTemasAAlumnos(listaTematicas, listaAlumnos, 6)
'''

def calcularMedia(poblacion):
    acum = 0
    #for i in poblacion:
    #    acum += i
    #print( sum(lista)/len(lista) )
    resultado = sum(poblacion)/len(poblacion)
    #print('MEDIA:', resultado)
    return resultado

def calcularMediana(poblacion):
    ordenado = sorted(poblacion)
    resultado = 0
    if(len(poblacion) % 2 == 0):
        resultado = (ordenado[int(len(poblacion)/2) - 1] + ordenado[int(len(poblacion)/ 2)])/2
    else:
        resultado = ordenado[int(len(poblacion)/2)]
    #print('MEDIANA:',resultado)
    return resultado

def calcularModa(poblacion):
    resultado = []
    vecesRepetido = []
    for o in poblacion:
        if poblacion.count(o) > 1:
            vecesRepetido.append([poblacion.count(o), o])
        if vecesRepetido == []:
            resultado = poblacion
        else:
            resultado = max(vecesRepetido)[1]
    #print('MODA:',resultado)
    return resultado

def calcularVarianza(poblacion):
    media = calcularMedia(poblacion)
    resultado = 0
    for i in poblacion:
        resultado = resultado + (i - media) ** 2
    resultado /= len(poblacion) - 1
    resultado **= 0.5
    #print('VARIANZA:',resultado)
    return resultado	

def NormalizarDatos(data):
	'''Devuelve una lista de datos normalizados'''
	datosNormalizados = []
	maximo = max(data)
	minimo = min(data)
	for i in data:
		normalizedValue = (i - minimo)/(maximo - minimo)
		datosNormalizados.append(normalizedValue)
	return datosNormalizados

def EstadisticaDescriptiva(poblacion):
	'''
	A partir de una lista de datos (numérica) obtener 
	Medidas de Centro: Media, Moda, Mediana
	Medidas de Dispersion: Desv. Tip. y Variaza
	'''
	media = calcularMedia(poblacion)
	moda = calcularModa(poblacion)
	mediana = calcularMediana(poblacion)
	desvEstandar = calcularVarianza(poblacion)
	Variaza = desvEstandar ** 2
	print('Población:')
	print(poblacion)
	print('Datos Estadísticos (Medidas de Centro):')
	print('Media | Moda | Mediana') 
	print('Media:', round(media,4))
	print('Moda:', moda)
	print('Mediana:', round(mediana,4))
	print('Datos Estadísticos (Medidas de Dispersión):')
	print('DesvEstandar | Variaza')
	print('Desv. Estándar:', round(desvEstandar,4))
	print('Varianza:', round(desvEstandar,4))

poblacion = [1,3,4,5,6,7,8,9,10]
EstadisticaDescriptiva(poblacion)

def ValidacionCruzada(p_test, datos):
	'''
	A partir de unos datos, obtenemos la parte de test y train separados
	'''
