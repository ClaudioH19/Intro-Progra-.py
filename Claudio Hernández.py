#versión python: 3.70
#libreria gráfica: TURTLE
#guardar este archivo python junto al archivo "correcaminos.gif"
import math
import time
from tkinter import messagebox
import turtle
import os
import tkinter
def velocidades_del_proyectil(Vi,a):
    #Propósito: descompone la velocidad inicial en sus componentes rectangulares 
    #Entradas: flotantes: Vi: velocidad inicial, a:angulo
    #Salida: flotantes: Vy, Vy componentes rectangulares de Vi

    #radianes ---> grados
    a=a*(2*math.pi/360)
    #calculo velocidades iniciales
    Vy=Vi*math.sin(a)
    Vx=Vi*math.cos(a)
    return  Vy,Vx

def coordenadas_proyectil(Cx,Cy,Vy,Vx,t):
    #Propósito: Calcula coordenadas de la bala en un instante t
    #Entradas: flotantes: Cx,Cy,Vy,Vx, int: t
    #Salida: flotantes: Px,Py: coordenadas de la bala

    Px= (Cx*5+Vx*t)/5
    Py= (Cy*5+Vy*t-4.8*t**2)/5
    return Px,Py

def tiempo(t):
    #Propósito: hace de contador de tiempo en intervalos discretos
    #Entradas: int: t
    #Salida: t: tiempo

    t+=1
    return t

def dstnc_c(Px,Py,Rx,Ry,intentos,dcercano):
    #Propósito: Calcula distancia bala-centro de correcaminos para cuando hay impacto 
    #Entradas: flotantes:Px,Py,Rx,Ry
    #Salida: flotantes: dcercano: distancia más cercana 

    distancia=math.sqrt(((Px-Rx)**2)+((Py-Ry)**2))
    if intentos==1:
        dcercano=distancia

    if distancia<=dcercano:
        dcercano=distancia
    return dcercano

def dstnc_l(Px,Py,Rx,Ry,intentos,dlejano):
    #Propósito: Calcula distancia bala-centro de correcaminos para cuando no hay impacto 
    #Entradas: flotantes:Px,Py,Rx,Ry
    #Salida: flotantes: dlejano: distancia más lejana

    distancia=math.sqrt(((Px-Rx)**2)+((Py-Ry)**2))
    if intentos==1:
        dlejano=distancia

    if distancia>=dlejano:
        dlejano=distancia
    return dlejano




#---------------------------------------------FIGURAS--------------------------------------------------------
def fig_cañon(Cx,Cy,a):
    #Propósito: dibuja el cañon
    #Entradas: flotantes: Cx,Cy: coordenadas del cañon, a: ángulo
    #Salida: dibujo del cañon

    turtle.penup()
    turtle.setx(Cx)
    turtle.sety(Cy)
    turtle.pendown()
    turtle.color("gray")
    turtle.goto(Cx,Cy+20)
    turtle.begin_fill()
    turtle.left(a)
    #MEDIDAS
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.end_fill()
    turtle.penup()
    turtle.home()

    turtle.color("brown")
    turtle.setx(Cx)
    turtle.sety(Cy)
    turtle.pendown()
    turtle.circle(20)
    turtle.penup()
    turtle.goto(Cx,Cy+20)
    i=1
    while i<=8:
        turtle.pendown()
        turtle.forward(20)
        turtle.backward(20)
        turtle.right(45)
        i+=1


def fig_bala(Px,Py):
    #Propósito: dibuja la bala
    #Entradas: flotantes: Px,Py: coordenadas de la bala
    #Salida: dibujo de la bala

    turtle.penup()
    turtle.setx(Px)
    turtle.sety(Py)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    turtle.penup()

def borrar_bala(Px,Py):
    #Propósito: borra la bala
    #Entradas: flotantes: Px,Py: coordenadas de la bala
    #Salida: dibujo de la bala con el color de fondo

    turtle.penup()
    turtle.setx(Px)
    turtle.sety(Py)
    turtle.pendown()
    turtle.color("Light blue")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    turtle.color("black")
    turtle.dot(5)
    turtle.penup()

def ejes_cambiados(eje_x,eje_y):
    #Propósito: crea nuevos ejes de coordenadas
    #Entradas: flotantes: eje_x,eje_y:coordenadas de nuevos ejes
    #Salida: dibujo de los nuevos ejes coordenados

    turtle.penup()
    turtle.setx(eje_x)
    turtle.sety(eje_y)
    turtle.pendown()
    turtle.forward(1000000)
    turtle.backward(2000000)
    turtle.penup()
    turtle.setx(eje_x)
    turtle.sety(eje_y)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(1000000)
    turtle.backward(2000000)
    turtle.penup()
    turtle.home()
    turtle.setx(eje_x)
    turtle.sety(eje_y)
    turtle.penup()

def ejes_originales():
    #Propósito: crea los verdaderos ejes de coordenadas
    #Entradas: ----
    #Salida: dibujo de los ejes coordenados

    turtle.penup()
    turtle.color("red")
    turtle.home()
    turtle.pendown()
    turtle.goto(1000000,0)
    turtle.goto(-2000000,0)
    turtle.home()
    turtle.goto(0,1000000)
    turtle.goto(0,-2000000)
    turtle.penup()
    turtle.color("black")
    turtle.home()
    turtle.penup()

