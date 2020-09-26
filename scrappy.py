import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
res = requests.get(url)
bs = BeautifulSoup(res.text, 'html.parser')
storylinks = bs.select('.storylink')
subtexts = bs.select('.subtext')


def sort_links(lis):
    return sorted(lis, key=lambda x: x['vote'], reverse=True)


def format_links(links, texts):
    hn = []
    for idx, item in enumerate(links):
        if len(texts[idx].select('.score')):
            vote = texts[idx].select('.score')[0].getText().replace(' points', '')
            if int(vote) >= 100:
                hn.append({'text': item.getText(), 'link': item.get('href', None), 'vote': int(vote)})
    return sort_links(hn)


for dic in format_links(storylinks, subtexts):
    print(dic['text'])
    print(dic['link'])
    print(dic['vote'])




