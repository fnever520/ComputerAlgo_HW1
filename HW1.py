import random

def init():
	x = 0 
	numOfZombies = int(input('Enter the number of Zombies: ' ))
	lengthOfBridge = int(input('Enter length of the bridge: '))
	posOfZombies = [None] * int(numOfZombies)
	positionOfZombies = input('Initial position of the zombie:')
	for i in positionOfZombies.split(' '):
		posOfZombies[x] = i
		x+=1

	minx = -1 
	maxn = -1
	for z in range(numOfZombies):
		print('max:' ,maxn)
		print('min:' , minx)
		maxn = max(maxn, max(lengthOfBridge-int(posOfZombies[z])+1, int(posOfZombies[z])+1))
		minx = max(minx, min(lengthOfBridge-int(posOfZombies[z]), int(posOfZombies[z])))
	print('Total time taken : ', maxn, minx)

# def Setup():
# 	pickDirection = random.randint(1, 100)
# 	if pickDirection >= 50:
# 		pickDirection = 
# 		timeTaken = lengthOfBridge 
# 	else:

# class Initialisation(self):
# 	def __init__( self, \
# 					numOfZombies,\
# 					lengthOfBridge, \
# 					positionOfZombies)
# 	self.numOfZombies =
# 	self.lengthOfBridge = 
# 	self.positionOfZombies = 

if __name__ == '__main__':
	init()
	# Setup()
