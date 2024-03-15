var1 = int(input("введите сумму в ruble "))
valuta = str(input("введите валюту, в которую переведем (yuan, dollar, euro) "))
if valuta == "Yuan" or valuta == "yuan":
    val = var1 * 0.001327
    print(f"{var1} ruble = {val} yuan")
elif valuta == "Dollar" or valuta == "dollar":
    val = var1 * 0.011
    print(f"{var1} ruble = {val} dollar")
elif valuta == "E1uro" or valuta == "euro":
    val = var1 * 0.011
    print(f"{var1} ruble = {val} euro")