from django.db import models


class Temporada(models.Model):
    season = models.CharField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return self.season

class Competition(models.Model):
    competition_name = models.CharField(
        max_length=50, blank=False, unique=True)
    location = models.CharField(max_length=50, blank=False)
    club_name = models.CharField(max_length=50, blank=False)
    competition_date = models.DateField(null=False)
    competition_note = models.DecimalField(max_digits=5, decimal_places=3)
    season_id = models.ForeignKey('Temporada', verbose_name="season", on_delete=models.CASCADE)

    def __str__(self):
        return self.competition_name

    class Meta:
        ordering = ('-competition_date',)



