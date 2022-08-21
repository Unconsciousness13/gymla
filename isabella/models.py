from django.db import models


class Competition(models.Model):
    competition_name = models.CharField(
        max_length=50, blank=False, unique=True)
    location = models.CharField(max_length=50, blank=False)
    club_name = models.CharField(max_length=50, blank=False, unique=True)
    competition_date = models.DateField(null=False)
    

    def __str__(self):
        return self.competition_name

    class Meta:
        ordering = ('-competition_date',)


class Note(models.Model):
    note = models.DecimalField(max_digits=5, decimal_places=3)
    competition = models.ForeignKey('Competition', on_delete=models.CASCADE)
    temporada = models.OneToOneField('Temporada', on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.note)


class Temporada(models.Model):
    season = models.CharField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return self.season