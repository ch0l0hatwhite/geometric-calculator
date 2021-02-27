def ban():
  print("\033[36m")
  print("""
   **********************
	1) Triangulo 
	2) Cuadrado
	3) Rectangulo
	4) Circulo
	5) Rombo
	6) Pentagono
	7) Hexagono
	8) Trapecio
	9) Paralelogramo 
   **********************""")
   
  print("")
 		
def triangulo():
   print("\033[32m")
   print ("""
                 ______
                /     /\
               /     /##\
              /     /####\
             /     /######\
            /     /########\
           /     /##########\
          /     /#####/\#####\
         /     /#####/++\#####\
        /     /#####/++++\#####\
       /     /#####/\+++++\#####\
      /     /#####/  \+++++\#####\
     /     /#####/    \+++++\#####\
    /     /#####/      \+++++\#####\
   /     /#####/        \+++++\#####\
  /     /#####/__________\+++++\#####\
 /                        \+++++\#####\
/__________________________\+++++\####/
\+++++++++++++++++++++++++++++++++\##/
 \+++++++++++++++++++++++++++++++++\/
  ``````````````````````````````````
   """)
   print("") 
   bdt=float(input("base del triangulo > "))
   print("")
   adt=float(input("altura del triangulo> "))
   print("")
   l1=float(input("Lado 1 del triangulo > ")) 
   print("")
   l2=float(input("Lado 2 del triangulo > "))
   print("")
   res=(bdt*adt)
   res1=(res/2)
   pe=(bdt + l1 + l2)
   print("El Area Del Triangulo Es : ",+res1,"cm")
   print("")
   print("El Perimetro De El Triangulo Es : ",+pe ,"cm")
   
      		

	
def cuadro():
	
	print("") 
	print("\033[33m")
	lc1=float(input("Lado 1 > "))
	print("")
	lc2=float(input("Lado 2 > "))
	print("")
	lc3=float(input("Lado 3 > "))
	print("")
	lc4=float(input("Lado 4 > "))
	l12=(lc1*lc2)
	pec=(lc1 + lc2 + lc3 + lc4)
	print("")
	print("El Area Del Cuadro Es : ",+l12 ,"cm")
	print("")
	print("El Perimetro Del Cuadrado Es :",+pec ,"cm")
					
def Rectangulo():
	print("")
	print("\033[34m")
	baser=float(input("Base > "))
	print("")
	alturar=float(input("Altura > "))
	print("")
	baserr=(baser*alturar)
	perr=(baser + baser + alturar + alturar)
	print("El Area De El Rectangulo Es :",+baserr ,"cm")
	print("")
	print("El Perimetro Del Rectangulo Es :",+perr ,"cm")
	
def circulo():
	print("")
	print("\033[35m")
	diam=float(input("Diametro del circulo > "))
	print("")
	cirr=(3.1416*diam/2**2)
	perc=(3.1416*diam)
	print("El Area Del Circulo Es : ",+cirr ,"cm")
	print("")
	print("El Perimetro De El Circulo Es : ",+perc ,"cm")
				


def Rombo():
	print("")
	print("\033[36m")
	dma=float(input("Diagonal mayor Del Rombo > "))
	print("")
	dme=float(input("Diagonal menor Del Rombo > "))
	print("")
	dade=(dma*dme/2)
	pder=( dma*2 + dme*2)
	print("El Area De El Rombo Es : ",+dade ,"cm")
	print("")
	print("El Perimetro De El Rombo Es : ",+pder ,"cm")
	
def pentagono():
	print("")
	print("\033[37m")
	lado=float(input("Lado de el pentagono > "))
	print("")
	apo=float(input("Apotema de el pentagono > "))
	resp=(lado*5*apo/2)
	penp=(lado*5)
	print("")
	print("El Area De El Pentagono Es : ",+resp ,"cm")
	print("")
	print("El Perimetro Del Pentagono Es :",+penp ,"cm")
	
def Hexagono():
	print("")
	print("\033[38m")
	lad6=float(input("Medida De Un Lado Del Hexagono > "))
	print("")
	tema=float(input("Apotema De Un lado De El Hexagono > "))
	hex=(lad6*6)
	print("")
	print("El Perimetro De El Hexagono Es : " ,+hex ,"cm")
	apot=(hex*tema/2)
	print("")
	print("El Area De El Hexagono Es :",+apot ,"cm")
	print("")
	
def Trapecio():
	print("")
	print("\033[39m")
	basa=float(input("Base Mayor Del Trapecio > "))
	print("")
	basm=float(input("Base Menor Del Trapecio > "))
	print("")
	tua=float(input("Altura De El Trapecio > "))
	print("")
	lt1=float(input("Medida De lado Derecho Del Trapecio > "))
	print("")
	lt2=float(input("Medida De Lado Izquierdo De El Trapecio > "))
	print("")
	tra=(basa+basm*tua/2)
	pert=( basa+basm+lt1+lt2)
	print("El Area De El Trapecio Es : ",+tra ,"cm")
	print("")
	print("El Perimetro De El Trapecio Es : ",pert ,"cm")
	
	
def Paralelogramo():
	print("")
	print("\033[31m")
	bs=float(input("Base De El Paralelogramo > "))
	print("")
	alp=float(input("Altura Del Paralelogramo > "))
	print("")
	par=(bs*alp)
	pedp=( bs+alp*2)
	print("El Area Del Paralelogramo Es : ",+par ,"cm")
	print("")
	print("El Perimetro Del Paralelogramo Es : ",+pedp ,"cm")
	
ban()

menu=int(input("Escribe Un Numero   Del 1 al 9 >"))

if menu == 1:
	triangulo()
	
if menu == 2:
	cuadro()
	
if menu == 3:
	Rectangulo()
	
if menu == 4:
	circulo()
	
if menu == 5:
	Rombo()
	
if menu == 6:
	pentagono()
	
if menu == 7:
	Hexagono()
	
if menu == 8:
	Trapecio()
	
if menu == 9:
	Paralelogramo()	
