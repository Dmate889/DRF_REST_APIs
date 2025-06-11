from django.contrib import admin
from .models import Game

# Register your models here.
class GameAdmin(admin.ModelAdmin):
    list_display = ["name", "release_year", "developer", "bio", "is_rented", "price"]

admin.site.register(Game, GameAdmin)