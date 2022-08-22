from django.urls import path
from .views import CompetitionList,  TemporadaList , CompetitionDetail ,  TemporadaDetail 

app_name = 'isabella_api'

urlpatterns = [
    path('competitions/', CompetitionList.as_view(), name='competition_list'),
    path('competitions/<int:pk>/', CompetitionDetail.as_view(), name='competition_detail'),
    path('temporadas/', TemporadaList.as_view(), name='temporadas_list'),
    path('temporadas/<int:pk>/', TemporadaDetail.as_view(), name='temporada_detail'),
]
