from tkinter import *
import mysql.connector
#######################################################################################
mydb=mysql.connector.connect(
host="127.0.0.1",
user="root",
password="",
database="covid"
)
mycursor=mydb.cursor()
#######################################################################################
pantalla1=Tk()
pantalla1.title("Base de datos COVID")
pantalla1.geometry('500x500')
#######################################################################################
def tamaulipas():
    pantalla5=Tk()
    pantalla5.title("Datos Tamaulipas")
    pantalla5.geometry('500x500')
    
    sql = "SELECT  \
        estados.estado AS uno, \
        datos.muertos,datos.infectados,datos.hospitalizados,datos.recuperados  AS dos \
        FROM estados \
        INNER JOIN datos ON estados.claveEs = datos.claveDa"
        
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    datos=[]
    for x in myresult:
        datos.append(x)

    a=datos[5]
    
    datosA=[]
    
    for y in a:
        datosA.append(y)
    
    estado=datosA[0]
    infectados=datosA[2]
    hospitalizados=datosA[3]
    muertos=datosA[1]
    recuperados=datosA[4]
    
    et5=Label(pantalla5,text=estado,fg="white", bg="green",font=("Arial",30)).place(x=145,y=60)
    et5a=Label(pantalla5,text="Infectados: "+str(infectados),font=("Arial",30)).place(x=70,y=180)
    et5b=Label(pantalla5,text="Hospitalizados: "+str(hospitalizados),font=("Arial",30)).place(x=70,y=240)
    et5c=Label(pantalla5,text="Muertos: "+str(muertos),font=("Arial",30)).place(x=70,y=300)
    et5d=Label(pantalla5,text="Recuperados: "+str(recuperados),font=("Arial",30)).place(x=70,y=360)
    
    pantalla5.mainloop()
    
    pantalla5.mainloop()
#######################################################################################
def sonora():
    pantalla5=Tk()
    pantalla5.title("Datos Sonora")
    pantalla5.geometry('500x500')
    
    sql = "SELECT  \
        estados.estado AS uno, \
        datos.muertos,datos.infectados,datos.hospitalizados,datos.recuperados  AS dos \
        FROM estados \
        INNER JOIN datos ON estados.claveEs = datos.claveDa"
        
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    datos=[]
    for x in myresult:
        datos.append(x)

    a=datos[4]
    
    datosA=[]
    
    for y in a:
        datosA.append(y)
    
    estado=datosA[0]
    infectados=datosA[2]
    hospitalizados=datosA[3]
    muertos=datosA[1]
    recuperados=datosA[4]
    
    et5=Label(pantalla5,text=estado,fg="white", bg="green",font=("Arial",30)).place(x=180,y=60)
    et5a=Label(pantalla5,text="Infectados: "+str(infectados),font=("Arial",30)).place(x=70,y=180)
    et5b=Label(pantalla5,text="Hospitalizados: "+str(hospitalizados),font=("Arial",30)).place(x=70,y=240)
    et5c=Label(pantalla5,text="Muertos: "+str(muertos),font=("Arial",30)).place(x=70,y=300)
    et5d=Label(pantalla5,text="Recuperados: "+str(recuperados),font=("Arial",30)).place(x=70,y=360)
    
    pantalla5.mainloop()
#######################################################################################
def colima():
    pantalla5=Tk()
    pantalla5.title("Datos Colima")
    pantalla5.geometry('500x500')
    
    sql = "SELECT  \
        estados.estado AS uno, \
        datos.muertos,datos.infectados,datos.hospitalizados,datos.recuperados  AS dos \
        FROM estados \
        INNER JOIN datos ON estados.claveEs = datos.claveDa"
        
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    datos=[]
    for x in myresult:
        datos.append(x)

    a=datos[3]
    
    datosA=[]
    
    for y in a:
        datosA.append(y)
    
    estado=datosA[0]
    infectados=datosA[2]
    hospitalizados=datosA[3]
    muertos=datosA[1]
    recuperados=datosA[4]
    
    et5=Label(pantalla5,text=estado,fg="white", bg="green",font=("Arial",30)).place(x=185,y=60)
    et5a=Label(pantalla5,text="Infectados: "+str(infectados),font=("Arial",30)).place(x=70,y=180)
    et5b=Label(pantalla5,text="Hospitalizados: "+str(hospitalizados),font=("Arial",30)).place(x=70,y=240)
    et5c=Label(pantalla5,text="Muertos: "+str(muertos),font=("Arial",30)).place(x=70,y=300)
    et5d=Label(pantalla5,text="Recuperados: "+str(recuperados),font=("Arial",30)).place(x=70,y=360)
    
    pantalla5.mainloop()
