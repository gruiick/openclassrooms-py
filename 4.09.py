#!/usr/bin/env python3
# coding: utf-8

# $Id: 4.09.py 1.1 $
# SPDX-License-Identifier: BSD-2-Clause

""" Tkinter """

#from tkinter import *  # bah! pas bien !
import tkinter  # les namespaces, c'est pas pour les chiens

fenetre = tkinter.Tk()
champ_label = tkinter.Label(fenetre, text="Salut !")
champ_label.pack()

var_texte = tkinter.StringVar()
ligne_texte = tkinter.Entry(fenetre, textvariable=var_texte, width=30)
ligne_texte.pack()

var_case = tkinter.IntVar()
case = tkinter.Checkbutton(fenetre, text="Ne plus poser cette question", variable=var_case)
case.pack()

print(var_case.get())

fenetre.mainloop()

