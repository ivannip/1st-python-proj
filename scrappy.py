import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
res = requests.get(url)
bs = BeautifulSoup(res.text, 'html.parser')
storylinks = bs.select('.storylink')
subtexts = bs.select('.subtext')


def format_links(links, texts):
    hn = []
    for idx, item in enumerate(links):
        if len(texts[idx].select('.score')):
            vote = texts[idx].select('.score')[0].getText().replace(' points', '')
            if int(vote) >= 100:
                hn.append({'text': item.getText(), 'link': item.get('href', None), 'vote': int(vote)})
    return hn


print(format_links(storylinks, subtexts))

