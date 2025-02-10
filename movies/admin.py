from django.contrib import admin
from movies.models import Movies


@admin.register(Movies)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'release_date', 'get_actors', 'resume')
    search_fields = ('title', 'genre', 'release_date')

    def get_actors(self, obj):
        return ", ".join([actor.name for actor in obj.actors.all()])

    get_actors.short_description = 'actors'
