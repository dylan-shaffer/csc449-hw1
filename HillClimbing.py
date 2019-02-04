import numpy
import random
import math
import matplotlib.pyplot as plt
import collections


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


# Print out the current value and next potential value
def print_stats(x):
    print("Current Max: " + "{:.8f}".format(x) + ": " + "{:.8f}".format(evaluate(x)))
    print("\n\n")


# Random initialization hill climbing to find maximum value of evaluated function
def hill_climbing(epochs):

    current = random.random()
    itr = 1
    improvement_made = True

    while(itr < epochs and improvement_made):
        x_prime = current + 0.0001

        if (evaluate(x_prime) > evaluate(current)):
            current = x_prime
            improvement_made = True
        else:
            improvement_made = False

        itr += 1

    return current


# Iterative hill climbing algorithm
def iterative_hill_climbing(generations, epochs):
    itr = 1
    best = 0
    best_list = [(itr, evaluate(best))]

    while(itr < generations):
        current = hill_climbing(epochs)

        if (evaluate(current) > evaluate(best)):
            best = current
            print(itr)
            print_stats(best)
            best_list.append((itr, evaluate(best)))
        
        itr += 1
    
    x, y = zip(*best_list)

    plt.plot(x, y)
    plt.show()

    return best


max_value = iterative_hill_climbing(500, 50)

x = numpy.arange(0.0, 1.0, 0.01)
func = numpy.float_power(2, -2 * numpy.float_power(((x - 0.1) / 0.9), 2)) * numpy.float_power(numpy.sin(5 * numpy.pi * x), 6)
line, = plt.plot(x, func)

plt.annotate("Max\n" + "{:.2f}".format(max_value) + ", " + "{:.2f}".format(evaluate(max_value)), xy=(max_value, evaluate(max_value)), xytext=(0.75, 0.9), arrowprops=dict(facecolor='black', shrink=0.01))

plt.show()



