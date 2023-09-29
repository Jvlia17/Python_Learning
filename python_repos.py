import requests


def get_python_repos():
    # Wykonanie wywołania API i zachowania otrzymanej odpowiedzi.
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    return r.status_code
