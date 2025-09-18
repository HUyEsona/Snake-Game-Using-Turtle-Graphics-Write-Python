from turtle import Turtle
score = 0
ALIGMENT = 'center'
FONT = 'arial'
FONT_SIZE = 10
FONT_TYPE = 'normal'

class Score_broad(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scorebroad()
    
    def update_scorebroad(self):
        self.write(f"score : {self.score}", align=ALIGMENT, font=(FONT,FONT_SIZE,FONT_TYPE))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scorebroad()
        
