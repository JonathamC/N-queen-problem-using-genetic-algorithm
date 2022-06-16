import random

def generateStartingPopulation(size): 
    populations = [] 
    for _ in range(size): 
        temp = []
        for q in range(8): 
            temp.append(random.randrange(0,8))
        
        populations.append(temp)
    
    return populations

def convertTo2DMatrix(chromosome):
    chessboard = [["_" for _ in range(8)] for _ in range(8)]
    column = 0
    for row in chromosome: 
        chessboard[row][column] = "Q"
        column += 1
    return chessboard

def printMatrix(matrix): 
    for i in matrix: 
        print(i)
        

populationSize = int(input("Choose starting population: "))
population = generateStartingPopulation(populationSize)
print(population[0])
matrix = convertTo2DMatrix(population[0])
printMatrix(matrix)
