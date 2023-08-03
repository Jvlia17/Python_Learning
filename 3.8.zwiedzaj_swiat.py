"""
imiona = ["Szymon", "Ania", "Julia", "Konrad"]

imiona.sort() # posortowane normalnie trwałe
print(imiona)

imiona.sort(reverse = True) # posortowane w odwrotnej kolejności trwałe
print(imiona)

print(sorted(imiona)) # posortowanie tylko do wyświtlenia, nie wpływa na listę

imiona.reverse() # zamienienie kolejnością (nie alfabetyczną!) listy
print(imiona)
imiona.reverse() # powrót do normalnej kolejności

print(len(imiona)) # długośc listy
"""

# 3.8 Zwiedzaj świat. Pomyśl o pięciu miejscach na świecie, które chciałbyś zwiedzić, a następnie wykonaj kilka poleceń.

miejsca = ["Toronto", "Ottawa", "Brisbane", "Sydney", "Melbourne"]

print(f"Lista początkowa: {miejsca}")
print(sorted(miejsca))
print(f"Lista początkowa: {miejsca}")
print(sorted(miejsca, reverse = True))
print(f"Lista początkowa: {miejsca}")
miejsca.reverse()
print(miejsca)
miejsca.reverse()
print(f"Lista początkowa: {miejsca}")
miejsca.sort()
print(miejsca)
miejsca.sort(reverse=True)
print(miejsca)