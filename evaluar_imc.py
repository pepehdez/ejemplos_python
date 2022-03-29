from tkinter import ttk
from tkinter import *

import sqlite3

class Product:
    db_name = "database.db"

    def __init__(self, window):

        self.wind = window
        self.wind.title("Evualuador 2.0")
        #self.wind.icobitmap('balon.ico')

        frame = LabelFrame(self.wind, text = "Registro Nuevo")
        frame.grid(row =0, column =0, columnspan =3, pady =20)

        # input nombre
        Label(frame, text= "Nombre: ").grid(row = 1, column =0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row =1, column =1) 

        # input edad
        Label(frame, text= "Peso: ").grid(row = 2, column =0)
        self.peso = Entry(frame)
        self.peso.grid(row =2, column =1) 
        
        # Button input
        ttk.Button(frame, text="salve", command = self.add_product).grid(row= 3, columnspan = 2, sticky = W+ E)

        # Output Message
        self.message = Label(text = '', fg = "red")
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

        # table 
        self.tree = ttk.Treeview(height = 10, column = 2)
        self.tree.grid(row = 4, column =0, columnspan = 2)
        self.tree.heading("#0", tex="Nombre", anchor = CENTER)
        self.tree.heading("#1", tex="Peso", anchor = CENTER)

        # Button
        ttk.Button(text = 'DELETE', command = self.delete_product).grid(row = 5, column =0, sticky = W + E)
        ttk.Button(text = 'EDIT', command = self.edit_product).grid(row = 5, column =1, sticky = W + E)
        
        self.get_products()

    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn: 
          cursor = conn.cursor()
          result = cursor.execute(query, parameters)
          conn.commit()
        return result  
    

    def get_products(self):
        records =self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # query  data
        query = "SELECT * FROM product ORDER BY name DESC" 
        db_row = self.run_query(query)
        for row in db_row: 
            self.tree.insert('', 0, text = row[1], value = row[2])     

    def validation(self):
        return len(self.name.get()) != 0 and len(self.peso.get()) != 0
    
    def add_product(self):
        if self.validation():
           query = 'INSERT INTO product VALUES(NULL, ?, ?)'
           parameters = (self.name.get(), self.peso.get())
           self.run_query(query, parameters)
           self.message['text'] = 'Deportista {} Agredado Satifactoriamente'.format(self.name.get())
           self.name.delete(0,END)
           self.peso.delete(0, END)
        else:
            self.message['text'] = 'Nombre y Peso son Requeridos'
        self.get_products()   

    def delete_product(self):
        self.message['text']= ''
        try:
            self.tree.item(self.tree.selection())['text'][0] 
        except IndexError as e:
            self.massege['Text'] = 'Por favor seleccione un registro'
            return
        self.message['text']= ''    
        name = self.tree.item(self.tree.selection())['text'] 
        query = 'DELETE FROM product WHERE name = ?'
        self.run_query(query, (name, ))
        self.message['text'] = 'Registro {} borrado satifactoriaamente'.format(name)         
        self.get_products()

    def edit_product(self):
        self.message['text']= ''
        try:
            self.tree.item(self.tree.selection())['text'][0] 
        except IndexError as e:
            self.massege['Text'] = 'Por favor seleccione un registro'
            return
        name = self.tree.item(self.tree.selection())['text']
        old_peso = self.tree.item(self.tree.selection())['values'][0]
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Edite deportista'  

        # old nombre
        Label(self.edit_wind, text = 'Viejo Nombre: ').grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = name), state ='readonly').grid(row= 0, column =2) 

        # new nombre
        Label(self.edit_wind, text = 'Nuevo Nombre: ').grid(row = 1, column = 1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row= 1, column =2) 

        # old peso
        Label(self.edit_wind, text = 'Viejo Peso').grid(row =2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind,value = old_peso), state = 'readonly').grid(row = 2, column = 2)

        # new peso
        Label(self.edit_wind, text = 'Nuevo Peso' ).grid(row =3, column = 1)
        new_peso = Entry(self.edit_wind)
        new_peso.grid(row =  3, column = 2)

        Button(self.edit_wind, text = "Update", command = lambda: self.edit_records(new_name.get(), name, 
        new_peso.get(), old_peso)).grid(row = 4, column = 2, sticky = W)

    def edit_records(self, new_name, name, new_peso, old_peso):
        query = 'UPDATE product SET name = ?, peso = ? where name = ? AND peso = ?'   
        parameters = (new_name, new_peso, name, old_peso)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = ' Record {} updated successfully'.format(name)
        self.get_products()


if __name__== "__main__":
    window = Tk()
    application = Product(window)
    window.mainloop()
