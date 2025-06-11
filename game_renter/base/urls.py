from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name = "home"),
    path("create_game", views.create_game, name="create_game"),
    path("get_games", views.get_games, name="get_games"),
    path("get_game/<int:pk>", views.get_game, name="get_game"),
    path("delete_game/<int:pk>", views.delete_game, name="delete_game"),
    path("update_game/<int:pk>", views.update_game, name="update_game")
]