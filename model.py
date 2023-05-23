#!/python3

import enum
import random

class Choice(enum.Enum):
    rock = "✊"
    paper = "✋"
    scissors = "✌️"

class Player(enum.Enum):
    com = "🤖"
    you = "😃"
    tie = "👔"

class Game():
    com_score = 0
    your_score = 0
    
    com_selection = Choice.rock
    your_selection = Choice.rock

    winner:Player = None
    
    def reset(self):
        self.com_score = 0
        self.your_score = 0
        self.com_selection = Choice.rock
        self.your_selection = Choice.rock
        self.winner = None
    
    def update_com_selection(self):
        self.com_selection = random.choice(list(Choice))
    
    def update_score(self, winner: Player):
        print(f"Winner!: {winner} {winner.name} {winner.value}")
        if Player.com == winner:
            self.com_score += 1
        if Player.you == winner:
            self.your_score += 1
        self.winner = winner

    
# this is to use the over complicated method to
# check if your choice won the match. see 
# diagram im folder
    choice_values = {
        Choice.paper : 1,
        Choice.rock : 2,
        Choice.scissors: 4
    }
    winner_values = {
        0 : "draw",
        1: Choice.paper,
        2: Choice.rock,
        3: Choice.scissors
    }

    def compare(self,x,y):
        return (abs(abs(x) + (-1 * abs(y))))

    def who_wins(self, com:Choice,you:Choice) -> Player:
        pass
        # convert choices to choice values 
        com_val = self.choice_values[com]
        your_val = self.choice_values[you]
        # compare the choice values and get the result
        winner_val = self.compare(com_val,your_val)
        # translate result to winner values 

        # if draw return draw 
        if winner_val == 0:
            return Player.tie
        # otherwise compare against player value to see if its the winner or not
        winner_choice = self.winner_values[winner_val]
        if you == winner_choice:
            return Player.you
        if com == winner_choice:
            return Player.com
        
#########################
    
    def play(self, choice:Choice):
        self.your_selection = choice
        self.update_com_selection()
        winner :Player = self.who_wins(self.com_selection,self.your_selection)
        self.update_score(winner)