#!/usr/bin/env python
# -*-coding:utf-8-*-

#############################################################
# Python Program - Games.py
# 
# project	: le-tock
# @authors	: Guillaume Josserand - Pierre Vrot
# @date		: 2014-09-18
#
#############################################################

#############################################################
### CLASS
#############################################################

class Games:

	"""
		This class describes a game by :
		- the number of player
		- the number of turn
		- the gameboard
		- the pickaxe (cards reserve)

		This class have methods, like :
		- newGame()		: initialise a new game
		- tourGame()	: up to the next turn
		- endGame()		: get the result of a game
	"""

	### CLASS CONSTRUCTOR ###################################

	def __init__(self):

		# Number of player for this Game
		self.numberOfPlayer = 4

		# Turn Number
		# 2 -> 5 cards per Player
		# 1 -> 4 cards per Player
		# 0 -> 4 cards per Player
		# under 0, new Turn
		self.numberOfTurn = 2

		# List of cases
		self.gameboard = []

		# Card pickaxe
		# Turn 2 -> 34 cards
		# Turn 1 -> 18 cards
		# Turn 0 -> 2 cards
		# 2 cards when you use jocker
		self.pickaxe = []
		
	### GETTERS/SETTERS #####################################
	
	@property
	def numberOfTurn(self):
		return self._numberOfTurn
	@numberOfTurn.setter
	def numberOfTurn(self, value):
		self._numberOfTurn = value

	@property
	def gameboard(self):
		return self._gameboard
	@gameboard.setter
	def gameboard(self, value):
		self._gameboard = value

	@property
	def pickaxe(self):
	    return self._pickaxe
	@pickaxe.setter
	def pickaxe(self, value):
	    self._pickaxe = value
	
	### METHODS #############################################

	def newGame(self):
		print("newGame")
		# TODO : initialize the game

	def turnGame(self):
		print("turnGame")
		# TODO : nextPlayer

	def endGame(self):
		print("endGame")
		# TODO : result of the game
	