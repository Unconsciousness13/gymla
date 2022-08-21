from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('isabella_api.urls', namespace='isabella_api')),
    path('', include('isabella.urls', namespace='isabella')),
]
