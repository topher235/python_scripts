import string
import random
import time
from functools import reduce

mutate_rate = 0.01
breed_rate = 0.75
population_size = 250
target = 'This is a genetic algorithm'

def generateCharacter():
	return random.choice(string.ascii_letters + string.punctuation + string.whitespace)

def selectParent(elders, total_score):
	# return the elder that causes the sum to surpass the total score
	selection = random.random()*total_score
	sum = 0
	for e in elders:
		sum += e['score']
		if(selection <= sum):
			return e

def generatePopulation():
	# create a phrase the same length as target with random characters
	# do this a number of times equal to population_size
	p = []
	for i in range(population_size):
		x = ''
		for index, character in enumerate(target):
			x += generateCharacter()
		p.append(x)
	return p

def checkFitness(x):
	# create a dictionary where the value is the given phrase
	# and the score is equal to the number of characters that
	# match the target
	r = {'value': x, 'score': 0}
	for i in range(len(x)):
		if(x[i] == target[i]):
			r['score'] += 1
	return r

def breed(p1, p2):
	# create a new phrase where any given letter has
	# either mutated into a new random character or
	# it takes the character of one of its parents
	c = ''
	for i in range(len(target)):
		if(random.random() < mutate_rate):
			c += generateCharacter()
		else:
			if(random.random() < 0.5):
				c += p1[i]
			else:
				c += p2[i]
	return c

# begin with a first generation and population
population = generatePopulation()
generation = 0

# create new generations until the target is reached
while(population[0] != target):
	generation += 1

	# sort the population from highest score -> lowest score
	results = sorted(list(map(checkFitness, population)), key=lambda k: k['score'], reverse=True)
	# print the best phrase from this generation
	print("Generation {0}: {1}, score {2}".format(generation, results[0]['value'], results[0]['score']))
	# slice results by a percentage of the population size
	elders = results[0: round(population_size*(1 - breed_rate))] #round because has to be int
	# reset population to be made of the elders
	population = list(map((lambda x: x['value']), elders))
	# fill out the population with a new generation
	for i in range(round(population_size*breed_rate)): #round because cannot be a float
		# time.sleep(0.001)
		# add up all scores of the elders
		total_score = reduce((lambda a, x: a + x['score']), elders, 0) #had to initialize lambda to 0 because it was expecting a to be a dict until the second iteration
		population.append(breed(selectParent(elders, total_score)['value'], selectParent(elders, total_score)['value']))
