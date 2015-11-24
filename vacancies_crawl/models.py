from django.db import models


class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    is_from_monster = models.BooleanField(default=False)
    is_from_stepstone = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s - %s'%(self.company, self.title)
