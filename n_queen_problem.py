import random
from time import sleep 
def generateStartingPopulation(size): 
    """ 
    Generate starting population
    """
    populations = [] 
    for _ in range(size): 
        temp = []
        for q in range(8): 
            temp.append(random.randrange(0,8))
        
        populations.append(temp)
    
    return populations

def convertTo2DMatrix(chromosome):
    chessboard = [["-" for _ in range(8)] for _ in range(8)]
    column = 0
    for row in chromosome: 
        chessboard[row][column] = "Q"
        column += 1
    return chessboard

def printMatrix(matrix): 
    for i in matrix: 
        for j in i: 
            print("{}  ".format(j), end="")
        print()

def topDownDiagonalMatrixTraversal(matrix): 
    """
    Traverse matrix from top left to bottom right corner. 
    """
    result = [] 

    for l in range(2*8-1): 
        t = max(0, l+1-8)
        b = min(l, 8-1)
        temp = []
        for i in range(t, b + 1): 
            temp.append(matrix[i][l-i])
        result.append(temp)
    return result

def bottomUpDiagonalMatrixTraversal(chromosome): 
    """
    Traverse matrix from top right to bottom left corner. 

    To achieve this result without coding new traversal method,
    just simply flip the matrix horizontally and call TopDownDiagonalMatrixTraversal. 
    """
    revChromosome = chromosome[::-1]
    revMatrix = convertTo2DMatrix(revChromosome)
    return topDownDiagonalMatrixTraversal(revMatrix)

def topDownVerticalMatrixTraversal(matrix): 
    """
    Traverse matrix from top to bottom vertically. 
    """
    result = []
    for i in range(8): 
        temp = [] 
        for j in range(8): 
            temp.append(matrix[j][i])
        result.append(temp)
    return result

def countQueensAttacking(matrix): 
    """ 
    Count number of queens attacking in matrix. 

    Used in calculating fitness score. 
    """
    total = 0 
    for i in matrix:
        queen = 0 
        for j in i: 
            if j == "Q": 
                queen += 1 
        if queen > 0:
            total += queen - 1 
        
    return total 

def crossover(p1, p2): 
    """
    Reproduce using parent1 p1 chromosome and parent2 p2 chromosome by crossover. 
    Random crossover points between 1 and 7 
    """

    crossoverPoint = random.randrange(1,8)
    child1 = p1[:crossoverPoint] + p2[crossoverPoint:]
    child2 = p2[:crossoverPoint] + p1[crossoverPoint:]

    return child1, child2


def fitness(chromosome): 
    """
    Count how many queens are attacking horizontally and diagonally. 
    """
    fitnessScore = 0
    chessboard = convertTo2DMatrix(chromosome)

    # horizontally 
    fitnessScore += countQueensAttacking(chessboard)

    # vertically 
    fitnessScore += countQueensAttacking(topDownVerticalMatrixTraversal(chessboard))

    # diagonally 
    fitnessScore += countQueensAttacking(topDownDiagonalMatrixTraversal(chessboard))
    fitnessScore += countQueensAttacking(bottomUpDiagonalMatrixTraversal(chromosome))

    return fitnessScore

def randomIndexGenerator(selectionFactor): 
    rand = random.uniform(0,1)
    randIndex = 150 *  rand ** selectionFactor

    return int(randIndex)

def mutation(chromosome, mutationProb): 
    if random.uniform(0,1) < 0.6: 
        mutatePoint = random.randrange(0,8)
        mutate = random.randrange(0,8)

        chromosome[mutatePoint] = mutate


def main():
    generations = 1
    selectionFactor = 5 # randomly chosen number. The higher the selection factor, the better for parents selection. 
    populationSize = 150 # randomly chosen 
    mutationProb = 0.6 #randomly chosen 

    # generate starting population
    population = generateStartingPopulation(populationSize)
    populationWithFitness = []

    for i in population: 
        populationWithFitness.append([fitness(i), i])
    # create a new population 2d array with fitness score for each chromosome
    populationWithFitness = sorted(populationWithFitness, key = lambda x: x[0], reverse = False)

    # while loop infinitely until fitness of 0 is created 
    while (True):

        tempPopulation = []
        for _ in range(75): 
            # parent1 and parent2 selection 
            p1 = populationWithFitness[randomIndexGenerator(selectionFactor)][1]
            p2 = populationWithFitness[randomIndexGenerator(selectionFactor)][1]

            # prevent selecting same parent for parent1 and parent2 
            while p2 == p1: 
                p2 = populationWithFitness[randomIndexGenerator(selectionFactor)][1]


            child1, child2 = crossover(p1, p2)
            mutation(child1, mutationProb)
            mutation(child2, mutationProb)
            fitnessChild1 = fitness(child1)
            fitnessChild2 = fitness(child2)
            
            


            if fitnessChild1 == 0: 
                print("\nGeneration #: {}\n".format(generations))
                printMatrix(convertTo2DMatrix(child1))
                print("Chromosome: {}, Fitness Score = {}\n".format(child1, fitnessChild1))
                return 
            print("Chromosome = {}, Fitness Score = {}".format(child1, fitnessChild1))
            if fitnessChild2 == 0: 
                print("\nGeneration #: {}\n".format(generations))
                printMatrix(convertTo2DMatrix(child2))
                print("Chromosome: {}, Fitness Score = {}\n".format(child2, fitnessChild2))
                return
            print("Chromosome = {}, Fitness Score = {}".format(child2, fitnessChild2))
            tempPopulation.append([fitnessChild1, child1])
            tempPopulation.append([fitnessChild2, child2])
            # sleep(0.1)
        generations += 1
        populationWithFitness = tempPopulation
        populationWithFitness = sorted(populationWithFitness, key = lambda x: x[0], reverse = False)



main()
