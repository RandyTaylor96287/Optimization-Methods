import random
import math
import matplotlib.pyplot as plt

def initialize_population(population_size, number_of_genes):
    population = [[random.randint(0,1) for gene_index in range(number_of_genes)] for chromosome_index in range(population_size)]
    return population

def decode_chromosome(chromosome, number_of_variables, maximum_variable_value):
    number_of_genes = len(chromosome)
    k = int(number_of_genes / number_of_variables)
    
    x = []
    
    for i in range(number_of_variables):
        x_temp = 0
        start_index = i * k
        for j in range(k):
            gene_index = start_index + j
            x_temp += chromosome[gene_index] * pow(2, -j-1)
        x_temp = -maximum_variable_value + 2 * maximum_variable_value * x_temp / (1 - pow(2, -k))
        x.append(x_temp)
    
    return x

def evaluate_individual(x):
    x_1 = x[0]
    x_2 = x[1]

    first_term = (1.5 - x_1 + x_1 * x_2) ** 2
    second_term = (2.25 - x_1 + x_1 * (x_2) ** 2) ** 2 
    third_term = (2.625 - x_1 + x_1 * (x_2) ** 3) ** 2

    denominator = 1 + first_term + second_term + third_term
    f = 1 / denominator
    
    return f

def tournament_select(fitness_list, tournament_probability, tournament_size):
    population_size = len(fitness_list)
    individual = []

    for i in range(tournament_size):
        individual.append(random.randint(0, population_size - 1))

    for i in range(tournament_size):
        for j in range(i+1, tournament_size):
            if fitness_list[individual[j]] > fitness_list[individual[i]]:
                individual[i], individual[j] = individual[j], individual[i]

    for i in range(tournament_size):
        r = random.random()
        if r < tournament_probability or i == tournament_size - 1:
            return individual[i]
    
    return individual[0]

def cross(chromosome1, chromosome2):
    number_of_genes = len(chromosome1)
    cross_point = random.randint(1, number_of_genes - 1)

    new_chromosome_1 = chromosome1[:cross_point] + chromosome2[cross_point:]
    new_chromosome_2 = chromosome2[:cross_point] + chromosome1[cross_point:]

    return [new_chromosome_1, new_chromosome_2]

def mutate(chromosome, mutation_probability):
    number_of_genes = len(chromosome)
    mutated_chromosome = chromosome.copy()
    for gene_index in range(number_of_genes):
        r = random.random()
        if r < mutation_probability:
            mutated_chromosome[gene_index] = 1 - chromosome[gene_index]

    return mutated_chromosome

def run_function_optimization(population_size, number_of_genes, number_of_variables, maximum_variable_value,
                              tournament_size, tournament_probability, crossover_probability,
                              mutation_probability, number_of_generations):
    
  population = initialize_population(population_size,number_of_genes)

  for generation_index in range(number_of_generations):
    maximum_fitness = 0
    best_chromosome = []
    best_individual = []
    fitness_list = []
    for chromosome in population:
      individual = decode_chromosome(chromosome,number_of_variables,maximum_variable_value)
      fitness = evaluate_individual(individual)
      if (fitness > maximum_fitness):
        maximum_fitness = fitness
        best_chromosome = chromosome.copy()  
        best_individual = individual.copy()
      fitness_list.append(fitness)

    temp_population = []
    for i in range(0,population_size,2):
      index_1 = tournament_select(fitness_list, tournament_probability, tournament_size)
      index_2 = tournament_select(fitness_list, tournament_probability, tournament_size)
      chromosome1 = population[index_1].copy()
      chromosome2 = population[index_2].copy()
      r = random.random()
      if r < crossover_probability:
        [new_chromosome_1, new_chromosome_2] = cross(chromosome1,chromosome2)
        temp_population.append(new_chromosome_1)
        temp_population.append(new_chromosome_2) 
      else:
        temp_population.append(chromosome1)
        temp_population.append(chromosome2)

    for i in range(population_size):
      original_chromosome = temp_population[i]

      mutated_chromosome = mutate(original_chromosome, mutation_probability)
      temp_population[i] = mutated_chromosome

    temp_population[0] = best_chromosome
    population = temp_population.copy()

  return [maximum_fitness, best_individual]



