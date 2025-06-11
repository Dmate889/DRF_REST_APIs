from django.utils import timezone
from rest_framework import serializers
from .models import Game


class GameRenterSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()


    class Meta:
        model = Game
        fields =  '__all__'
        read_only_fields = ['created_by']

    def get_created_by(self, obj):
        return obj.created_by.username if obj.created_by else None

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value

    def validate_release_year(self, value):
        if value.date() > timezone.now().date():
            raise serializers.ValidationError("The release year can not be in the future.")
        return value


