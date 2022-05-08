from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('users/', include('users.urls')),

    path('vacancies/', include('job.urls'))
]
