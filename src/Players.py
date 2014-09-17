#!/usr/bin/env python
# -*-coding:utf-8-*-

#############################################################
# Python Program
# 
# project	: le-tock
# @authors	: Guillaume Josserand - Pierre Vrot
# @date		: 2014-09-17
#
#############################################################

from scipy import *

#############################################################
### CLASS
#############################################################

class Players(object):

	"""
		This class describes a player by :
		- his name 
		- his color
		- his teammate
		- his pins (start, during, end)
		- his cards

		This class have methods, like :
		- playCard()	: play a card and call the card actions
		- throwCard()	: throw away the player cards
		- drawCard()	: draw a card from the pickaxe
	"""

	# Define the number of instances' class
	numberOfPlayer = 0

	### CLASS CONSTRUCTOR ###################################

	def __init__(self, name, color, teammate):
		""" Constructor of one Player """

		# Auto increment for the Player id
		Players.numberOfPlayer += 1
		self._id = Players.numberOfPlayer

		# Player's name
		self._name = name

		# HTML color code
		self._color = color

		# Co-worker for this game
		self._teammate = teammate

		# Pins' number during the game
		self._tabPins = None

		# List of player's cards
		self._tabCards = None

	### GETTERS/SETTERS #####################################

	@property
	def id(self):
		return self._id
	@id.setter
	def id(self, value):
		self._id = value
	
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self, value):
		self._name = value
	
	@property
	def color(self):
		return self._color
	@color.setter
	def color(self, value):
		self._color = value

	@property
	def teammate(self):
		return self._teammate
	@teammate.setter
	def teammate(self, value):
		self._teammate = value

	@property
	def tabPins(self):
		return self._tabPins
	@tabPins.setter
	def tabPins(self, value):
		self._tabPins = value
	
	@property
	def tabCards(self):
		return self._tabCards
	@tabCards.setter
	def tabCards(self, value):
		self._tabCards = value

	### METHODS #############################################

	def playCard(self):

		print("play")
		# TODO

	def throwCard(self):

		print("throw")
		# TODO

	def drawCard(self):
		print("draw")
		# TODO

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

tagada.play()