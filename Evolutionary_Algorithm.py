import numpy as np
import matplotlib.pyplot as plt
import random
import math

#  Computer the tour length
def evaluate(cities):
    distance = 0
    for index in range(len(cities)):
        a = cities[index]
        if index == len(cities) - 1:
            b = cities[0]
        else:
            b = cities[index + 1]

        distance += np.linalg.norm(a - b)
        index += 1

    return distance


def initialize_population(cities_number):
    pop = []
    i = 0

    while i < cities_number * 10:
        pop.append((np.random.rand(cities_number) * cities_number * 10).astype(int))
        i += 1

    return pop


def convert_sequence_to_solution(sequence, cities_number, cities):
    temp_cities = cities
    new_solution = np.zeros(shape=(cities_number, 2)).astype(int)
    i = 0

    while i < cities_number:
        index = sequence[i]
        if ((cities_number - (i + 1)) <= 0):
            index = 0
        else:
            index = index % (cities_number - (i + 1))
        
        new_solution[i] = temp_cities[index]
        temp_cities = np.delete(temp_cities, index, 0)
        i += 1

    return new_solution


def evalutate_population(population, cities_number, cities):
    pop_eval = {}

    for item in population:
        current_path = convert_sequence_to_solution(item, cities_number, cities)
        distance = evaluate(current_path)
        pop_eval[distance] = item

    ranked_population = np.zeros(shape=(cities_number * 10, cities_number)).astype(int)
    keys = sorted(pop_eval.keys(), reverse=False)
    i = 0

    for key in keys:
        ranked_population[i] = pop_eval[key]
        i += 1

    return ranked_population


def find_best(population, cities_number, cities):
    best = 0
    best_sol = []
    for x in population:
        value = evaluate(convert_sequence_to_solution(x, cities_number, cities))
        if value > best:
            best = value
            best_sol = x

    return best_sol
    

def natural_selection(population, cities_number, cities):
    reduced_pop = []
    x = 0

    while x < 10:
        reduced_pop.append(population[x])
        x += 1

    return reduced_pop


def select(population, cities_number, cities):
    i = 0
    total = 0.0

    prob = np.random.random()
    
    for x in population:
        total += evaluate(convert_sequence_to_solution(x, cities_number, cities))

    value = 0
    while value < prob:
        value += evaluate(convert_sequence_to_solution(population[i], cities_number, cities)) / total
        i += 1

    return i


def variate(population, cities_number):
    population = mutate(population, cities_number)
    population = recombination(population, cities_number)

    return population


def recombination(population, cities_number):
    new_pop = population
    i = 0

    while i < 100:
        index1 = int(np.random.randint(0, 15))
        index2 = int(np.random.randint(0, 15))
        split = int(np.random.randint(1, len(new_pop[0])))

        parent1 = new_pop[index1]
        parent2 = new_pop[index2]

        gene1 = parent1[:split]
        gene2 = parent2[split:]

        child = np.append(gene1, gene2, 0)
        new_pop = np.insert(new_pop, len(new_pop) - 1, child, 0)
        i += 1

    return new_pop


def mutate(population, cities_number):
    new_pop = population
    i = 0
    
    while i < 100:
        index = int(np.random.randint(0, 9))
        mutant = population[index]
        
        mutant = swap(mutant)

        new_pop = np.insert(new_pop, len(new_pop) - 1, mutant, 0)
        i += 1

        
    return new_pop


def swap(x):
    index = int(np.random.randint(0, len(x) - 2))
    index2 = int(np.random.randint(0, len(x) - 1))

    y = np.copy(x)

    temp = np.copy(y[index])
    y[index] = np.copy(y[index2])
    y[index2] = np.copy(temp)

    return y




def main(cities, cities_number):
    population = initialize_population(cities_number)
    no_improvement_count = 0
    continue_search = True
    i = 0
    
    population = evalutate_population(population, cities_number, cities)
    population = natural_selection(population, cities_number, cities)
    current_best = population[0]

    while continue_search:
        population = variate(population, cities_number)
        population = evalutate_population(population, cities_number, cities)
        population = natural_selection(population, cities_number, cities)

        new_solution = population[0]

        if evaluate(convert_sequence_to_solution(current_best, cities_number, cities)) > evaluate(convert_sequence_to_solution(new_solution, cities_number, cities)):
            current_best = new_solution
            print(evaluate(convert_sequence_to_solution(current_best, cities_number, cities)))
            plot(convert_sequence_to_solution(current_best, cities_number, cities), path = 1, wait = 0)
            no_improvement_count = 0
        else:
            no_improvement_count += 1

        i += 1

        if no_improvement_count > 500:
            continue_search = False

    return convert_sequence_to_solution(current_best, cities_number, cities)


def plot(cities, path, wait):
    plt.clf()
    if (path == 1):
        plt.plot(cities[:, 0], cities[:, 1], color='red', zorder=0)
    plt.scatter(cities[:, 0], cities[:, 1], marker='o')
    plt.axis('off')
    if (wait == 0):  plt.ion()
    plt.show()
    plt.pause(.001)



cities_number = 40
cities = (np.random.rand(cities_number, 2) * 100).astype(int)
plot(cities ,path = 0, wait = 1)
cities = main(cities, cities_number)
plt.ioff()
plot(cities,path = 1, wait = 1)