def correcaminos(Rx,Ry,ruta):
    #Propósito: copia el gif del correcaminos
    #Entradas: flotantes: Rx,Ry str: ruta
    #Salida: impresión del correcaminos

    turtle.penup()
    turtle.goto(Rx,Ry+20)#el +20 es estetico 
    turtle.showturtle()
    turtle.addshape("correcaminos.gif")
    turtle.shape("correcaminos.gif")
    turtle.clone()
    turtle.hideturtle()


def ambiente(eje_x,eje_y):
    #Propósito: dibuja el fondo
    #Entradas: flotantes: eje_x,eje_y:coordenadas de los ejes
    #Salida: dibujo del fondo

    turtle.penup()
    turtle.goto(eje_x-1000000,eje_y)
    turtle.pendown()
    turtle.begin_fill()
    i=1
    while i<=2:
        turtle.color("Brown")
        turtle.forward(2000000)
        turtle.right(90)
        turtle.forward(1000000)
        turtle.right(90)
        i+=1
    turtle.end_fill()
    i=1
    turtle.begin_fill()
    while i<=2:
        turtle.color("Light blue")
        turtle.forward(2000000)
        turtle.left(90)
        turtle.forward(1000000)
        turtle.left(90)
        i+=1
    turtle.end_fill()

def torre(eje_y,Cx,Cy,Rx,Ry):
    #Propósito: dibuja una "torre" para las fig en altura
    #Entradas: flotantes: eje_y,Cx,Cy,Rx,Ry
    #Salida: dibujo de la torre

    if Cy>eje_y:
        turtle.color("gray")
        turtle.begin_fill()
        turtle.penup()
        turtle.goto(Cx,Cy)
        turtle.goto(Cx+50,Cy)
        turtle.goto(Cx+50,eje_y)
        turtle.goto(Cx-50,eje_y)
        turtle.goto(Cx-50,Cy)
        turtle.goto(Cx,Cy)
        turtle.end_fill()
    if Ry>eje_y:
        turtle.color("gray")
        turtle.begin_fill()
        turtle.penup()
        turtle.goto(Rx,Ry)
        turtle.goto(Rx+50,Ry)
        turtle.goto(Rx+50,eje_y)
        turtle.goto(Rx-50,eje_y)
        turtle.goto(Rx-50,Ry)
        turtle.goto(Rx,Ry)
        turtle.end_fill()

def h_max(max_x,max_y,eje_y):
    #Propósito: dibuja una línea recta desde el punto más alto hasta el eje y
    #Entradas: flotantes: eje_y,max_x,max_y
    #Salida: dibujo de una línea recta
 
    turtle.penup()
    turtle.setx(max_x)
    turtle.sety(max_y)
    turtle.write("Punto máximo")
    turtle.clone()
    turtle.color("black")
    turtle.pendown()
    turtle.goto(max_x,eje_y)
    turtle.penup()


#PROGRAMA-------------------------------------------------------------
#Cargando imagenes----------------------------------------------------------------------
ruta=os.path.dirname(__file__)
os.chdir(ruta)
print(ruta)


#ESTRUCTURA
RUN=True
#Comprobando imagen
if os.access("correcaminos.gif",os.F_OK)==False:
    print("ERROR LA IMAGEN DEL CORRECAMINOS NO SE ENCUENTRA EN LA MISMA UBICACIÓN DEL ARCHIVO PYTHON")
    RUN=False
