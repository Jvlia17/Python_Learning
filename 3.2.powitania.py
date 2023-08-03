# 3.2 Powitania. Rozpocznij od listy utworzonej w ćwiczeniu 3.1, ale zamiast samego imiona osoby wyświtl komunikat, który będzie jej dotyczył. Tekst wszystkich komunikatów powinien pozostać taki sam, ale mają być one spersonalizowane dzięki wykorzystaniu imienia konkretnej osoby.

names = ["szymon", "ania", "mola", "pola"]

print(f"Witaj, przyjacielu {names[0].title()}")
print(f"Hejka, {names[1].title()}")
print(f"Dzień dobry, {names[-1].title()} i {names[-2].title()}")