import random
import time
from time import sleep 
def generateStartingPopulation(size, numQueens): 
    """ 
    Generate starting population
    """
    populations = [] 
    for _ in range(size): 
        temp = []
        for q in range(numQueens): 
            temp.append(random.randrange(0,numQueens))
        
        populations.append(temp)
    
    return populations

def convertTo2DMatrix(chromosome, numQueens):
    chessboard = [["-" for _ in range(numQueens)] for _ in range(numQueens)]
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

def topDownDiagonalMatrixTraversal(matrix, numQueens): 
    """
    Traverse matrix from top left to bottom right corner. 
    """
    result = [] 

    for l in range(2*numQueens-1): 
        t = max(0, l+1-numQueens)
        b = min(l, numQueens-1)
        temp = []
        for i in range(t, b + 1): 
            temp.append(matrix[i][l-i])
        result.append(temp)
    return result

def bottomUpDiagonalMatrixTraversal(chromosome, numQueens): 
    """
    Traverse matrix from top right to bottom left corner. 
    To achieve this result without coding new traversal method,
    just simply flip the matrix horizontally and call TopDownDiagonalMatrixTraversal. 
    """
    revChromosome = chromosome[::-1]
    revMatrix = convertTo2DMatrix(revChromosome, numQueens)
    return topDownDiagonalMatrixTraversal(revMatrix, numQueens)

def topDownVerticalMatrixTraversal(matrix, numQueens): 
    """
    Traverse matrix from top to bottom vertically. 
    """
    result = []
    for i in range(numQueens): 
        temp = [] 
        for j in range(numQueens): 
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

def crossover(p1, p2, numQueens): 
    """
    Reproduce using parent1 p1 chromosome and parent2 p2 chromosome by crossover. 
    Random crossover points between 1 and 7 
    """

    crossoverPoint = random.randrange(1,numQueens)
    child1 = p1[:crossoverPoint] + p2[crossoverPoint:]
    child2 = p2[:crossoverPoint] + p1[crossoverPoint:]

    return child1, child2


def fitness(chromosome, numQueens): 
    """
    Count how many queens are attacking horizontally and diagonally. 
    """
    fitnessScore = 0
    chessboard = convertTo2DMatrix(chromosome, numQueens)

    # horizontally 
    fitnessScore += countQueensAttacking(chessboard)

    # vertically 
    fitnessScore += countQueensAttacking(topDownVerticalMatrixTraversal(chessboard, numQueens))

    # diagonally 
    fitnessScore += countQueensAttacking(topDownDiagonalMatrixTraversal(chessboard, numQueens))
    fitnessScore += countQueensAttacking(bottomUpDiagonalMatrixTraversal(chromosome, numQueens))

    return fitnessScore

def randomIndexGenerator(selectionFactor): 
    rand = random.uniform(0,1)
    randIndex = 150 *  rand ** selectionFactor

    return int(randIndex)

def mutation(chromosome, mutationProb, numQueens): 
    if random.uniform(0,1) < mutationProb: 
        mutatePoint = random.randrange(0,numQueens)
        mutate = random.randrange(0,numQueens)

        chromosome[mutatePoint] = mutate


def main():
    generations = 1
    populationSize = 150 # chosen value
    numQueens = int(input("Enter number of queens: "))
    selectionFactor = 5 # chosen value 
    mutationProb = 0.6  # chosen value 
    print("\n")
    # generate starting population
    population = generateStartingPopulation(populationSize, numQueens)
    populationWithFitness = []

    for i in population: 
        populationWithFitness.append([fitness(i, numQueens), i])
    # create a new population 2d array with fitness score for each chromosome
    populationWithFitness = sorted(populationWithFitness, key = lambda x: x[0], reverse = False)

    # while loop infinitely until fitness of 0 is created 
    while (True):

        tempPopulation = []
        for _ in range(populationSize // 2): 
            # parent1 and parent2 selection 
            p1 = populationWithFitness[randomIndexGenerator(selectionFactor)][1]
            p2 = populationWithFitness[randomIndexGenerator(selectionFactor)][1]

            # prevent selecting same parent for parent1 and parent2 
            while p2 == p1: 
                p2 = populationWithFitness[randomIndexGenerator(selectionFactor)][1]


            child1, child2 = crossover(p1, p2, numQueens)
            mutation(child1, mutationProb, numQueens)
            mutation(child2, mutationProb, numQueens)
            fitnessChild1 = fitness(child1, numQueens)
            fitnessChild2 = fitness(child2, numQueens)
            
            


            if fitnessChild1 == 0: 
                print("\nGeneration #: {}\n".format(generations))
                printMatrix(convertTo2DMatrix(child1, numQueens))
                print("Chromosome: {}, Fitness Score = {}\n".format(child1, fitnessChild1))
                return 
            print("Chromosome = {}, Fitness Score = {}".format(child1, fitnessChild1))
            if fitnessChild2 == 0: 
                print("\nGeneration #: {}\n".format(generations))
                printMatrix(convertTo2DMatrix(child2, numQueens))
                print("Chromosome: {}, Fitness Score = {}\n".format(child2, fitnessChild2))
                return
            print("Chromosome = {}, Fitness Score = {}".format(child2, fitnessChild2))
            tempPopulation.append([fitnessChild1, child1])
            tempPopulation.append([fitnessChild2, child2])
            # sleep(0.1)
        generations += 1
        populationWithFitness = tempPopulation
        populationWithFitness = sorted(populationWithFitness, key = lambda x: x[0], reverse = False)

    
s = time.time()
main()
print("{:.2f} seconds".format((time.time()-s)))