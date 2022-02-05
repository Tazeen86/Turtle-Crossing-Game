from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.level = 0
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)


    def you_win(self):
        self.clear()
        self.goto(0,0)
        self.write("YOU WIN",align="center",font=FONT)

    def display_score(self):
        self.clear()
        self.penup()
        self.goto(0,240)
        self.hideturtle()
        self.write(f"Level : {self.level}",align="center",font=FONT)
    
    def level_up(self):
        self.level += 1