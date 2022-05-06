from django.urls import path
from . import views

urlpatterns = [
    path('', views.VacancyViewSet.as_view({'get':'list'})),
    path('<int:pk>/', views.VacancyViewSet.as_view({'get': 'retrieve', 'patch': 'update'})),
]
