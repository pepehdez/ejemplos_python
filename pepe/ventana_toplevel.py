import tkinter as tk

def crearventana():
    ventana = tk.Toplevel(app)
    #ventana=tk.Tk()
    #app=tk.Tk()
    #root=tk.Toplevel()
    ventana.geometry("600x500")
    ventana.configure(background ='dark turquoise')
    ventana.title("Valoracion de Indece de Masa Muscular")
    labelEjemplo = tk.Label(ventana, text= " New Window")
    buttonEjemplo = tk.Button(ventana, text = " New window boton")

    labelEjemplo.pack()
    buttonEjemplo.pack()

app = tk.Tk()

app.title("Evaluador 1.0")
app.geometry("680x540")
app.configure(bg="yellow")
image=tk.PhotoImage(file="logoudcr.gif")
image=image.subsample(1,1)
label=tk.Label(image=image)
label.place(x=0, y=0,relwidth =1.0, relheight=1.0)
label.pack()


t1=tk.Label(app, text="Evaluador 1.0",bg="black", fg="white")
t1.pack(padx=5,pady=5, ipadx=5,ipady=5, fill=tk.X)
Font_tuple=("Comic Sans MS", 20, "bold")
t1.configure(font=Font_tuple)
t2=tk.Label(app, text="Datos Informativos",bg="black", fg="white")
t2.pack(padx=5,pady=5, ipadx=5,ipady=5,fill=tk.X )
Font_tuple=("Comic Sans MS", 12, "bold")
t2.configure(font=Font_tuple)
t3=tk.Label(app, text="Club :   Universidad de Cartagena",bg="black", fg="white",)
t3.pack(padx=5,pady=5, ipadx=5,ipady=5,fill=tk.X )
Font_tuple=("Comic Sans MS", 12, "bold")
t3.configure(font=Font_tuple)
t4=tk.Label(app, text="Diciplina :   Baloncesto",bg="black", fg="white")
t4.pack(padx=5,pady=5, ipadx=5,ipady=5, fill=tk.X)
Font_tuple=("Comic Sans MS", 12, "bold")
t4.configure(font=Font_tuple)
t5=tk.Label(app, text="Categoria :   Mayores Masculino",bg="black", fg="white",)
t5.pack(padx=5,pady=5, ipadx=5,ipady=5,fill=tk.X )
Font_tuple=("Comic Sans MS", 12, "bold")
t5.configure(font=Font_tuple)
t6=tk.Label(app, text="Instructor :   Alberto Hernandez Pacheco",bg="black", fg="white")
t6.pack(padx=5,pady=5, ipadx=5,ipady=5, fill=tk.X )
Font_tuple=("Comic Sans MS", 12, "bold")
t6.configure(font=Font_tuple)
e11=tk.Label(app, text="Password:", bg="black", fg="white")
e11.pack(padx=5,pady=5, ipadx=5,ipady=5)
    #entrada1=tk.Entry(ventana)
    #entrada1.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)
    #boton=tk.Button(ventana, text="Nueva Ventana", fg="blue", command=abrirventana2)
    #boton.pack(side=tk.TOP)
    #boton3=tk.Button(ventana, text="Validar Password", fg="blue", comman=validar )
    #boton3.pack(side=tk.TOP)

    #ventana.mainloop()
buttonEjemplo = tk.Button(app,
               text="Crear Nueva window",
               command=crearventana) 

buttonEjemplo.pack()

app.mainloop()
