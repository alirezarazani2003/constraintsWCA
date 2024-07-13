
import random
import matplotlib.pyplot as plt
import numpy as np
#function we want to optimize:
def objective_function(x):
    return x**2 + 3*x - 5

#constraint:
def is_feasible(x):
    # Check if x satisfies the constraint: 0 <= x <= 10
    return 0 <= x <= 10

def water_cycle_algorithm(max_iterations=100, population_size=50, step_size=0.1):
    # Initialize water drops randomly within the feasible range
    water_drops = [random.uniform(0, 10) for _ in range(population_size)]

    # Lists to store best solutions and fitness values
    best_solutions = []
    best_fitness_values = []

    # Main loop
    for iteration in range(max_iterations):
        # Evaporation: Randomly select some water drops to evaporate
        evaporation_count = int(0.1 * population_size)
        random.shuffle(water_drops)
        evaporated_drops = water_drops[:evaporation_count]

        # Precipitation: Move the remaining water drops towards better positions
        for i in range(population_size - evaporation_count):
            current_drop = water_drops[i]
            new_position = current_drop + step_size * random.uniform(-1, 1)
            if is_feasible(new_position):
                water_drops[i] = new_position

        # Update best solution
        best_solution = min(water_drops, key=objective_function)
        best_solutions.append(best_solution)
        best_fitness_values.append(objective_function(best_solution))

    return best_solutions, best_fitness_values

if __name__ == "__main__":
    best_solutions, best_fitness_values = water_cycle_algorithm()
    final_best_x = best_solutions[-1]
    final_best_value = objective_function(final_best_x)
    print(f"Best solution: x = {final_best_x:.2f}, f(x) = {final_best_value:.2f}")
    # Plot the fitness values over iterations
    plt.figure(figsize=(8, 6))
    plt.plot(best_fitness_values, label="Best Fitness Value")
    plt.xlabel("Iteration")
    plt.ylabel("Fitness Value")
    plt.title("Water Cycle Algorithm Optimization")
    plt.legend()
    plt.grid(True)
    plt.show()