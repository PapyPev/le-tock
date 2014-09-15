class Players:

	"""
		This class describes a player by :
		- his name 
		- his color
		- his teammate
		- his pins (start, during, end)
		- his cards
	"""

	numberOfPlayer = 0

	################### CONSTRUCTOR ###################

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

	################### GETTERS ###################

	def _get_id():
		return self._id

	def _get_name():
		return self._name

	def _get_color():
		return self._olor

	def _get_teammate():
		return self._teammate

	def _get_tabPins():
		return self._tabPins

	def _get_cards():
		return self._cards

	################### SETTERS ###################

	def _set_name(newName):
		self._name = newName

	def _set_color(newColor):
		self._color = newColor

	def _set_teammate(newTeammate):
		self._teammate = newTeammate

	def _set_pinsStart(newTabPins):
		self._tabPins = newTabPins

	def _set_cards(newTabCards):
		self._tabCards = newTabCards

	################### FUNCTIONS ###################

	def play():

		print "play"
		# TODO


################### TESTS ###################

petipa = Players("petitpa", "#f7777", 1)
name = petipa._get_name()
print name
