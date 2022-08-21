from rest_framework import serializers
from isabella.models import Competition, Note, Temporada


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ('id', 'competition_name', 'location',
                  'club_name', 'competition_date',)


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'note', 'competition', 'temporada',)


class TemporadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temporada
        fields = ('id', 'season')
