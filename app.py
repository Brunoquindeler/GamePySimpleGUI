import PySimpleGUI as sg
from packages.hero import *
import os.path
from os import path

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Enter Name, Vocation and Sex')],
            [sg.Text('Name:'), sg.InputText(key='n')],
            [sg.Text('Vocation:'), sg.InputText(key='v')],
            [sg.Text('Sex:'), sg.InputText(key='s')],
            [sg.Button('Promotion'), sg.Button('UP'), sg.Button('DOWN')],
            [sg.Button('Create'), sg.Button('Print'), sg.Button('Close'), sg.Button('Save')]]

# Create the Window
window = sg.Window('Character', layout)
# Event Loop to process "events" and get the "values" of the inputs


while True:
    event, values = window.read()
    if event in (None, 'Close'):   # if user closes window or clicks cancel
        break

    if event == 'Create':
        n = values['n']
        v = values['v']
        s = values['s']
        
        if path.exists(values['n']+'.txt'):
            print('Character already exists')
            print('')
        elif values['n'] == '' or values['v'] == '' or values['s'] == '':
            print('Incomplete field')
            print('')
        else:
            h = Hero(values['n'], values['v'], values['s']) 
            arq = open(h.name+'.txt','w')
            print('')


    if event == 'Print':
        try:
            h.printHero()
        except:
            print('No character created')

    if event == 'Promotion':
        try:
            if h.p == False:
                h.promotion()
            else:
                print('Character already promoted')
        except:
            print('No character created')
            
    
    if event == 'UP':
        try:
            h.upLvl()
        except:
            print('No character created')

    if event  == 'DOWN':
        try:
            h.downLvl()
        except:
            print('No character created')

    if event == 'Save':
        
        try:
            txt = 'Name: ' + h.name + '\nLevel: ' + str(h.lvl) + '\nVocation: ' + h.voc + '\nSex: ' + h.sex + '\nLife: {:.1f}'.format(h.life) + '\nMana: {:.1f}'.format(h.mana)
            arq = open(h.name+'.txt', 'w')
            arq.write(txt)
            arq.close()
        except:
            print('No character created')

window.close()