from urlparse import urljoin
from bs4 import BeautifulSoup
import requests
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'gsoft.settings')
from vacancies_crawl import models

url = 'http://www.stepstone.se/lediga-jobb-i-hela-sverige/data-it/'

for num_page in range(1, 10):
    print "now I crawl - %s page."% num_page
    page = {
        'sida': num_page,
    }
    response = requests.get(urljoin(url, '%s%s' % (page.keys(), page['sida'])))
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('div', attrs={'data-ajax': 'article-list'})
    rows = table.find_all('div', attrs={'class': 'description'})

    for row in rows:
        title = row.h5.get_text()
        company = row.span.get_text()
        location = row.find_all('span', attrs={'class': 'text-opaque'})[1].get_text()

        vacancy, created = models.Vacancy.objects.get_or_create(
            title=title,
            company=company,
            location=location,
        )
        vacancy.is_from_stepstone = True
        vacancy.save()

print 'Crawl %s Successfully completed' % url
