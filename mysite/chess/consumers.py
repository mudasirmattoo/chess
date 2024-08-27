import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Game, Move

class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "game_room"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave the room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        move = data['move']
        player = data['player']

        try:
            game = Game.objects.get(id=data['game_id'])
        except Game.DoesNotExist:
            await self.send(text_data=json.dumps({
                'error': 'Game not found.'
            }))
            return

        new_state = self.process_move(game.state, move, player)

        game.state = new_state
        game.save()

        Move.objects.create(game=game, player=player, move=move)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'game_move',
                'move': move,
                'player': player,
                'game_state': new_state,
            }
        )

    async def game_move(self, event):
        move = event['move']
        player = event['player']
        game_state = event['game_state']

        await self.send(text_data=json.dumps({
            'move': move,
            'player': player,
            'game_state': game_state,
        }))

    def process_move(self, current_state, move, player):
    
        if move == 'P1:L':
            pass

        return current_state
