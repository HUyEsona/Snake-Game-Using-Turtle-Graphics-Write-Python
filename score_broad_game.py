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
        self.write(f"score : {self.score}", align="center", font=(FONT,FONT_SIZE,FONT_TYPE))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scorebroad()
        
