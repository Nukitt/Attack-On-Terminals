import sys 
sys.path.insert(1, './src')
from src.replay import game 

replay = input("What is the replay file name? ")
Game=game(replay)
Game.play()