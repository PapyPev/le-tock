class Players:

	"""
		This class describes a player by :
		- his name 
		- his color
		- his teammate
		- his pins (start, during, end)
		- his cards
	"""

	# Attributes from this class
	numberOfPlayer = 0

	def __init__(self, name, color, teammate):
		""" Constructor of one Player """

		# Auto increment for the Player id
		numberOfPlayer += 1
		self.id = numberOfPlayer

		# Player's name
		self.name = name

		# HTML color code
		self.color = color

		# Co-worker for this game
		self.teammate = teammate

		# Pins' number during the game
		self.tabPins = []

		# List of player's cards
		self.tabCards = []

	################### GETTERS ###################

	def _get_name():
		return self.name

	def _get_color():
		return self.color

	def _get_teammate():
		return self.teammate

	def _get_tabPins():
		return self.tabPins

	def _get_cards():
		return self.cards

	################### SETTERS ###################

	def _set_name(newName):
		self.name = newName

	def _set_color(newColor):
		self.color = newColor

	def _set_teammate(newTeammate):
		self.teammate = newTeammate

	def _set_pinsStart(newTabPins):
		self.tabPins = newTabPins

	def _set_cards(newTabCards):
		self.tabCards = newTabCards

	################### FUNCTIONS ###################

	def play():

		print "play"
		# TODO

#tagada = Players()
petipa = Players("petitpa", "#f7777", 1)

petitpa._get_name()

