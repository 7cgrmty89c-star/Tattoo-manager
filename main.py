# asystent analizujacy profil tatuazysty i podpowiadajacy jak zdobywc klientow
import random
# ----funkcje----
def pokaz_porade():
    """Losuje i wyswietla jedna porade dnia."""
    porada = random.choice(porady_dnia)
    print(f"\n💡 PORADA DNIA: {porada}")
# ----dane----
porady_dnia = [
    "Odpowiadaj na wiadomosci klientow w ciagu 24h - to buduje zaufanie.",
    "Rob zdjecia gotowych tatuazy w dobrym swietle, to Twoja najlepsza reklama.",
    "Zapytaj stalych klientow o opinie - to za darmo, a dziala lepiej niz reklama.",
    "Pokazuj proces pracy w Stories - ludzie uwielbiaja 'kulisy'.",
    "Nie badz za tani - niska cena przyciaga klientow, ktorzy nie doceniaja jakosci."]

def pokaz_historie():
    """Wczytuje i wyswietla zawartosc pliku historia.txt, jesli istnieje."""
    print("\n📂 HISTORIA POPRZEDNICH WPISOW:")
    try:
        plik = open("historia.txt", "r")
        zawartosc = plik.read()
        plik.close()
        if zawartosc == "":
            print("(brak wpisow - to Twoje pierwsze uruchomienie)")
        else:
            print(zawartosc)
    except FileNotFoundError:
        print("(brak wpisow - to Twoje pierwsze uruchomienie)")

def zbierz_dane_klienta():
    """Pyta o liczbe klientow w miesiacu, waliduje i zapisuje do historia.txt."""
    while True:
        try:
            liczba = int(input("ilu klientow miales w tym miesiacu?"))
            if liczba < 0:
                print("⚠️ Liczba klientow nie moze byc ujemna. Sprobuj ponownie.")
                continue
            break
        except ValueError:
            print("⚠️ To nie jest liczba. Sprobuj ponownie.")

    plik = open("historia.txt", "a")
    plik.write(f"Liczba klientow: {liczba}\n")
    plik.close()

    return liczba

def program_polecen():
    """Pokazuje zasady polecen, gotowa wiadomosc do klienta oraz zbiera i zapisuje liczbe polecen."""
    print("\n🤝 PROGRAM POLECEN")
    print("\nZasady: Klient przyprowadza znajomego = oboje dostaja 10% znizki.")
    print("\n--- GOTOWA WIADOMOSC DO WYSLANIA ---")
    wiadomosc = [
        "Hej! Mam dla Ciebie propozycje 😊",
        "Przyprowadz znajomego na tatuaz, a oboje dostajecie 10% znizki!",
        "Wystarczy, ze wspomnisz o mnie lub pokazesz ten post.",
        "Daj znac jesli masz kogos zainteresowanego!",
        "-----------------------------------------"
    ]
    for linia in wiadomosc:
        print(linia)

    while True:
        try:
            polecenia = int(input("\nIlu klientow w tym miesiacu przyszlo z polecenia? "))
            if polecenia < 0:
                print("⚠️ Liczba polecen nie moze byc ujemna. Sprobuj ponownie.")
                continue
            break
        except ValueError:
            print("⚠️ To nie jest liczba. Sprobuj ponownie.")

    plik = open("historia.txt", "a")
    plik.write(f"Polecenia: {polecenia}\n")
    plik.close()

    if polecenia > 0:
        print(f"\n✅ Swietnie! {polecenia} klientow to wynik polecen.")
        print("To najlepsza reklama – zadowoleni klienci polecaja dalej.")
    else:
        print("\n💡 Wskazowka: Wyslij powyzsza wiadomosc do 3 ostatnich klientow.")
        print("Program polecen to najtansza i najskuteczniejsza kampania.")

def flash_day():
    """Wyswietla liste krokow do zorganizowania Flash Day."""
    print("\n⚡ FLASH DAY - kroki:")
    kroki = [
        "1. Przygotuj 3-5 malych wzorow (max 1h)",
        "2. Zrob zdjecia wzorow",
        "3. Wstaw post: 'Jutro Flash Day! Pierwszy zglasza sie - pierwszy wybiera'",
        "4. Ustaw cene nizsza o 20-30%",
        "5. Na koniec dnia - relacja z pracy"
    ]
    for krok in kroki:
        print(krok)

def instagram_push():
    """Wyswietla 7-dniowy plan postow na Instagram."""
    print("\n📱 INSTAGRAM PUSH - plan 7 dni:")
    dni = [
        "Dzien 1: Post before/after + pytanie w opisie",
        "Dzien 2: Stories z procesu pracy",
        "Dzien 3: Post z opinia klienta",
        "Dzien 4: Stories: 'Pytajcie o wzory w DM'",
        "Dzien 5: Post 'wolne terminy' z kalendarzem",
        "Dzien 6: Reels/TikTok z procesu",
        "Dzien 7: Podsumowanie tygodnia"
    ]
    for dzien in dni:
        print(dzien)

def gratulacje():
    """Wyswietla gratulacje i przypomnienia dla osob z wystarczajaca liczba klientow."""
    print("\n✅ Brawo! Masz wystarczajaco klientow.")
    print("Pamietaj o:")
    print("- proszeniu o opinie")
    print("- dodawaniu zdjec na Instagram")
    print("- oferowaniu kolejnych terminow stalym klientom")

# ----start programu----
pokaz_porade()

print("=== TATTOO MANAGER ===")
print("witaj w programie")

pokaz_historie()

liczba = zbierz_dane_klienta()

if liczba < 10:

    print("\n⚠️ Masz za malo klientow. Wybierz dzialanie:")
    print("1 - Flash Day (szybkie wzory, jeden dzien)")
    print("2 - Instagram Push (7 dni postow)")
    print("3 - Program Polecen (znizka za znajomego)")

    while True:
        wybor = input("\nWybierz 1, 2 lub 3: ")
        if wybor == "1" or wybor == "2" or wybor == "3":
            break
        else:
            print("⚠️ Nieprawidlowy wybor. Wpisz 1, 2 lub 3.")

    if wybor == "1":
        flash_day()

    elif wybor == "2":
        instagram_push()

    elif wybor == "3":
        program_polecen()

else:
    gratulacje()
