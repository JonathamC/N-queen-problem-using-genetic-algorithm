import random

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

def main():

    populationSize = int(input("Choose starting population: "))
    population = generateStartingPopulation(populationSize)
    print(population[0])
    matrix = convertTo2DMatrix(population[0])
    printMatrix(matrix)
    print(fitness(population[0]))


main()