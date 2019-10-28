from kanren import *
import numpy as np
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter.ttk as ttk

#Definir las bases del conocimiento
Quintas = Relation()
TerceraM = Relation()
Terceram = Relation()
SegundaM = Relation()
Segundam = Relation()
#Quintas
facts(Quintas,
    ("C","G"),
    ("G","D"),
    ("D","A"),
    ("A","E"),
    ("E","B"),
    ("B","F#"),
    ("F#","C#"),
    ("Gb","Db"),
    ("C#","G#"),
    ("Db","Ab"),
    ("G#","D#"),
    ("Ab","Eb"),
    ("D#","A#"),
    ("Eb","Bb"),
    ("A#","F"),
    ("Bb","F"),
    ("F","C"))
#TerceraMayor
facts(TerceraM,
    ("C","E"),
    ("C#","F"),
    ("Db","F"),
    ("D","F#"),
    ("D#","G"),
    ("Eb","G"),
    ("E","G#"),
    ("F","A"),
    ("F#","A#"),
    ("Gb","Bb"),
    ("G","B"),
    ("G#","C"),
    ("Ab","C"),
    ("A","C#"),
    ("A#","D"),
    ("Bb","D"),
    ("B","D#"))
#TerceraMenor
facts(Terceram,
    ("C","Eb"),
    ("C#","E"),
    ("Db","E"),
    ("D","F"),
    ("D#","F#"),
    ("Eb","Gb"),
    ("E","G"),
    ("F","Ab"),
    ("F#","A"),
    ("Gb","A"),
    ("G","Bb"),
    ("G#","B"),
    ("Ab","B"),
    ("A","C"),
    ("A#","C#"),
    ("Bb","Db"),
    ("B","D"))

#Segunda Mayor
facts(SegundaM,
    ("C","D"),
    ("C#","D#"),
    ("Db","Eb"),
    ("D","E"),
    ("D#","F"),
    ("Eb","F"),
    ("E","F#"),
    ("F","G"),
    ("F#","G#"),
    ("Gb","Ab"),
    ("G","A"),
    ("G#","A#"),
    ("Ab","Bb"),
    ("A","B"),
    ("A#","C"),
    ("B","C#"))

#Segunda Menor
facts(Segundam,
    ("C","C#"),
    ("C#","D"),
    ("Db","D"),
    ("D","Eb"),
    ("D#","E"),
    ("Eb","E"),
    ("E","F"),
    ("F","Gb"),
    ("F#","G"),
    ("Gb","G"),
    ("G","G#"),
    ("G#","A"),
    ("Ab","A"),
    ("A","A#"),
    ("A#","B"),
    ("B","C"))

#Variables
T = var()
SMaj = var()
S = var()
SM = var()
Sm = var()
TM = var()
Tm = var()
Q = var()


def TriadaMayor(T):
    return np.array(run(1,(T,TM,Q),TerceraM(T,TM),Terceram(TM,Q)))[0]

def InferirTerceraMayor(T):
    return np.array(run(1,(T,TM),SegundaM(T,SM),SegundaM(SM,TM)))[0]

def TriadaMenor(T):
    return np.array(run(1,(T,Tm,Q),Terceram(T,Tm),TerceraM(Tm,Q)))[0]

def SetimaMayor(T):
    return np.array(run(1,(T,SMaj),Segundam(SMaj,T)))[0]

def SetimaMenor(T):
    return np.array(run(1,(T,S),SegundaM(S,T)))[0]

def CuatriadaMayorMaj7(T):
    return np.array(zip(TriadaMayor(T),SetimaMayor(T))).flatten() 


def init(self):
    Notas = ["C","C#","Db","D","D#","Eb","E","F","F#","Gb","G","G#","Ab","A","A#","Bb","B"]
    Calidad = ["Mayor", "Menor", "Setima", "Setima Mayor"]

    l_notas = Label(self,text = "Nota", fg = "black", bg = "white").place(x = 10, y = 10)
    cbx_notas = ttk.Combobox(self, values = Notas, textvariable = notas).place(x = 10, y = 30)
    l_calidad = Label(self,text = "Calidad", fg = "black", bg = "white").place(x = 10, y = 55)
    cbx_calidad = ttk.Combobox(self, values = Calidad, textvariable = calidad).place(x = 10, y = 75)
    l_acorde = Label(self,text = "Acrode", fg = "black", bg = "white").place(x = 170, y = 10)
    #Notacion = notas.get() + ("" if calidad.get() == "Mayor" else "m")
    l_notacion = Label(self,textvariable = notacion, fg = "black", bg = "white").place(x = 170, y = 30)
    bttn_gen = Button(self,text = "Generar Acorde", command = Generar).place(x = 170, y = 55)
    l_acordeFinal = Label(self,textvariable = AcordeFinal, fg = "black", bg = "white", font = ("Arial",44)).place(x = 0, y = 150)

def MostrarNotacion():
    if calidad.get() == "Mayor":
        return "",TriadaMayor(notas.get())       
    elif calidad.get() == "Menor":
        return "m",TriadaMenor(notas.get())
    elif calidad.get() == "Setima":
        return "7",TriadaMenor(notas.get())
    elif calidad.get() == "Setima Mayor":
        return "maj7",TriadaMenor(notas.get())

def Generar():
    AcordeF = ""
    Acorde = np.array([])
    NotacionF = ""
    if notas.get() == "" and calidad.get == "":
        return
    NotacionF,Acorde = MostrarNotacion()
    notacion.set(notas.get() + NotacionF)
    for i in range(len(Acorde)):
        AcordeF = AcordeF + Acorde[i] + " "
    AcordeFinal.set(AcordeF)

ventana = Tk()
ventana.geometry('300x300')
ventana.title("TriadGen")

#Inicializa las variables de lo
# 
#spinbox
notas = StringVar()
calidad = StringVar()
notacion = StringVar()

AcordeFinal = StringVar()
AcordeFinal.set("none")
notacion.set("none")
init(ventana)
ventana.mainloop()