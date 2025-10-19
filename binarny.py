def dec_to_bin(n):
    wynik = ""
    while n > 0:
        wynik = str(n % 2) + wynik
        n //= 2
    return wynik or "0"

liczba = int(input("liczba: "))

print(dec_to_bin(liczba))
