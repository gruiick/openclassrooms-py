#!/usr/bin/env python3
# coding: utf-8

# $Id: 4.09b.py 1.2 $
# SPDX-License-Identifier: BSD-2-Clause

""" Tkinter """

#from tkinter import *  # bah! pas bien !
import tkinter  # les namespaces, c'est pas pour les chiens


class Interface(tkinter.Frame):
    """ fenêtre principale """
    def __init__(self, fenetre, **kwargs):
        tkinter.Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=tkinter.BOTH)
        self.nb_clic = 0

        # widgets
        self.message = tkinter.Label(self, text="faut cliquer.")
        self.message.pack()

        self.bouton_quitter = tkinter.Button(self, text="Quitter", command=self.quit)
        self.bouton_quitter.pack(side='left')

        self.bouton_cliquer = tkinter.Button(self, text="Cliquez ici", fg="red", command=self.cliquer)
        self.bouton_cliquer.pack(side='right')

    def cliquer(self):
        """ \o/ quelqu'un a cliqué les gars ! """
        self.nb_clic += 1
        self.message["text"] = "Vous avez cliqué {} fois !".format(self.nb_clic)

fenetre = tkinter.Tk()
interface = Interface(fenetre)

interface.mainloop()
interface.destroy()
