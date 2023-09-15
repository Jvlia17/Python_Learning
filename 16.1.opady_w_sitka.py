# 16.1 Opady w Sitka. Miejscowość Sitka leży w strefie klimatów umiarkowanych, więc dość często pada tam deszcz. W pliku znajduje się nagłówek o nazwie PRCP, który przedstawia wielkośc dziennych opadów. Utwórz wizualizację koncentrującą się na danych w tej kolumnie.

import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'data\\sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    row_headers = next(reader)

    for index, header in enumerate(row_headers):
        print(index, header)

    dates, rainfall = [], []

    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        daily_rainfall = float(row[3])
        dates.append(current_date)
        rainfall.append(daily_rainfall)

plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(10,5), dpi=128)
ax.plot(dates, rainfall)

# Formatowanie wykresu.
ax.set_title("Dzienne opady w Sitka w 2018 roku", fontsize=16)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Dzienne opady w milimetrach", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()