import time
from colorama import Fore
import numpy as np
from itertools import combinations

#przegląd wyczerpujący
def exhaustive_search(mp,M):
    '''
    Metoda przeglądu wyczerpującego
    :param mp: lista przedmiotów, w której każdy przedmiot opisywany jest przez wartość (m, p)
    :param M: maksymalna masa wszystkich wykorzystanych przedmiotów
    '''
    valid_combinations = []
    #sprawdzenie wszystkich kombinacji i zebranie listy o dozwolonej masie
    for r in range(len(mp) + 1):
        for combo in combinations(mp, r):
            total_cost = sum(item[0] for item in combo)
            if total_cost <= M:
                valid_combinations.append(list(combo))

    #wybranie najlepszej kombinacji
    best_combination = None
    max_total_value = 0

    for combo in valid_combinations:
        total_value = sum(item[1] for item in combo)
        if total_value > max_total_value:
            max_total_value = total_value
            best_combination = combo

    best_combination_cost = 0
    for item in best_combination:
        best_combination_cost += item[0]
    
    return best_combination, best_combination_cost, max_total_value,

#heurestyka
def heuristic_method(mp, M):
    '''
    Metoda z użyciem heurystyki
    :param mp: lista przedmiotów, w której każdy przedmiot opisywany jest przez wartość (m, p, p/m)
    :param M: maksymalna masa wszystkich wykorzystanych przedmiotów
    '''
    mp.sort(key=lambda x: x[2], reverse=True)  #sortowanie listy przedmiotów według p/m
    plecak = []
    total_cost = 0

    for item in mp:
        if total_cost + item[0] <= M:
            plecak.append(item)
            total_cost += item[0]

    total_value = sum(item[1] for item in plecak)
    return plecak, total_cost, total_value

def main():
    # m = np.array([8, 3, 5, 2]) #masa przedmiotów
    # M = np.sum(m)/2 #niech maksymalna masa plecaka będzie równa połowie masy przedmiotów
    # p = np.array([16, 8, 9, 6]) #wartość przedmiotów

    n = 20    #25 - 140s; 24 - 60s
    m = np.random.randint(1, 30, n)
    p = np.random.randint(1, 30, n)
    M = np.sum(m)/2

    mp = []
    for i in range(len(m)):
        mp.append((m[i], p[i], p[i]/m[i]))

    print("\nDostępne przedmioty:")
    print(Fore.BLUE + f"{'m':<10}{'p':<10}{'p/m':<15}" + Fore.RESET)
    for item in mp:
        print(f"{item[0]:<10}{item[1]:<10}{item[2]:<10.2f}")
    print("Maksymalna masa plecaka (M):", M)

    #przegląd wyczerpujący
    start1 = time.perf_counter()
    best_combination, best_combination_cost, max_total_value = exhaustive_search(mp,M)
    end1 = time.perf_counter()
    total1 = end1 - start1
    
    #wypisanie kombinacji
    print(Fore.GREEN + "\nWynik przeglądu wyczerpującego" + Fore.YELLOW + " ({0:02f}s)".format(total1) + Fore.RESET)

    # Wypisanie najlepszej kombinacji
    if best_combination is not None:
        print(Fore.BLUE + f"{'m':<10}{'p':<10}{'p/m':<15}" + Fore.RESET)
        for item in best_combination:
            print(f"{item[0]:<10}{item[1]:<10}{item[2]:<10.2f}")
        print(f"Suma m: {best_combination_cost}")
        print(f"Suma p: {max_total_value}")
    else:
        print("Nie znaleziono rozwiązania")

    #heurestyka
    start2 = time.perf_counter()
    plecak, total_cost, total_value = heuristic_method(mp,M)
    end2 = time.perf_counter()
    total2 = end2 - start2

    #heurestyka
    print(Fore.GREEN + "\nWynik heurestyki" + Fore.YELLOW + " ({0:02f}s)".format(total2) + Fore.RESET)
    #Wypisanie wybranych przedmiotów
    print(Fore.BLUE + f"{'m':<10}{'p':<10}{'p/m':<15}" + Fore.RESET)
    for item in plecak:
        print(f"{item[0]:<10}{item[1]:<10}{item[2]:<10.2f}")

    print(f"Suma m: {total_cost}")
    print(f"Suma p: {total_value}")

    print(Fore.GREEN + "\nPodsumowanie:" + Fore.RESET)
    print(f"Liczba przedmiotów: {n}; M = {M}")
    print(f"Wynik przeglądu wyczerpującego: p = {max_total_value}, m = {best_combination_cost}, " + "t = {0:02f}s".format(total1))
    print(f"Wynik przy użyciu heurestyki:   p = {total_value}, m = {total_cost}, " + "t = {0:02f}s".format(total2))

if __name__ == "__main__":
    main()