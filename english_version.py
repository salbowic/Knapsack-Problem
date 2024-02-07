import time
from colorama import Fore
import numpy as np
from itertools import combinations

# exhaustive search
def exhaustive_search(items, max_weight):
    '''
    Exhaustive search method
    :param items: list of items, where each item is described by a tuple (weight, value)
    :param max_weight: maximum total weight of the items used
    '''
    valid_combinations = []
    # check all combinations and collect those within the allowed weight
    for r in range(len(items) + 1):
        for combo in combinations(items, r):
            total_weight = sum(item[0] for item in combo)
            if total_weight <= max_weight:
                valid_combinations.append(list(combo))

    # select the best combination
    best_combination = None
    max_total_value = 0

    for combo in valid_combinations:
        total_value = sum(item[1] for item in combo)
        if total_value > max_total_value:
            max_total_value = total_value
            best_combination = combo

    best_combination_weight = 0
    for item in best_combination:
        best_combination_weight += item[0]
    
    return best_combination, best_combination_weight, max_total_value,

# heuristic method
def heuristic_method(items, max_weight):
    '''
    Method that use heuristic to find the solution
    :param items: list of items, where each item is described by a tuple (weight, value, value/weight)
    :param max_weight: maximum total weight of the items used
    '''
    items.sort(key=lambda x: x[2], reverse=True)  # sort items by value/weight
    backpack = []
    total_weight = 0

    for item in items:
        if total_weight + item[0] <= max_weight:
            backpack.append(item)
            total_weight += item[0]

    total_value = sum(item[1] for item in backpack)
    return backpack, total_weight, total_value

def main():
    # Example items
    n = 20    # For 25 items - 140s; for 24 - 60s
    weights = np.random.randint(1, 30, n)
    values = np.random.randint(1, 30, n)
    max_weight = np.sum(weights)/2

    items = []
    for i in range(len(weights)):
        items.append((weights[i], values[i], values[i]/weights[i]))

    print("\nAvailable items:")
    print(Fore.BLUE + f"{'weight':<10}{'value':<10}{'value/weight':<15}" + Fore.RESET)
    for item in items:
        print(f"{item[0]:<10}{item[1]:<10}{item[2]:<10.2f}")
    print("Maximum backpack weight (max_weight):", max_weight)

    # exhaustive search
    start1 = time.perf_counter()
    best_combination, best_combination_weight, max_total_value = exhaustive_search(items, max_weight)
    end1 = time.perf_counter()
    total1 = end1 - start1
    
    # printing the combination
    print(Fore.GREEN + "\nExhaustive search result" + Fore.YELLOW + " ({0:02f}s)".format(total1) + Fore.RESET)

    # Print the best combination
    if best_combination is not None:
        print(Fore.BLUE + f"{'weight':<10}{'value':<10}{'value/weight':<15}" + Fore.RESET)
        for item in best_combination:
            print(f"{item[0]:<10}{item[1]:<10}{item[2]:<10.2f}")
        print(f"Total weight: {best_combination_weight}")
        print(f"Total value: {max_total_value}")
    else:
        print("No solution found")

    # heuristic method
    start2 = time.perf_counter()
    backpack, total_weight, total_value = heuristic_method(items, max_weight)
    end2 = time.perf_counter()
    total2 = end2 - start2

    # heuristic result
    print(Fore.GREEN + "\nHeuristic result" + Fore.YELLOW + " ({0:02f}s)".format(total2) + Fore.RESET)
    # Print selected items
    print(Fore.BLUE + f"{'weight':<10}{'value':<10}{'value/weight':<15}" + Fore.RESET)
    for item in backpack:
        print(f"{item[0]:<10}{item[1]:<10}{item[2]:<10.2f}")

    print(f"Total weight: {total_weight}")
    print(f"Total value: {total_value}")

    print(Fore.GREEN + "\nSummary:" + Fore.RESET)
    print(f"Number of items: {n}; max_weight = {max_weight}")
    print(f"Exhaustive search result: value = {max_total_value}, weight = {best_combination_weight}, " + "time = {0:02f}s".format(total1))
    print(f"Heuristic method result:   value = {total_value}, weight = {total_weight}, " + "time = {0:02f}s".format(total2))

if __name__ == "__main__":
    main()
