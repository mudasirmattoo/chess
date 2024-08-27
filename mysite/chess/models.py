from django.db import models

# Create your models here.

initial_state = {
    'board': [
        ['A-P1', 'A-P2', 'A-P3', 'A-H1', 'A-H2'],
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['B-H2', 'B-H1', 'B-P3', 'B-P2', 'B-P1'],
    ],
    'current_turn': 'A',
}

class Game(models.Model):
    player1 = models.CharField(max_length=100)
    player2 = models.CharField(max_length=100)
    state = models.JSONField(default=dict)  

class Move(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.CharField(max_length=100)
    move = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
