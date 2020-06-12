while True:
	#Asignación de los valores de n y m. Creación de la lista de vértices
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

	n= int(n)
	m= int(m)
	#En este for llenamos la listaVertices con los valores 1...(n-1)

	for i in range(n):
		listaVertices.append(i)

	 
	print(n,m)

	#Asignación de los puntos de inicio y destino

	entrada1=input("Ingrese S y D: ")

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

	s= int(s)
	d= int(d)

	print(s,d)

	for i in range(n-1):
		listaTemporal.append(0)
		listaFinal.append(0)

	listaTemporal.insert(s,0)
	listaFinal.insert(s,0)

	print(listaTemporal[:])
	print(listaFinal[:])

	#Asignación de los caminos establecidos
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
		
		diccionarioAristas[u+" "+v]=int(p)

	#Algoritmo#################################
	verticeActivo=str(s)
	diccionarioAdyacentes={}
	aux=""
	contador=0
	aux2=""


	print(diccionarioAristas.keys())
	
	#Mira si un vértice es adyacente
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
				print(i + " Es un vértice adyacente")
				break
			else:
				print(i+ " no es adyacente")
				break

	menor=0
	for i in range(n-1):
		if listaTemporal[i]>0:
			

	print(menor)


	
	print(diccionarioAdyacentes)
	print(listaTemporal[:])	





	#Algoritmo#################################




print(diccionarioAristas)


	
	


