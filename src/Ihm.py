# -*- coding: utf-8 -*-

import sys, os, tkinter, json
from pprint import pprint
    
"""
root=tkinter.Tk()
size_grid_x = 350
size_grid_y = 200
fond=tkinter.Canvas(root, width=size_grid_x, height=size_grid_y, background='darkgray')
fond.pack()
i = 0
while i*10<size_grid_x:
    ligne=fond.create_line(0 + i * 10,0,0 + i * 10,size_grid_y, width=2)
    ligne=fond.create_line(0,0+ i * 10,size_grid_x, 0 + i * 10, width=2)
    #fond.create_rectangle(0 , 0, 0, 0)
    i+=1

root.mainloop()
"""

file=open('tock_4j.json', 'r')
jsonString = file.read()
file.close()

data = json.loads(jsonString)
#if 'nbPlayers' in data:
   # print(data['nbPlayers'])
   # print(data['cellTypes'])
    
#########################################################
root=tkinter.Tk()
size_grid_x = data['gridwidth']*10
size_grid_y = data['gridheight']*10
fond=tkinter.Canvas(root, width=size_grid_x, height=size_grid_y, background='darkgray')
fond.pack()
i = 0
j = 0
for row in data['cells']:
    for cel in row:
        
        fond.create_rectangle(0 + cel['x']*10 , 0 + j*10, 10 + cel['x']*10, 10 + j*10, fill=data['cellTypes'][cel['type']]['color'])
        i += 1
    i=0
    j += 1
root.mainloop()

##print(data['cells'][0]) #--> La premiere ligne
##print(data['cells'][0][0])# -->La cellule
##print(data['cells'][0][0]['type'])# --> L'info de la cellule

