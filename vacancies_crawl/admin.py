from django.contrib import admin
from vacancies_crawl.models import Vacancy


class VacancyAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'location']
    ordering = ['title']

admin.site.register(Vacancy, VacancyAdmin)
