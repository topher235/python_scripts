#NOTE TO USER:
#TO ESCAPE THE SCRIPT PRESS CTRL+C

import random
import threading

#Hexadecimal range: 21 - 79
#Add all symbols to an array based on their hexadecimal values
initial = '!'
hexa = ord(initial)
symbols = [initial]
space = []
for i in range(89):
	hexa += 1
	char = chr(hexa)
	symbols.append(char)

#Gets a random number
#Uses that as the x-coordinate
def randomXPos():
	randomXPos = random.randrange(37)
	return randomXPos

#Gets a random number
#Uses that to determine the symbol to print out
def randomIndex():
	randomIndex = random.randrange(len(symbols))
	return randomIndex
	
#Prints a symbol every 0.01 seconds
#Adds spaces in front of the symbol for formatting
#Rains symbols in random places indefinitely
def printIt():
	threading.Timer(0.01, printIt).start()
	for i in range(10):
		spaces = ""
		y = randomXPos()
		for j in range(y):
			spaces = spaces + " "
		x = symbols[randomIndex()]
		z = symbols[randomIndex()]
		print(spaces + x + spaces + z)

printIt()
