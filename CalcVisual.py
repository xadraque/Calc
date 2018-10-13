# -*- coding:utf-8 -*-

from tkinter import *

class Calculadora(object):
    def __init__(self, master):
        self.frame = Frame(master)
        self.dados = Entry(master, width=34)
        self.dados.grid(row=1,column=0)
        self.frame.grid()
        bts = ["0","1","2","3","4","5","6","7","8","9","+","-","*","/","=","C"]
        r=1
        c=0
        for bt in bts:
            comando = lambda x=bt:self.calcular(x)
            self.botao = Button(self.frame,text=bt,width=6,command=comando)
            self.botao.grid(row=r,column=c)
            c += 1
            if c > 3:
                c = 0
                r += 1

    def calcular(self,valor):
        if valor == "=":
            tudo = "123456789.+-*/"
            if self.dados.get()[0] not in tudo:
                self.dados.insert(END,"Operação invalida!")
            try:
                resutado = eval(self.dados.get())
                self.dados.insert(END, "="+str(resutado))
            except:
                self.dados.insert(END, "Error!")
        elif valor == "C":
            self.dados.delete(0,END)
        else:
            if "=" in self.dados.get():
                self.dados.delete(0,END)
            self.dados.insert(END,valor)

root = Tk()
root.title("Calculadora Rosmar")
Calculadora(root)
root.mainloop()