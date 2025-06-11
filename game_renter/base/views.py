from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Game

from .serializer import GameRenterSerializer

# Create your views here.
def home(request):
    return render(request, "base/home.html")

@permission_classes([IsAuthenticated])
@api_view(["POST"])
def create_game(request):
    serializer = GameRenterSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save(created_by = request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_games(request):
    games = Game.objects.all()
    search_query = request.query_params.get("search")
    if search_query:
        games = games.filter(name__icontains=search_query)

    serializer = GameRenterSerializer(games, many = True)
    return Response(serializer.data)

@api_view(["GET"])
def get_game(request, pk):
    game = Game.objects.get(id = pk)
    serializer = GameRenterSerializer(game)

    return Response(serializer.data)

@permission_classes([IsAuthenticated])
@api_view(["PUT"])
def update_game(request, pk):
    game = Game.objects.get(id = pk)
    serializer = GameRenterSerializer(game, data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated])
@api_view(["POST"])
def delete_game(request, pk):
    game = Game.objects.get(id = pk)
    game.delete()
    return Response({"message": "Game deleted"}, status = status.HTTP_200_OK)

@permission_classes([IsAuthenticated])
@api_view(["POST"])
def delete_all(request):
    game = Game.objects.all()
    game.delete()
    return Response({"all games have been deleted"}, status = status.HTTP_200_OK)

