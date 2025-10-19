liczba = int(input("Podaj liczbę: "))
dzielniki = []  # lista na dzielniki

for i in range(1, liczba + 1):
    if liczba % i == 0:
        dzielniki.append(i)  # dodajemy dzielnik do listy

print("Dzielniki liczby", liczba, "to:", dzielniki)
