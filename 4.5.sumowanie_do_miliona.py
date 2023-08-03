# 4.5 Sumowanie do miliona. Utwórz listę liczb od jednego do miliona, a następnie za pomoca funkcji min() i max() sprawdź, czy lista faktycznie zaczyna się od wartości jeden i kończy na milionie.

lista = list(range(1, 1_000_001))

print(min(lista))
print(max(lista))

print(sum(lista))