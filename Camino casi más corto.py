def algoritmo(s,diccionarioAdyacentes,diccionarioAristas,listaFinal,listaTemporal,verticeInicial):
	listaCompleta=False
	contadorCero=0
	for i in listaTemporal:
		if i==0:
			contadorCero+=1
		
	if contadorCero==1:
		listaCompleta=True


	verticeActivo=str(s)
	aux=""
	contador=0
	aux2=""
	menor=0
	indexMenor=None



	for i in diccionarioAristas.keys():	
		aux=""
		for j in i:
			aux2=""
			contador=0

			if j!=" ":
				aux=aux+j
			elif aux==verticeActivo:

				for k in i:
					if k==" ":
						contador+=1
					elif contador==1:
						aux2=aux2+k
				diccionarioAdyacentes[aux2]=diccionarioAristas[i]
				listaTemporal[int(aux2)]=diccionarioAristas[i]
				if menor==0:
					menor=diccionarioAristas[i]
					indexMenor=int(aux2)
				else:
					if diccionarioAristas[i]<menor:
						menor=diccionarioAristas[i]
						indexMenor=int(aux2)
				print(i + " Es un vértice adyacente")
				break
			else:
				print(i+ " no es adyacente")
				break
			
	#listaFinal[indexMenor]=menor


	print(listaTemporal[:])
	



	pesoMenor=None
	nuevoVertice=None
	posicion=0

	for i in listaTemporal:
		if listaFinal[posicion]==None:
			if i!=0:
				if pesoMenor==None:
					pesoMenor=i
					nuevoVertice=posicion
				else:					
					if i<pesoMenor:
						pesoMenor=i
						nuevoVertice=posicion
		else:
			nuevoVertice=indexMenor
		posicion+=1

	listaFinal[nuevoVertice]=listaTemporal[nuevoVertice]
	print(listaFinal[:])



	print("El nuevoVertice es: " + str(nuevoVertice))

	if listaCompleta:
		print("Terminó")
	else:
		algoritmo(nuevoVertice,diccionarioAdyacentes,diccionarioAristas,listaFinal,listaTemporal,verticeInicial)










while True:
	#Asignación de los valores de n y m. Creación de la lista de vértices, temporal y final
	entrada=input("Ingrese N y M: ")
	if entrada=="0 0":
		break

	listaVertices=[]
	listaTemporal=[]
	listaFinal=[]
	n=""
	m=""
	c=0
	c1=0

	for i in entrada:
		if c==0:
			if(i!=" "):
				n=n+i
			else :
				c+=1
		else :
			if(i!=" "):
				m=m+i

	n= int(n)	#Conversión a enteros de N y M
	m= int(m)

	for i in range(n):#En este for llenamos la listaVertices con los valores 1...(n-1)
		listaVertices.append(i)

	 
	#print(n,m)  Imprime los valores de n y m

	entrada1=input("Ingrese S y D: ")#Asignación de los puntos de inicio y destino

	s=""
	d=""
	c=0

	for i in entrada1:
		if c==0:
			if(i!=" "):
				s=s+i
			else :
				c+=1
		else :
			if(i!=" "):
				d=d+i

	s= int(s)#Conversión a enteros de S y D
	d= int(d)

	#print(s,d) Imprime S y D

	for i in range(n-1):#Iniciliza las listas Temporal y Final con ceros
		listaTemporal.append(0)
		listaFinal.append(None)

	listaTemporal.insert(s,0)
	listaFinal.insert(s,0)#En las posiciones S de las listas temporal y final pone un cero

	#print(listaTemporal[:])
	#print(listaFinal[:]) Imprime las listas temporal y final con sólo los ceros en la posición S

	############### Asignación de las aristas #####################################

	diccionarioAristas={}
	for i in range(m):
		u=""
		v=""
		p=""
		c=0
		entrada2=input("Ingrese las aristas y el peso: ")

		for i in entrada2:
			if c==0:
				if i!=" ":
					u=u+i
				else:
					c+=1
			elif c==1:
				if i!=" ":
					v=v+i
				else:
					c+=1
			else :
				p=p+i
		
		diccionarioAristas[u+" "+v]=int(p)#Al diccionario de aristas le da una clave de "u v" y un valor entero p

	############### Fin de asignación de las aristas #####################################

	diccionarioAdyacentes={}
	
	
	algoritmo(s,diccionarioAdyacentes,diccionarioAristas,listaFinal,listaTemporal,s)

	
	print(diccionarioAdyacentes)
	print(listaTemporal[:])	
	print(listaFinal[:])





	#####################Fin algoritmo #################################




#print(diccionarioAristas) Imprime todas las aristas del grafo


	


