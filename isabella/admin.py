from django.contrib import admin
from .models import Competition, Note, Temporada

@admin.register(Competition)
class IsabellaAdminConfig(admin.ModelAdmin):
    search_fields = ('competition_name', 'location', 'competition_date' , 'club_name')
    list_filter = ('competition_name', 'competition_date' ,)
    ordering = ('competition_date',)
    list_display = ('competition_name', 'location', 'competition_date',)

@admin.register(Note)
class IsabellaAdminConfig(admin.ModelAdmin):
    search_fields = ('competition', 'note')
    list_filter = ('competition', 'note')
    ordering = ('competition', 'note')
    list_display = ('competition', 'note')


@admin.register(Temporada)
class IsabellaAdminConfig(admin.ModelAdmin):
    list_filter = ('season',)
    ordering = ('season',)
