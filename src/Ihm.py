#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, Tkinter, json

file=open('tock_4j.json', 'r')
jsonString = file.read()
file.close()

data = json.loads(jsonString)
    
#########################################################
window=Tkinter.Tk()
size_case = 20
size_grid_x = data['gridwidth']*size_case
size_grid_y = data['gridheight']*size_case
fond=Tkinter.Canvas(window, width=size_grid_x, height=size_grid_y, background='darkgray')
fond.pack()
i = 0
j = 0

grid = [[0] * data['gridwidth'] for _ in range(data['gridheight'])]
for row in data['cells']:
    for cel in row:
        
        if cel['type'] == 'teleportation':
            fond.create_rectangle(0 + cel['x']*size_case , 0 + j*size_case, size_case + cel['x']*size_case, size_case + j*size_case, fill=data['cellTypes']['teleportation']['color'])
            grid[j][i]='teleportation'
        elif cel['type'] == 'start':
            fond.create_rectangle(0 + cel['x']*size_case , 0 + j*size_case, size_case + cel['x']*size_case, size_case + j*size_case, fill=data['cellTypes']['start']['color'])
            grid[j][i]='start'
        else:
            fond.create_rectangle(0 + cel['x']*size_case , 0 + j*size_case, size_case + cel['x']*size_case, size_case + j*size_case, fill=cel['player'])
            grid[j][i]='simpleroad'
        
        i += 1
    i=0
    j += 1

coord_x = 90
coord_y = 110
radius = 10
fond.create_oval(coord_x-radius, coord_y-radius, coord_x+radius, coord_y+radius, width=1, fill='skyblue')

window.mainloop()

##print(data['cells'][0]) #--> La premiere ligne
##print(data['cells'][0][0])# -->La cellule
##print(data['cells'][0][0]['type'])# --> L'info de la cellule


print(grid)

