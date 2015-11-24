from vacancies_crawl import models


def merge_duplicates():
    duplicates = models.Vacancy.objects.filter(is_from_stepstone=True)
    correct_vacancy = models.Vacancy.objects.filter()
