from rest_framework import serializers
from isabella.models import Competition,  Temporada


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ('id', 'competition_name', 'location',
                  'club_name', 'competition_date', 'season_id',)



class TemporadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temporada
        fields = ('id', 'season')