#######################################################################################
def sinaloa():
    pantalla5=Tk()
    pantalla5.title("Datos Sinaloa")
    pantalla5.geometry('500x500')
    
    sql = "SELECT  \
        estados.estado AS uno, \
        datos.muertos,datos.infectados,datos.hospitalizados,datos.recuperados  AS dos \
        FROM estados \
        INNER JOIN datos ON estados.claveEs = datos.claveDa"
        
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    datos=[]
    for x in myresult:
        datos.append(x)

    a=datos[2]
    
    datosA=[]
    
    for y in a:
        datosA.append(y)
    
    estado=datosA[0]
    infectados=datosA[2]
    hospitalizados=datosA[3]
    muertos=datosA[1]
    recuperados=datosA[4]
    
    et5=Label(pantalla5,text=estado,fg="white", bg="green",font=("Arial",30)).place(x=180,y=60)
    et5a=Label(pantalla5,text="Infectados: "+str(infectados),font=("Arial",30)).place(x=70,y=180)
    et5b=Label(pantalla5,text="Hospitalizados: "+str(hospitalizados),font=("Arial",30)).place(x=70,y=240)
    et5c=Label(pantalla5,text="Muertos: "+str(muertos),font=("Arial",30)).place(x=70,y=300)
    et5d=Label(pantalla5,text="Recuperados: "+str(recuperados),font=("Arial",30)).place(x=70,y=360)
    
    pantalla5.mainloop()
#######################################################################################
def nuevoleon():
    pantalla5=Tk()
    pantalla5.title("Datos Nuevo Leon")
    pantalla5.geometry('500x500')
    
    sql = "SELECT  \
        estados.estado AS uno, \
        datos.muertos,datos.infectados,datos.hospitalizados,datos.recuperados  AS dos \
        FROM estados \
        INNER JOIN datos ON estados.claveEs = datos.claveDa"
        
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    datos=[]
    for x in myresult:
        datos.append(x)

    a=datos[1]
    
    datosA=[]
    
    for y in a:
        datosA.append(y)
    
    estado=datosA[0]
    infectados=datosA[2]
    hospitalizados=datosA[3]
    muertos=datosA[1]
    recuperados=datosA[4]
    
    et5=Label(pantalla5,text=estado,fg="white", bg="green",font=("Arial",30)).place(x=145,y=60)
    et5a=Label(pantalla5,text="Infectados: "+str(infectados),font=("Arial",30)).place(x=70,y=180)
    et5b=Label(pantalla5,text="Hospitalizados: "+str(hospitalizados),font=("Arial",30)).place(x=70,y=240)
    et5c=Label(pantalla5,text="Muertos: "+str(muertos),font=("Arial",30)).place(x=70,y=300)
    et5d=Label(pantalla5,text="Recuperados: "+str(recuperados),font=("Arial",30)).place(x=70,y=360)
    
    pantalla5.mainloop()
#######################################################################################
def coahuila():
    pantalla5=Tk()
    pantalla5.title("Datos Coahuila")
    pantalla5.geometry('500x500')
    
    sql = "SELECT  \
        estados.estado AS uno, \
        datos.muertos,datos.infectados,datos.hospitalizados,datos.recuperados  AS dos \
        FROM estados \
        INNER JOIN datos ON estados.claveEs = datos.claveDa"
        
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    datos=[]
    for x in myresult:
        datos.append(x)

    a=datos[0]
    
    datosA=[]
    
    for y in a:
        datosA.append(y)
    
    estado=datosA[0]
    infectados=datosA[2]
    hospitalizados=datosA[3]
    muertos=datosA[1]
    recuperados=datosA[4]
    
    et5=Label(pantalla5,text=estado,fg="white", bg="green",font=("Arial",30)).place(x=175,y=60)
    et5a=Label(pantalla5,text="Infectados: "+str(infectados),font=("Arial",30)).place(x=70,y=180)
    et5b=Label(pantalla5,text="Hospitalizados: "+str(hospitalizados),font=("Arial",30)).place(x=70,y=240)
    et5c=Label(pantalla5,text="Muertos: "+str(muertos),font=("Arial",30)).place(x=70,y=300)
    et5d=Label(pantalla5,text="Recuperados: "+str(recuperados),font=("Arial",30)).place(x=70,y=360)
    
    pantalla5.mainloop()
