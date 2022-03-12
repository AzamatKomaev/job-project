from django.db import models
from django.db.models import QuerySet
from django.conf import settings


class VacancyManager(models.Manager):
    def get_filtered_queryset(self, **filter_data) -> QuerySet:
        return super().get_queryset().filter(filter_data)


class Vacancy(models.Model):
    IT = 'IT'
    EDU = 'EDU'
    HEALTH = 'HEALTH'
    CULTURE = 'CULTURE'
    SPORT = 'SPORT'
    MANAGERIAL = 'MANAGERIAL'
    ECONOMY = 'ECONOMY'

    SPHERE_CHOICES = (
        (IT, 'Information Technologies'),
        (EDU, 'Education or Science'),
        (HEALTH, 'Healthcare'),
        (CULTURE, 'Culture'),
        (SPORT, 'Sport'),
        (MANAGERIAL, 'Administrative, managerial and office activities'),
        (ECONOMY, 'Economy')
    )

    title = models.CharField('title', max_length=100)
    description = models.TextField('description')
    salary = models.FloatField('salary')
    sphere = models.CharField('sphere', max_length=100, choices=SPHERE_CHOICES)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    objects = VacancyManager()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        db_table = 'vacancies'
