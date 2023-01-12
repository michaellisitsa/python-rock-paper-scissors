from Game.Rock import Rock
from Game.Scissors import Scissors
from Game.Game import Game

# Create a class for creating objects 
# type: rock, 
# paper and scissors
game = Game()
game.create_object("rock")
game.create_object("rock", 1,1)
game.create_object("scissors", 2,1)
game.create_object("paper", 2,2)

game.list[0].move_in_direction(1)
game.list[1].move_in_direction(2)
print('pos x:',game.list[1].x," y: ",game.list[1].y)
# Add an attraction and repulsion attribute
# as a class attribute

# Store all the instances of the 
# rock paper scissors, in a game class

# Game class contains a list of these.

# Have a Game method to add to the Game.objects list

# Have a Game method to iterate over the list,
# and Calculate the nearest attracted
# and repulsed objects

# The info about what is the nearest object
# would only get calculated when called.
# not when any of the positions change 