#######################################################################################
#def editarestado():
    #pantalla4=Tk()
    #pantalla4.title("Editar datos")
    #pantalla4.geometry('500x500')
    #b4=Button(pantalla4,text="Coahuila",bg="yellow",fg="black",height='1',width='10',font=("Arial",20)).place(x=165,y=20)
    #b4a=Button(pantalla4,text="Nuevo Leon",bg="yellow",fg="black",height='1',width='10',font=("Arial",20)).place(x=165,y=100)
    #b4b=Button(pantalla4,text="Sinaloa",bg="yellow",fg="black",height='1',width='10',font=("Arial",20)).place(x=165,y=180)
    #b4c=Button(pantalla4,text="Colima",bg="yellow",fg="black",height='1',width='10',font=("Arial",20)).place(x=165,y=260)
    #b4d=Button(pantalla4,text="Sonora",bg="yellow",fg="black",height='1',width='10',font=("Arial",20)).place(x=165,y=340)
    #b4e=Button(pantalla4,text="Tamaulipas",bg="yellow",fg="black",height='1',width='10',font=("Arial",20)).place(x=165,y=420)
    #pantalla4.mainloop()
#######################################################################################   
def selestado():
    pantalla3=Tk()
    pantalla3.title("Menu estados")
    pantalla3.geometry('500x500')
    
    b3=Button(pantalla3,text="Coahuila",bg="orange",fg="white",height='1',width='10',font=("Arial",20),command=coahuila).place(x=165,y=20)
    b3a=Button(pantalla3,text="Nuevo Leon",bg="orange",fg="white",height='1',width='10',font=("Arial",20),command=nuevoleon).place(x=165,y=100)
    b3b=Button(pantalla3,text="Sinaloa",bg="orange",fg="white",height='1',width='10',font=("Arial",20),command=sinaloa).place(x=165,y=180)
    b3c=Button(pantalla3,text="Colima",bg="orange",fg="white",height='1',width='10',font=("Arial",20),command=colima).place(x=165,y=260)
    b3d=Button(pantalla3,text="Sonora",bg="orange",fg="white",height='1',width='10',font=("Arial",20),command=sonora).place(x=165,y=340)
    b3e=Button(pantalla3,text="Tamaulipas",bg="orange",fg="white",height='1',width='10',font=("Arial",20),command=tamaulipas).place(x=165,y=420)
    
    pantalla3.mainloop()
#######################################################################################
def ingresar():
    pantalla2=Tk()
    pantalla2.title("Estados")
    pantalla2.geometry('500x500')  
    
    #b2=Button(pantalla2,text="Modificar estado",bg="yellow",fg="black",height='2',width='15',font=("Arial",30),command=editarestado).place(x=75,y=80)
    b2a=Button(pantalla2,text="Seleccionar estado",bg="yellow",fg="black",height='2',width='15',font=("Arial",30),command=selestado).place(x=75,y=150)
    
    pantalla2.mainloop()
#######################################################################################  
f1=PhotoImage(file='fc1.png')
f1a=Label(pantalla1,image=f1).place(x=0,y=0)  
et1=Label(pantalla1,text="Estadisiticas SARS CoV 2",fg="white", bg="blue",font=("Arial",30)).place(x=18,y=70)
b1=Button(pantalla1,text="Ingresar",bg="black",fg="white",height='2',width='10',font=("Arial",30),command=ingresar).place(x=135,y=230)
pantalla1.mainloop()
#######################################################################################