from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('trademe_api.urls', namespace='trademe_api')),
    path('', include('trademe.urls', namespace='trademe')),
]
