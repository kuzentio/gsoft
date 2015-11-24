from bs4 import BeautifulSoup
import requests
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'gsoft.settings')
from vacancies_crawl import models

url = 'http://jobb.monster.se/browse/Data-IT_4'

for num_page in range(1, 10):
    print "now I crawl - %s page." % num_page
    page = {
        'pg': num_page,
    }
    response = requests.get('http://jobb.monster.se/browse/Data-IT_4?%s=%s' % (page.keys(), page['pg']))
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('div', attrs={'id': 'listings'})
    rows = table.find_all('tr')

    for row in rows:
        try:
            row['class']
        except KeyError:
            continue
        if 'Hidden' in row['class']:
            continue
        data = row.find_all('a')
        try:
            title = row.find_all('a')[0].get_text()
            company = row.find_all('a')[1].get_text()
            location = row.find_all('a')[3].get_text()
        except:
            continue

        vacancy, created = models.Vacancy.objects.get_or_create(
            title=title,
            company=company,
            location=location,
        )
        vacancy.is_from_monster = True
        vacancy.save()

print 'crawl %s Successfully completed' % url
