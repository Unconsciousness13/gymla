from rest_framework import generics
from isabella.models import Competition, Temporada
from .serializers import CompetitionSerializer,  TemporadaSerializer

class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

class CompetitionDetail(generics.RetrieveDestroyAPIView):
     queryset = Competition.objects.all()
     serializer_class = CompetitionSerializer


class TemporadaList(generics.ListCreateAPIView):
    queryset = Temporada.objects.all()
    serializer_class = TemporadaSerializer


class TemporadaDetail(generics.RetrieveDestroyAPIView):
     queryset = Temporada.objects.all()
     serializer_class = TemporadaSerializer