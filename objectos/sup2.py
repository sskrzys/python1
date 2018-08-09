from random import randint
import sys


class Samochod:

    def __init__(self):
        self.nazwa = "Generyczny samochod"
        self.moc = 100
        self.benzyna = 100


class Wyscigi:

    def __init__(self):
        self.samochody = list()

    def dodawanie_samochodow(self):

        def bezpieczne_wprowadzanie_mocy(proby=3):
            for proba in range(proby):
                try:
                    self.samochody[numerek].moc = int(input("Jaką moc będzie miał %s? " % self.samochody[numerek].nazwa))
                    break
                except ValueError:
                    if proba == proby - 1:
                        sys.exit("Ile razy mam powtarzac? Wychodze stąd")
                    else:
                        print("To ma byc liczba gluptasku")

        while True:
            kcesz = input("Czy chcesz wprowadzic samochod? Jak nie to wpisz \"N\"")
            if kcesz == 'N':
                break
            else:
                self.samochody.append(Samochod())
                numerek = len(self.samochody) - 1
                self.samochody[numerek].nazwa = input("Prosze nazwać jakoś samochód numer %d: " % (numerek + 1))
                bezpieczne_wprowadzanie_mocy()
            print("Samochodow jest %d " % (numerek + 1))
        for samochod in self.samochody:
            print("Samochod %s o mocy %s" % (samochod.nazwa, samochod.moc))

    def tankowanie(samochod):
        losu = randint(0, samochod.moc)
        print(losu)
        if losu < 15:
            print("Samochod %s ma przegranko bo nie dotankowal" % samochod.nazwa)
            del samochod
        else:
            samochod.benzyna = 50

    def jazda(self, samochod):
        samochod.benzyna -= randint(0, 5)
        print("Samochod %s ma jeszcze %d procent baku" % (samochod.nazwa, samochod.benzyna))
        if samochod.benzyna < 15:
            Wyscigi.tankowanie(samochod)


sciganko = Wyscigi()
autko1 = Samochod()
autko1.nazwa = "<<<rakieta koszmiczna>>>"
# Wyscigi.dodawanie_samochodow(sciganko)
for x in range(0,100):
    Wyscigi.jazda(Wyscigi, autko1)
