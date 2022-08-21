from rest_framework import serializers
from isabella.models import Competition, Note , Temporada

class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note

class TemporadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temporada