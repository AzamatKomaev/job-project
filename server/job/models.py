from django.db import models
from django.conf import settings


class Specialization(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'specializations'
        verbose_name = 'Specialization'
        verbose_name_plural = 'Specializations'


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    salary = models.PositiveIntegerField(null=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = 'vacancies'
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return self.title
