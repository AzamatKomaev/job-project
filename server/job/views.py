from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request

from job.models import Vacancy
from job.permissions import IsOwnerOrReadOnly
from job.serializers import VacancySerializer


class VacancyViewSet(ViewSet):
    permissions = (IsOwnerOrReadOnly, )
    model = Vacancy

    def list(self, request: Request) -> Response:
        queryset = self.model.objects.all()
        serializer = VacancySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request: Request, pk: int) -> Response:
        vacancy = get_object_or_404(Vacancy, pk=pk)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

    def update(self, request: Request, pk: int) -> Response:
        vacancy = Vacancy.objects.filter(pk=pk).update(**request.data)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)
