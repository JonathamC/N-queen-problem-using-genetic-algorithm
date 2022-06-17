import random

def generateStartingPopulation(size): 
    """ 
    Generate
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

def TopDownDiagonalMatrixTraversal(matrix): 
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
    printMatrix(revMatrix)
    return TopDownDiagonalMatrixTraversal(revMatrix)

def fitness(): 

    return

# populationSize = int(input("Choose starting population: "))
# population = generateStartingPopulation(populationSize)
# print(population[0])
matrix = convertTo2DMatrix([2,3,0,6,4,2,7,1])
printMatrix(matrix)
print("\n")
s = bottomUpDiagonalMatrixTraversal([2,3,0,6,4,2,7,1])