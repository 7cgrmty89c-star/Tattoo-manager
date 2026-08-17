# asystent analizujacy profil tatuazysty i podpowiadajacy jak zdobywc klientow

print("=== TATTOO MANAGER ===")
print("witaj w programie")

liczba = int(input("ilu klientow miales w tym miesiacu: "))

if liczba < 10:

    print("\n⚠️ Masz za malo klientow. Wybierz dzialanie:")
    print("1 – Flash Day (szybkie wzory, jeden dzien)")
    print("2 – Instagram Push (7 dni postow)")
    print("3 – Program Polecen (znizka za znajomego)")

    wybor = input("\nWybierz 1, 2 lub 3: ")

    if wybor == "1":
        print("\n⚡ FLASH DAY – kroki:")
        kroki = [
            "1. Przygotuj 3-5 malych wzorow (max 1h)",
            "2. Zrob zdjecia wzorow",
            "3. Wstaw post: 'Jutro Flash Day! Pierwszy zglasza sie – pierwszy wybiera'",
            "4. Ustaw cene nizsza o 20-30%",
            "5. Na koniec dnia – relacja z pracy"
        ]
        for krok in kroki:
            print(krok)

    elif wybor == "2":
        print("\n📱 INSTAGRAM PUSH – plan 7 dni:")
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

    elif wybor == "3":
        print("\n🤝 PROGRAM POLECEN")
        print("\nZasady: Klient przyprowadza znajomego = oboje dostaja 10% znizki.")

        # Gotowa wiadomosc do klienta
        print("\n--- GOTOWA WIADOMOSC DO WYSLANIA ---")
        wiadomosc = [
            "Hej! Mam dla Ciebie propozycje 😊",
            "Przyprowadz znajomego na tatuaz, a oboje dostajecie 10% znizki!",
            "Wystarczy, ze wspomnisz o mnie lub pokazesz ten post.",
            "Daj znac jesli masz kogos zainteresowanego!",
            "----------------------------------------"
        ]
        for linia in wiadomosc:
            print(linia)

        # Symulacja liczenia polecen
        polecenia = input("\nIlu klientow w tym miesiacu przyszlo z polecenia? ")
        polecenia = int(polecenia)

        if polecenia > 0:
            print(f"\n✅ Swietnie! {polecenia} klientow to wynik polecen.")
            print("To najlepsza reklama – zadowoleni klienci polecaja dalej.")
        else:
            print("\n💡 Wskazowka: Wyslij powyzsza wiadomosc do 3 ostatnich klientow.")
            print("Program polecen to najtansza i najskuteczniejsza kampania.")

    else:
        print("Nieprawidlowy wybor. Sprobuj ponownie.")

else:
    print("\n✅ Brawo! Masz wystarczajaco klientow.")
    print("Pamietaj o:")
    print("- proszeniu o opinie")
    print("- dodawaniu zdjec na Instagram")
    print("- oferowaniu kolejnych terminow stalym klientom")

print("\nPowodzenia w biznesie! 🎨")
