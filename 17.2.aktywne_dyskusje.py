# 17.2 Aktywne dyskusje. Wykorzystując dane zebrane w programie hn_submissions.py, utwórz wykres słupkowy pokazujący najaktywniejsze dyskusje prowadzone obecnie w witrynie Hacker News.

from operator import itemgetter
import requests
from plotly.graph_objs import Bar
from plotly import offline

# Wykonanie wywołania API i zachowanie otrzymanej odpowiedzi.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Kod stanu: {r.status_code}")
print(r)

# Przetworzenie informacji o każdym artykule.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:

    # Przygotowanie oddzielnego wywołania API dla każdego artykułu.
    url = (f'https://hacker-news.firebaseio.com/v0/item/' +
           str(submission_id) + '.json')
    r = requests.get(url)
    print(r.status_code)
    response_dict = r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])


repo_names, comments, links = [], [], []
for submission_dict in submission_dicts:
    repo_names.append(submission_dict['title'])
    links.append(submission_dict['link'])
    comments.append(submission_dict['comments'])

# Utworzenie wizualizacji
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': comments,
    'hovertext': links,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Projekty z największą ilością komentarzy w serwisie Hacker News',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repozytorium',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Komentarze',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')