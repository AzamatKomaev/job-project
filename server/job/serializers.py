from rest_framework.serializers import ModelSerializer

from job.models import Vacancy


class VacancySerializer(ModelSerializer):

    class Meta:
        model = Vacancy
        fields = '__all__'
