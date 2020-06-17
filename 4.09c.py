#!/usr/bin/env python3
# coding: utf-8

# $Id: 4.09c.py 1.1 $
# SPDX-License-Identifier: BSD-2-Clause

""" Tkinter """

import PySimpleGUI as sg

nb_clic = 0

sg.ChangeLookAndFeel('GreenTan')

layout = [
    [sg.Text('Il faut cliquer', justification='center', size=(22,1), key='-SHOW-')],
    [sg.Button('Cliquez ici'), sg.Button('Exit')],
    ]


def cliquer():
    """ \o/ quelqu'un a cliqué les gars ! """
    global nb_clic
    nb_clic += 1
    window['-SHOW-'].update("Vous avez cliqué {} fois !".format(nb_clic))


window = sg.Window('pas de titre', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Cliquez ici':
        cliquer()

window.close()
