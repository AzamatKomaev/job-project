from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.AuthViewSet.as_view({'get': 'get_me'}), name='auth.get_me'),
    path('create/', views.AuthViewSet.as_view({'post': 'create_user'}), name='auth.create_user'),
]
