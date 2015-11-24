from django.views.generic import ListView
from vacancies_crawl import models


class ListVacancies(ListView):
    queryset = models.Vacancy.objects.all()
    paginate_by = 12
    allow_empty = True
    template_name = 'index.html'
