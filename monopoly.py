import random

class Board:

	def __init__(self): #initialize board and starting states
		self.board = [0] * 40
		self.pieceIndex = 0
		self.maxMoves = 0
		self.speeding = False
		self.chanceDeck = 0
		self.ccDeck = 0
		self.spaceNames = ["GO", "Medeterranian Avenue","Community Chest", "Baltic Avenue","Income Tax","Reading Railroad","Oriental Avenue","Chance","Vermont Avenue","Conneticut Avenue", "Jail",
		"St. Charles Place","Electric Company","States Avenue","Virginia Avenue","Pennsylvania Railroad","St. James Place","Community Chest","Tennessee Avenue","New York Avenue","Free Parking",
		"Kentucky Avenue","Chance","Indiana Avenue","Illinois Avenue","B. & O. Railroad", "Atlantic Avenue", "Ventnor Avenue", "Water Works", "Marvin Gardens", "Go To Jail",
		"Pacific Avenue","North Carolina Avenue", "Community Chest", "Pennsylvania Avenue", "Short Line Railroad", "Chance", "Park Place", "Luxury Tax","Boardwalk"]

	def Roll(self): #if three doubles are rolled, it is SPEEDING
		a = random.randint(1, 6)
		b = random.randint(1, 6)

		if a == b:
			#print("DOUBLES!")
			c = random.randint(1, 6)
			d = random.randint(1, 6)
			if c == d:
				#print("DOUBLE DOUBLES!")
				e = random.randint(1, 6)
				f = random.randint(1, 6)
				self.speeding = True
				#print(a + b + c + d + e + f)
				return a + b + c + d + e + f
			#print(a + b + c + d)
			return a + b + c + d
		#print(a + b)
		return a + b

	def Move(self, roll):
		if self.speeding == True: #if the piece is speeding, move it to jail then set speeding to false
			self.pieceIndex = 10
			self.speeding = False
			#print("JAIL")
		else:
			self.pieceIndex += roll #make a move

			if(self.pieceIndex > 39): #bound checker
				self.pieceIndex = self.pieceIndex - 40

			if(self.pieceIndex == 7 or self.pieceIndex == 22 or self.pieceIndex == 36): #landed on a CHANCE space
				if(self.chanceDeck == 0): #Advance to "Go".
					self.pieceIndex = 0
					self.chanceDeck+= 1
				if(self.chanceDeck == 1): #Advance to Illinois Ave. {Avenue}. If you pass Go, collect $200.
					self.pieceIndex = 24
					self.chanceDeck+= 1
				if(self.chanceDeck == 2): #Advance to St. Charles Place. If you pass Go, collect $200.
					self.pieceIndex = 11
					self.chanceDeck+= 1
				if(self.chanceDeck == 3): #Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total 10 times the amount thrown.
					if (self.pieceIndex == 7):
						self.pieceIndex = 12 #eletric company
					if (self.pieceIndex == 22):
						self.pieceIndex = 28 #waterworks
					if (self.pieceIndex == 36):
						self.pieceIndex = 12 #eletric company
					self.chanceDeck+= 1
				if(self.chanceDeck == 4): #Advance token to the nearest Railroad 
					if (self.pieceIndex == 7):
						self.pieceIndex = 15 #pennsylvania railroad
					if (self.pieceIndex == 22):
						self.pieceIndex = 25 #b. & o. railroad
					if (self.pieceIndex == 36):
						self.pieceIndex = 5 #reading railroad
					self.chanceDeck+= 1
				if(self.chanceDeck == 5): #Go Back Three Spaces
					self.pieceIndex = self.pieceIndex - 3
					if(self.pieceIndex < 0): #bound checker
						self.pieceIndex += 40
					self.chanceDeck+= 1
				if(self.chanceDeck == 6): #Go directly to Jail
					self.pieceIndex = 10
					self.chanceDeck+= 1
				if(self.chanceDeck == 7): #Take a trip to Reading Railroad
					self.pieceIndex = 5
					self.chanceDeck+= 1
				if(self.chanceDeck == 8): #Take a walk on the Boardwalk
					self.pieceIndex = 39
					self.chanceDeck+= 1
				if(self.chanceDeck < 14 and self.chanceDeck > 8):
					self.chanceDeck+= 1
				if(self.chanceDeck == 14): #reshuffle at the end of the deck
					self.chanceDeck == 0

			if(self.pieceIndex == 2 or self.pieceIndex == 17 or self.pieceIndex == 33):
				if(self.ccDeck == 0): #Advance to "Go".
					self.pieceIndex = 0
					self.ccDeck+= 1
				if(self.ccDeck == 1): #Go to Jail
					self.pieceIndex = 10
					self.ccDeck+= 1
				if(self.ccDeck < 16 and self.chanceDeck > 1):
					self.ccDeck+= 1
				if(self.ccDeck == 16):
					self.ccDeck = 0

			if(self.pieceIndex == 30): #go to jail space
				self.pieceIndex = 10

		self.board[self.pieceIndex] = self.board[self.pieceIndex] + 1 
		return 0

	def PrintProbability(self):
			print(self.board)
			for i in range(0, 40):
				print(self.spaceNames[i], ": ", self.board[i])

	def compileData(self):
		propertyList = [[self.board[1], "Medeterranian Avenue"], [self.board[3], "Baltic Avenue"], [self.board[5], "Reading Railroad"], [self.board[6], "Oriental Avenue"],
		[self.board[8], "Vermont Avenue"], [self.board[9], "Conneticut Avenue"], [self.board[11], "St. Charles Place"], [self.board[12], "Electric Company"], 
		[self.board[13], "States Avenue"], [self.board[14], "Virginia Avenue"], [self.board[15], "Pennsylvania Railroad"], [self.board[16], "St. James Place"],
		[self.board[18], "Tennessee Avenue"], [self.board[19], "New York Avenue"], [self.board[21], "Kentucky Avenue"], [self.board[23], "Indiana Avenue"],
		[self.board[24], "Illinois Avenue"], [self.board[25], "B. & O. Railroad"], [self.board[26], "Atlantic Avenue"], [self.board[27], "Ventnor Avenue"],
		[self.board[28], "Water Works"], [self.board[29], "Marvin Gardens"], [self.board[31], "Pacific Avenue"], [self.board[32], "North Carolina Avenue"],
		[self.board[34], "Pennsylvania Avenue"], [self.board[35], "Short Line"], [self.board[37], "Park Place"], [self.board[39], "Boardwalk"]]

		max =  [0, " "]
		for property in propertyList: #find max
			if property[0] > max[0]:
				max = property

		for i in range (0, 28):
			for j in range (0, 28):
				if propertyList[i][0] > propertyList[j][0]:
					temp = [0, " "]
					temp = propertyList[j]
					propertyList[j] = propertyList[i]
					propertyList[i] = temp

		for property in propertyList:
			print(property[1], 100*property[0]/max[0])



board = Board()
for i in range (0, 1500000):
	board.Move(board.Roll())
#board.PrintProbability()
board.compileData()

