def czy_pierwsza(n):
	if n < 2:
		return False
	for i in range(2, int(n**0.5) +1):
		if n % i == 0:
		    return False
	return True


n = int(input("Podaj liczbe: "))

if czy_pierwsza(n):
	print(f"twoja liczba {n} jest pierwsza")
else:
	print(f"twoja liczba {n} nie jest pierwsza")