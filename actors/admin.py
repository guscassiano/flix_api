from django.contrib import admin
from actors.models import ActorModel, Nationality


@admin.register(Nationality)
class NationalityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(ActorModel)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthday', 'nationality')
    search_fields = ('name', 'nationality')
