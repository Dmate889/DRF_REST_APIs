from django.contrib import admin
from .models import Game

# Register your models here.
class GameAdmin(admin.ModelAdmin):
    list_display = ["name", "release_date", "developer", "bio", "is_rented", "amount"]

admin.site.register(Game, GameAdmin)