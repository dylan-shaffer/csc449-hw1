import numpy
import random
import math
import matplotlib.pyplot as plt


# Evaluate function value
def evaluate(x):
    value = 0
    exponent = (x - 0.1)/0.9
    exponent = math.pow(exponent, 2)
    exponent = exponent * -2
    trigTerm = math.sin(5 * (math.pi) * x)
    trigTerm = math.pow(trigTerm, 6)

    value = math.pow(2, exponent)
    value = value * trigTerm

    return value


def print_stats(x):
    print("Current Max: " + "{:.3f}".format(x) + ", " + "{:.8f}".format(evaluate(x)))
    print("\n\n")


# Simulated annealing algorithm
def simulated_annealing(init_val):
    temperature = 800
    cooling_factor = 0.001
    x = init_val
    current_energy = evaluate(init_val)
    i = 1
    best_list = [(i, current_energy)]

    while temperature > 0.01:
        x_prime = x + 0.001
        new_energy = evaluate(x_prime)

        if (new_energy >= current_energy):
            x = x_prime
            current_energy = new_energy
            best_list.append((i, current_energy))
        elif (random.random() > math.exp((current_energy - new_energy) / temperature)):
            x = x_prime
            current_energy = new_energy
            best_list.append((i, current_energy))
        
        temperature = temperature - i * cooling_factor
        i += 1

    x_coor, y = zip(*best_list)

    plt.plot(x_coor, y)
    plt.show()
    
    return x

        



max_value = simulated_annealing(0)

x = numpy.arange(0.0, 1.0, 0.01)
func = numpy.float_power(2, -2 * numpy.float_power(((x - 0.1) / 0.9), 2)) * numpy.float_power(numpy.sin(5 * numpy.pi * x), 6)
line, = plt.plot(x, func)

plt.annotate("Max\n" + "{:.3f}".format(max_value) + ", " + "{:.5f}".format(evaluate(max_value)), xy=(max_value, evaluate(max_value)), xytext=(0.75, 0.9), arrowprops=dict(facecolor='black', shrink=0.01))

plt.show()
