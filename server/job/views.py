from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework import permissions


class VacancyViewSet(ViewSet):
    permissions = (permissions.IsAuthenticatedOrReadOnly, )

    def list(self, request: Request) -> Response:
        pass
