from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

app_name = 'isabella'

urlpatterns = [
    path('', TemplateView.as_view(template_name='isabella/index.html'),)
]