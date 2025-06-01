from rest_framework import serializers
from .models import Game


class GameRenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = [
            "id",
            "name",
            "developer",
            "bio",
            "release_year",
            "is_rented",
            "amount"
        ]

