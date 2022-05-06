from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.response import Response

from core.views import ListRetrieveViewSet
from .serializers import UserSerializer
from .permissions import AuthPermission

User = get_user_model()


class AuthViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer
    permission_classes = (AuthPermission, )

    def get_me(self, request):
        self.check_permissions(request)
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)

    def create_user(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserListRetrieveView(ListRetrieveViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
