from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")
MOVE_SCORE = False


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-20, 260)
        self.score = 0
        self.high_score = int(self.read_score())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", MOVE_SCORE, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_score()
        self.score = 0
        self.update_scoreboard()

    def read_score(self):
        with open('data.txt', mode = "r") as score_text:
            return score_text.read()

    def write_score(self):
        with open('data.txt', mode = "w") as score_text:
            score_text.write(str(self.high_score))


