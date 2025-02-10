from django.contrib import admin
from actors.models import ActorModel


@admin.register(ActorModel)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthday', 'nationality')
    search_fields = ('name', 'nationality')
