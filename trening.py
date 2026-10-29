def oblicz_koszt(cena_za_godzine, liczba_minut):
    if cena_za_godzine < 0:
        raise ValueError("Cena nie moze byc ujemna.")

    if liczba_minut <= 0:
        raise ValueError("Czas treningu musi byc dodatni.")

    return round(cena_za_godzine * liczba_minut / 60, 2)