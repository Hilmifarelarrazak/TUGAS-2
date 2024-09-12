def check_odd_even(bilangan):
    if bilangan % 2 == 0:
        return "Bilangan genap"
    else:
        return "Bilangan ganjil"

bilangan = int(input("Masukkan bilangan: "))
print(check_odd_even(bilangan))
