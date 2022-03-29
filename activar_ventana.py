import tkinter as tk
from tkinter import messagebox

def validar():
    if entrada1.get()=="pepe":
        abrirventana2()
    else:
        messagebox.showwarning("Cuidado", " password incorecto")

def abrirventana2():
    ventana.withdraw()
    win=tk.Toplevel()
    win.geometry("600x500")
    win.configure(background ='dark turquoise')
    win.title("Ventana 2")
    e3=tk.Label(win, text="Biendenido a la segunda ventana", bg="pink", fg="white")
    e3.pack(padx=5,pady=5, ipadx=5,ipady=5, fill=tk.X)
    boton2=tk.Button(win, text="OK", command=win.destroy)
    boton2.pack(side=tk.TOP)

def cerrarventana():
    ventana.destroy()

ventana=tk.Tk()
ventana.title("ventana numero 1")
ventana.geometry("680x540")
ventana.configure(bg="yellow")
image=tk.PhotoImage(file="logoudcr.gif")
image=image.subsample(1,1)
label=tk.Label(image=image)
label.place(x=0, y=0,relwidth =1.0, relheight=1.0)
label.pack()


t1=tk.Label(ventana, text="Evaluador 1.0",bg="black", fg="white")
t1.pack(padx=5,pady=5, ipadx=5,ipady=5, fill=tk.X)
Font_tuple=("Comic Sans MS", 20, "bold")
t1.configure(font=Font_tuple)
t2=tk.Label(ventana, text="Datos Informativos",bg="black", fg="white")
t2.pack(padx=5,pady=5, ipadx=5,ipady=5,fill=tk.X )
Font_tuple=("Comic Sans MS", 12, "bold")
t2.configure(font=Font_tuple)
t3=tk.Label(ventana, text="Club :   Universidad de Cartagena",bg="black", fg="white",)
t3.pack(padx=5,pady=5, ipadx=5,ipady=5,fill=tk.X )
Font_tuple=("Comic Sans MS", 12, "bold")
t3.configure(font=Font_tuple)
t4=tk.Label(ventana, text="Diciplina :   Baloncesto",bg="black", fg="white")
t4.pack(padx=5,pady=5, ipadx=5,ipady=5, fill=tk.X)
Font_tuple=("Comic Sans MS", 12, "bold")
t4.configure(font=Font_tuple)
t5=tk.Label(ventana, text="Categoria :   Mayores Masculino",bg="black", fg="white",)
t5.pack(padx=5,pady=5, ipadx=5,ipady=5,fill=tk.X )
Font_tuple=("Comic Sans MS", 12, "bold")
t5.configure(font=Font_tuple)
t6=tk.Label(ventana, text="Instructor :   Alberto Hernandez Pacheco",bg="black", fg="white")
t6.pack(padx=5,pady=5, ipadx=5,ipady=5, fill=tk.X )
Font_tuple=("Comic Sans MS", 12, "bold")
t6.configure(font=Font_tuple)
e1=tk.Label(ventana, text="Password:", bg="black", fg="white")
e1.pack(padx=5,pady=5, ipadx=5,ipady=5)
entrada1=tk.Entry(ventana)
entrada1.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)
boton=tk.Button(ventana, text="Nueva Ventana", fg="blue", command=abrirventana2)
boton.pack(side=tk.TOP)
boton3=tk.Button(ventana, text="Validar Password", fg="blue", comman=validar )
boton3.pack(side=tk.TOP)


ventana.mainloop()
