#1
imie = input("Podaj imie: ")
print("Witaj", imie)
#2
wiek = input("Podaj wiek: ")
print("Twój wiek to:", wiek)
#3
nazwisko = input("Podaj nazwisko: ")
imie1= imie[0]
nazwisko1 = nazwisko[0]
inicjaly= (imie1+"."+nazwisko1).upper()
print(inicjaly)
#4
tekst=input("Podaj tekst: ")
wynik=tekst*5
print(wynik)
#5
tekst1=input("Podaj tekst1: ")
tekst2=input("Podaj tekst2: ")
wynik1=tekst1+tekst2
print(wynik1)
#6
tekst3=input("Podaj tekst3: ")
tekst4=input("Podaj tekst4: ")
polowa1=len(tekst3)//2
polowa2=len(tekst4)//2
wynik1=tekst3[:polowa1]+tekst4[polowa2:]
print(wynik1)