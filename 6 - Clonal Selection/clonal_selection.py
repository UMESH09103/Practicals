import random
import matplotlib.pyplot as plt

# -------------------------------
# Fitness Function (maximize x^2)
# -------------------------------
def fitness(x):
    return x ** 2


# -------------------------------
# Initialize Population
# -------------------------------
def init_population(size, lower, upper):
    return [random.uniform(lower, upper) for _ in range(size)]


# -------------------------------
# Mutation with Boundary Control
# -------------------------------
def mutate(x, lower, upper):
    x = x + random.uniform(-1, 1)
    
    # 🔥 Enforce bounds
    x = max(lower, min(x, upper))
    
    return x


# -------------------------------
# Clone and Mutate
# -------------------------------
def clone_and_mutate(population, clone_factor, lower, upper):
    clones = []
    for x in population:
        for _ in range(clone_factor):
            mutated = mutate(x, lower, upper)
            clones.append(mutated)
    return clones


# -------------------------------
# Selection (Best Individuals)
# -------------------------------
def select_best(population, size):
    return sorted(population, key=fitness, reverse=True)[:size]


# -------------------------------
# Parameters
# -------------------------------
POP_SIZE = 5
GENERATIONS = 10
CLONE_FACTOR = 3
LOWER, UPPER = -10, 10


# -------------------------------
# Run Algorithm
# -------------------------------
population = init_population(POP_SIZE, LOWER, UPPER)

best_fitness_history = []

for gen in range(GENERATIONS):
    clones = clone_and_mutate(population, CLONE_FACTOR, LOWER, UPPER)
    
    # Combine original + clones
    combined = population + clones
    
    # Select best individuals
    population = select_best(combined, POP_SIZE)
    
    best = population[0]
    best_fitness_history.append(fitness(best))
    
    print(f"Generation {gen+1}, Best Solution: {best:.4f}, Fitness: {fitness(best):.4f}")

# Final Result
print("\nFinal Best Solution:", population[0])
print("Final Fitness:", fitness(population[0]))


# -------------------------------
# Plot Graph (VERY IMPORTANT)
# -------------------------------
plt.plot(best_fitness_history, marker='o')
plt.title("Fitness vs Generations")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.grid()
plt.show()