intentos=1
dcercano=0
dlejano=0
aciertos=0
while RUN:
    print("------------------------------------------------------------------------")
    print("Intento: ",intentos)
    print("Disparo más cercano (al centro del obj.): ",dcercano)
    print("Disparo más lejano  (al centro del obj.): ",dlejano)
    print("Aciertos: ",aciertos)
    #Variables
    t=0
    Cx=0
    Cy=0
    Rx=0
    Ry=0
    a=0
    Vi=0
    eje_x=0
    eje_y=0
    g=9.8
    bandera=0
    #ENTRADAS--------------------------------------------------------------
    #ESCALA 5:1
    #Posible cambio
    respuesta=int(input("¿Desea cambiar la posición de los ejes?(1->Sí|0->No): "))
    if respuesta==1:
        eje_x=float(input("Ingrese coordenada del eje x: "))
        eje_y=float(input("Ingrese coordenada del eje y: "))

    #coordenadas correcaminos
    Rx=float(input("Ingrese coordenada x del correcaminos(mts)[Recomendación:900]: "))/5+eje_x
    Ry=float(input("Ingrese coordenada y del correcaminos(mts)[Recomendación:0]: "))/5+eje_y

    #coordenadas cañón
    Cx=float(input("Ingrese coordenada x del cañón(mts)[Recomendación:0]: "))/5+eje_x
    Cy=float(input("Ingrese coordenada y del cañón(mts)[Recomendación:0]: "))/5+eje_y

    #velocidad inicial
    Vi=float(input("Ingrese velocidad inicial del proyectil(mts/s)[Recomendación:100]: "))


    #ángulo
    a=float(input("Ingrese el ángulo del cañón(en grados)[Recomendación:60]: "))

    #REVISANDO ERRORES-----------------------------------------------------------------------
    if (a>180) or (a<0) or (Vi<0) or (Ry<eje_y) or (Cy<eje_y):
        print("Error en alguno de los datos intente nuevamente.")
        a=0
        Vi=0
        Px=0
        Py=0
        Ry=0
        Cy=0
    
    #Preparatorias para dibujar------------------------------------------------------------
    #CONFIG INICIAL TURTLE
    turtle.setup(0.99,0.9,0,0)
    turtle.hideturtle()
    turtle.speed(0)
    turtle.screensize(1000000,1000000)
    turtle.delay(5)

    #CÁLCULOS INICIALES-------------------------------------------------------------------
    Vy,Vx=velocidades_del_proyectil(Vi,a)

    #DIBUJAR--------------------------------------------------------------------------------
    #dibujar ambiente,ejes,cañon,correcaminos
    ambiente(eje_x,eje_y)
    ejes_originales()
    ejes_cambiados(eje_x,eje_y)
    fig_cañon(Cx,Cy,a)
    correcaminos(Rx,Ry,ruta)
    torre(eje_y,Cx,Cy,Rx,Ry)


    #---------------------------------------INICIO VUELO-------------------------------------
    Px=Cx
    Py=Cy
    incerteza_x = abs(Px-Rx) #el absoluto para cubrir 60 izq y 60 der
    incerteza_y = (Py-Ry)
    #--------------------COMPROBAR SI IMPACTA AL INICIO VUELO----------------------
    #INCERTEZA: tamaño fig aprox.
    if (incerteza_x<=60) and (incerteza_y<=50) and (incerteza_y>=0):
        bandera=1
        print("El proyectil dio al objetivo en el segundo: ",t)

    #----------------------------------------VUELO-------------------------------------------
    bandera_2=True
    alt_y=Py
    alt_x=Px
    t_max=0
    while (bandera_2==True) and (bandera!=1): #MIENTRAS ESTÉ ARRIBA DEL SUELO Y NO HAYA IMPACTADO 
    #dibujos-------------------------------
        fig_cañon(Cx,Cy,a)
        fig_bala(Px,Py)
        borrar_bala(Px,Py)
    #cálculos------------------------------
        t=tiempo(t)
        Px,Py=coordenadas_proyectil(Cx,Cy,Vy,Vx,t)
        if Py>alt_y: #verifica vértice
            alt_y=Py
            alt_x=Px
            t_max=t
        incerteza_x = abs(Px-Rx) #el absoluto para cubrir 60 izq y 60 der
        incerteza_y = (Py-Ry)
    #--------------------COMPROBAR SI IMPACTA DURANTE EL VUELO----------------------
    #INCERTEZA: tamaño fig aprox.
        if (incerteza_x<=60) and (incerteza_y<=50) and (incerteza_y>=0):
            bandera=1
            print("El proyectil dio al objetivo en el segundo: ",t)
    #-------------------CONDICION PARA SEGUIR EN EL BUCLE----------------------------
        if Py<=eje_y:
            bandera_2=False

    #-------------------------------------FIN VUELO--------------------------------------------
    h_max(alt_x,alt_y,eje_y)
    alt = round(abs(alt_y-eje_y)*5,1)

    alt_str= str(alt)
    t_max_str= str(t_max)
    alcance_str= str(round(abs(Px-Cx)*5,1))
    t_str= str(t)
    messagebox.showinfo("Información", "Altura máxima (mts): " + alt_str + " en t=" + t_max_str +"\n" + "Alcance (mts): "+ alcance_str + " en t=" + t_str)

    correcaminos(Rx,Ry,ruta)
    fig_bala(Px,Py)
    time.sleep(5)

    #----------------------------------COMPROBAR IMPACTO AL FIN VUELO----------------------
    incerteza_x = abs(Px-Rx)
    incerteza_y = (Py-Ry)
    if (incerteza_x<=60) and (incerteza_y<=50) and (incerteza_y>=0):
        bandera=1





    #----------------------------------COMPROBAR ESTADO DE LA BANDERA 1----------------------
    #está escalado para pixeles hay que multiplicar por 5 para volver a metros
    if bandera==1:
        resultado="EN EL BLANCO!"
        dcercano= dstnc_c(Px,Py,Rx,Ry,intentos,dcercano)*5
        aciertos+=1
    else:
        resultado="Tiro fallido"
        dlejano= dstnc_l(Px,Py,Rx,Ry,intentos,dlejano)*5
    #----------------------------------RETORNO PREGUNTA------------------------------------
    intentos+=1
    print("MIRE LA PANTALLA DE TURTLE PARA CONTINUAR")
    otro_intento=turtle.numinput(resultado,"¿Desea intentar de nuevo? (1->Si|0->No")
    if otro_intento==1:
        turtle.clearscreen()
        RUN=True   
    else:
        RUN=False

