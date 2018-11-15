'''
this is a demonstration of the monty hall paradox
'''

import random

class Gameshow(object):
	"""A game show to demonstrate the monty hall paradox"""
	def __init__(self):
		self.correct = random.randint(1,3)
		self.turn = 0;
		self.board = [1,2,3]

	def get_turn(self):
		return self.turn

	def get_board(self):
		return self.board

	def check_ans(self, guess):
		return guess == self.correct

	def make_guess(self,guess):
		self.turn  += 1
		if guess == self.correct:
			tmp = self.board[:]
			tmp.remove(self.correct)
			self.board.remove(random.choice(tmp))
		else:
			tmp = self.board[:]
			tmp.remove(self.correct)
			tmp.remove(guess)
			self.board.remove(random.choice(tmp))
	def reset (self):
		self.correct = random.randint(1,3)
		self.turn = 0;
		self.board = [1,2,3]	

class Player(object):
	"""Player of the gameshow"""
	def __init__(self, num, isSwapped):
		self.num = num
		self.isSwapped = isSwapped
		self.guess = random.randint(1,3)
		self.game = Gameshow()
	def play(self):
		self.board = self.game.get_board()
		if not self.isSwapped:
			self.game.make_guess(self.guess)
			return  self.game.check_ans(self.guess)
		else:
			self.game.make_guess(self.guess)
			tmp = self.game.get_board()[:]
			tmp.remove(self.guess)
			self.guess = random.choice(tmp)
			return self.game.check_ans(self.guess)

def test():
	goodPlayer = Player(1,True)
	dumpPlayer = Player(2,False)
	goodPlayerWin = 0
	dumpPlayerWin = 0
	TRIAL = 1000
	for i in range(TRIAL):
		if goodPlayer.play():
			goodPlayerWin += 1
			# goodPlayer.game.reset()

		if dumpPlayer.play():
			dumpPlayerWin +=1
			# dumpPlayer.game.reset()

		goodPlayer = Player(1,True)
		dumpPlayer = Player(2,False)

	goodPlayerWinRate = goodPlayerWin/float(TRIAL) 
	dumpPlayerWinRate = dumpPlayerWin/float(TRIAL) 
	
	print ("After %d number of trial:" %TRIAL)
	print ("good Player have win rate of %2f" %goodPlayerWinRate )
	print ("dump Player have win rate of %2f" %dumpPlayerWinRate )



if __name__ == '__main__':
	test()


'''
Okey I mess up some where, even with swap and not swap the win rate is always around 33%
'''
		
