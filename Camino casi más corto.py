while True:
	#Asignación de los valores de n y m. Creación de la lista de vértices
	entrada=input("Ingrese N y M: ")
	if entrada=="0 0":
		break

	listaVertices=[]
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

	#Asignación de los caminos establecidos
	listaAristas=[]
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
		
		arista=u+" "+v+" "+p
		listaAristas.append(arista)
		arista=""


print(listaAristas[:])


	
	


