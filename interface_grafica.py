#tkinter teste#

#import tkinter
#janela = tkinter.Tk()
#janela.title("Aplicação GUI")
#janela.mainloop()

#janela não dimensionável#

#import tkinter
#janela = tkinter.Tk()
#janela.title("Aplicação GUI")
#janela.resizable(False, False)
#janela.mainloop()

#Usando Widget Label#

#import tkinter as tk
#from tkinter import ttk
#janela = tk.Tk()
#janela.title("Aplicação GUI widget label")
#ttk.Label(janela, text="Componente Label").grid(column=0, row=0)
#janela.mainloop()

#Usando  widget Button#

import tkinter as tk
def mostrar_nomes():
    print("nome: %s\nSobrenome: %s" % (e1.get(), e2.get()))
janela = tk.Tk()
janela.title("Aplicação GUI com o Widget Entry")
tk.Label(janela,text="Nome").grid(row=0)
tk.Label(janela,text="Sobrenome").grid(row=1)
e1 = tk.Entry(janela)
e2 = tk.Entry(janela)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
tk.Button(janela, text='sair', 
command=janela.quit).grid(row=3,column=0,sticky=tk.W,pady=4)
tk.Button(janela, text='exibir Dados', command=mostrar_nomes).grid(row=3,column=1, sticky=tk.W,pady=4)
tk.mainloop()
