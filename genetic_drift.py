def allele_freq(allele, population): # defining a function that calculates allele frequency
"""
    Parameters
    ----------
    allele: the allele to be counted
    population : a list of alleles in the population 
       
    Returns
    -------
    Frequency of the input allele 
    
    """
    return population.count(allele)/len(population)

def modelDrift_AB(pop_size, n_gens):
    
    '''Models the genetic drift of alleles A and B in a population, over n generations; returns 2 arrays for the 
    frequency of alleles A and B over n generations
    """
    Parameters
    ----------
    pop_size : size of population to be mdoelled
    n_gens: number of generations to model the population over
       
    Returns
    -------
    freq_A/freq_B : lists containing the frequency of allele A/B for each n generation 
       
    """
    
    '''
    
    import random
    
    pop_A = ['A' for i in range(int(pop_size/2))] # creating list of 50 A
    pop_B = ['B' for i in range(int(pop_size/2))] # creating list of 50 B
    population = pop_A + pop_B # combining allele lists to make initial population 
    
    freq_A = [allele_freq('A', population)] # creating lists to append frequencies to
    freq_B = [allele_freq('B', population)] # calling allele_freq function to add frequency of alleles in initial population 


    for i in range(n_gens): 

        population = random.choices(population, weights = None, k = pop_size) # randomly selecting 100 alleles with replacement
        
        if 'A' in population and 'B' in population: # checking neither allele has been lost
            f_A = allele_freq('A', population) # calling my allele frequency function on new population
            freq_A.append(f_A) # adding the frequency to list of frequencies
            f_B = allele_freq('B', population)
            freq_B.append(f_B)
        else:
            break # if either allele lost, break out of loop  
    
    return freq_A, freq_B # returning the final arrays of frequencies for each allele 


freq_A, freq_B = modelDrift_AB(100, 1000) # calling my function for population of 100, over 1000 generations

import pylab as plb

generations = range(0, len(freq_A)) # defining the x data 
plb.plot(generations, freq_A, 'r', label = 'Allele A')
plb.plot(generations, freq_B, 'b', label = 'Allele B')
plb.axis(xmin = 1, xmax = len(generations), ymin = 0, ymax = 1.0)
plb.xlabel("Number of Generations")
plb.ylabel("Allele frequency")
plb.title("Change in frequency of alleles 'A' and 'B' over {} generations".format(len(generations)))
plb.legend(bbox_to_anchor=(1.05, 1),loc = 'upper left')
plb.show()



def modelDrift_A(pop_size, n_gens):
    
    """Models the genetic drift of alleles 'A' and 'a' in a population, over n generations; returns 3 arrays
    for frequency of AA, Aa and aa respectively
    
   
    Parameters
    ----------
    pop_size : size of population to be mdoelled
    n_gens: number of generations to model the population over
       
    Returns
    -------
    freq_AA, freq_Aa, freq_aa : lists containing the frequency of homozygotes (AA or aa) and heterozygots (Aa) over n generations
       
    """
  
    
    import random
    
    AA = ['AA' for i in range(int(pop_size/4))] # creating list of 25% AA 
    Aa = ['Aa' for i in range(int(pop_size/2))]
    aa = ['aa' for i in range(int(pop_size/4))] 
    
    initial_pop = AA + Aa + aa # creating initial population from the three lists

    freq_AA = [allele_freq('AA', initial_pop)] # initialising lists to append frequencies at each generation
    freq_Aa = [allele_freq('Aa', initial_pop)] # using allele_freq function to add frequency of alleles in the initial population 
    freq_aa = [allele_freq('aa', initial_pop)]


    for i in range(n_gens):

        new_pop = [] # initialising new population list

        for ind in range(pop_size): 
            pair = random.choices(initial_pop, k = 2) # randomly selecting 2 individuals from the initial population
            offspring = pair[0][random.randint(0,1)] + pair[1][random.randint(0,1)] # creating offspring from one randomly selected allele from each parent 
            if offspring == 'aA':
                offspring = 'Aa' # ensuring all heterozygotes are in format 'Aa', not 'aA'
            new_pop.append(offspring) # adding the offspring to the new population


        a_in_pop = 0 
        for individual in new_pop:
            if individual == "Aa": # counting the number of 'a' alleles remaining in the population 
                a_in_pop += 1
            if individual == "aa":
                a_in_pop += 2

        if a_in_pop == 0: # if allele 'a' is lost from population
            break # finish the loop 
            
        n_dead = int(0.2*new_pop.count('aa')) # calculating the number of 'aa' homozygotes who don't survive 

        for count in range(n_dead):
            new_pop.remove('aa') # removing 20% of aa individuals from the population
            new_individual = random.choices(['AA', 'Aa'], k = 1) # replacing dead aa homozygotes with either Aa or AA 
            new_pop.append(*new_individual) # appending the new individual so population remains at N = pop_size
            

        f_AA = allele_freq('AA', new_pop) # calculating frequency of alleles using my defined function
        freq_AA.append(f_AA) # adding it to the frequency list
        f_Aa = allele_freq('Aa', new_pop)
        freq_Aa.append(f_Aa)
        f_aa = allele_freq('aa', new_pop)
        freq_aa.append(f_aa)


        initial_pop = new_pop # setting the new_pop to be initial pop for next iteration
    
    return freq_AA, freq_Aa, freq_aa


freq_AA, freq_Aa, freq_aa = modelDrift_A(100, 500) # calling modelDrift_A function on pop of size 100, over 500 generations

import pylab as plb

x_data = range(0,len(freq_AA))
plb.plot(x_data, freq_AA, 'r', label = 'AA')
plb.plot(x_data, freq_Aa, 'b', label = 'Aa')
plb.plot(x_data, freq_aa, 'k', label = 'aa')
plb.axis(xmin = 1, xmax = len(freq_AA))
plb.xlabel("Number of Generations")
plb.ylabel("Allele frequency in the population")
plb.title("Change in frequency of alleles 'A' and 'a' over {} generations".format(len(x_data)))
plb.legend(bbox_to_anchor=(1.05, 1),loc = 'upper left')
plb.show()

