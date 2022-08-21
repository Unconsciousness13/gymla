from rest_framework import generics
from isabella.models import Competition, Note , Temporada
from .serializers import CompetitionSerializer, NoteSerializer , TemporadaSerializer

class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class TemporadaList(generics.ListCreateAPIView):
    queryset = Temporada.objects.all()
    serializer_class = TemporadaSerializer
    