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
size_grid_x = data['gridwidth']*20
size_grid_y = data['gridheight']*20
fond=tkinter.Canvas(root, width=size_grid_x, height=size_grid_y, background='darkgray')
fond.pack()
i = 0
j = 0
for row in data['cells']:
    for cel in row:
        
        if cel['type'] == 'teleportation':
            fond.create_rectangle(0 + cel['x']*20 , 0 + j*20, 20 + cel['x']*20, 20 + j*20, fill=data['cellTypes']['teleportation']['color'])
        #fond.create_rectangle(0 + cel['x']*20 , 0 + j*20, 10 + cel['x']*20, 20 + j*20, fill=data['cellTypes'][cel['type']]['color'])

        elif cel['type'] == 'start':
            fond.create_rectangle(0 + cel['x']*20 , 0 + j*20, 20 + cel['x']*20, 20 + j*20, fill=data['cellTypes']['start']['color'])
        else:
            fond.create_rectangle(0 + cel['x']*20 , 0 + j*20, 20 + cel['x']*20, 20 + j*20, fill=cel['player'])
        
        i += 1
    i=0
    j += 1  

root.mainloop()

##print(data['cells'][0]) #--> La premiere ligne
##print(data['cells'][0][0])# -->La cellule
##print(data['cells'][0][0]['type'])# --> L'info de la cellule

