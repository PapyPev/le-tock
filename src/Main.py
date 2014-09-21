#!/usr/bin/env python
# -*-coding:utf-8-*-

#############################################################
# Python Program - Main.py
#
# project   : le-tock
# @authors  : Guillaume Josserand - Pierre Vrot
# @date     : 2014-09-18
#
#############################################################

from Players import Players
from Games import Games
from Horse import Horse

#############################################################
### MAIN
#############################################################

#That test forbids Main to be imported in another .py and their functions used.
#Works like a main in C language.

if __name__ == "__main__":

    tagada = Players("tagado", "blue", None)
    name = tagada.name
    did = tagada.id
    print(name, did)

    petitpois = Players("petitpois", "red", 1)
    name = petitpois.name
    did = petitpois.id
    print(name, did)

    tagada.playCard()
