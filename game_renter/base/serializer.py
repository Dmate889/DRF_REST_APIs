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


