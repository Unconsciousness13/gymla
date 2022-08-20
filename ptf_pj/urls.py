from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('ptf_api.urls', namespace='ptf_api')),
    path('', include('ptf.urls'), namespace='ptf'),
]
