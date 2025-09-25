from turtle import Turtle
score = 0
ALIGMENT = 'center'
FONT = 'arial'
FONT_SIZE = 20
FONT_TYPE = 'normal'

class Score_broad(Turtle):
    def __init__(self):
        super().__init__()
        self.highest_score = 0
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scorebroad()
    
    def update_scorebroad(self):
        self.clear()
        self.write(f"score : {self.score} highest score: {self.highest_score}", align=ALIGMENT, font=(FONT,FONT_SIZE,FONT_TYPE))

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.score = 0
        self.update_scorebroad()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER!", align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scorebroad()
        
