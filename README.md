# chess
The game has been developed in Django Backend







Overview:
Advanced Chess-like Game is a web-based turn-based strategy game inspired by chess. The game is developed using Django for the backend and Tailwind CSS for the frontend. It features a grid-based board with unique character types, each with distinct movement and capture abilities.

Features:

Character Types:

Pawn: Moves one block in any direction (Left, Right, Forward, Backward).
Hero1: Moves two blocks straight in any direction and captures opponents in its path.
Hero2: Moves two blocks diagonally and captures opponents in its path.

Gameplay:
Players take turns to move their characters on the board.
Characters can capture opponents if they land on a square occupied by an opposing piece.
The game ends when one player eliminates all of the opponent’s pieces.


Installation:
Prerequisites:
Python 3.8 or higher,
Django,
Tailwind CSS (via CDN),
Git,

Clone the Repository.

git clone https://github.com/mudasirmattoo/chess.git  .


cd chess.


or download all the files of the repository and store in a folder .


open that folder in terminal and 


Set Up the Virtual Environment.


python -m venv env.

cd env

source venv/bin/activate  # On Windows: venv\Scripts\activate.


cd ..


cd mysite .


pip install django.


Install Dependencies.

npm init -y .

npm install tailwind

pip install -r requirements.txt .


Apply Migrations.


python manage.py makemigrations .


python manage.py migrate .

Run the Development Server.

create a super user using createsuperuser using the command "python manage.py createsuperuser"

add a game in the admin panel by going to url : http://127.0.0.1:8000/admin



in the game state enter initial state as :

[["P1", null, null, null, "P2"], [null, "H1", null, "H2", null], [null, null, null, null, null], [null, "H2", null, "H1", null], ["P2", null, null, null, "P1"]]

python manage.py runserver  .

The application will be available at http://127.0.0.1:8000/game/< int:id >,  where int:id will be 1 for you or the game id you have created.


