# 16.2 Porównanie miejscowości SItka i Doliny Śmierci.

import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename_sitka = 'data\\sitka_weather_2018_simple.csv'
filename_death_valley = 'data\\death_valley_2018_simple.csv'

with open(filename_sitka) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs_sitka = []

    for row in reader:
        high_sitka = int(row[5])
        highs_sitka.append(high_sitka)

with open(filename_death_valley) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs_death_valley = []
    dates = []

    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high_dv = int(row[4])
        except ValueError:
            continue
        else:
            highs_death_valley.append(high_dv)
            dates.append(current_date)

plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(10,5), dpi=128)
ax.plot(dates, highs_sitka)
ax.plot(dates, highs_death_valley)

# Formatowanie wykresu.
ax.set_title("Najwyższe temperatury w 2018 roku", fontsize=16)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperatura (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.legend(["Sitka", "Death Valley"], loc ="lower right")
plt.show()