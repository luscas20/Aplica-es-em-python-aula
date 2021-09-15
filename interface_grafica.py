#tkinter teste#

import tkinter
janela = tkinter.Tk()
janela.title("Aplicação GUI")
janela.mainloop()

#janela não dimensionável#

import tkinter
janela = tkinter.Tk()
janela.title("Aplicação GUI")
janela.resizable(False, False)
janela.mainloop()

#Usando Widget Label#

import tkinter as tk
from tkinter import ttk
janela = tk.Tk()
janela.title("Aplicação GUI widget label")
ttk.Label(janela, text="Componente Label").grid(column=0, row=0)
janela.mainloop()

#Usando widget Button + Entry#

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

# Radio Buttons#

import tkinter as tk
janela =  tk.Tk()
v = tk.IntVar()
tk.Label(janela, text="Escolha uma linguagem de programação", justify = tk.LEFT,padx=20).pack()
tk.Radiobutton(janela, text="python",
padx=25,variable=v,value=1).pack(anchor=tk.W)
tk.Radiobutton(janela, text="C++", padx=25,variable=v,value=2).pack(anchor=tk.W)
tk.Radiobutton(janela, text="HTML5", padx=25,variable=v,value=3).pack(anchor=tk.W)
tk
janela.mainloop()

#Mensagens#

import tkinter as tk
janela = tk.Tk()
mensagem_para_o_usuario = "Acesso Negado.\n(Entrar em contato com o supervisor)"
msg = tk.Message(janela, text= mensagem_para_o_usuario)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack()
janela.mainloop()

