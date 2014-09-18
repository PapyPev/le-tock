#!/usr/bin/env python
# -*-coding:utf-8-*-

#############################################################
# Python Program - Main.py
# 
# project	: le-tock
# @authors	: Guillaume Josserand - Pierre Vrot
# @date		: 2014-09-18
#
#############################################################

from Players import Players
from Games import Games
from Interface import Interface

#############################################################
### MAIN
#############################################################

tagada = Players("tagado", "blue", None)
name = tagada.name
did = tagada.id
print(name, did)

petitpois = Players("petitpois", "red", 1)
name = petitpois.name
did = petitpois.id
print(name, did)

tagada.playCard()


