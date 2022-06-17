# prevent selecting same parent for parent1 and parent2 
            while p2 == p1: 
                p2 = populationWithFitness[randomIndexGenerator(selectionFactor)][1]