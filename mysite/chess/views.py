from django.shortcuts import render, get_object_or_404
from .models import Game

# Create your views here.

def game_view(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    context = {
        'game_id': game.id,
        'initial_state': game.state,
    }

    return render(request, 'chess/index.html', context)
