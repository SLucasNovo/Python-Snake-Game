from turtle import Turtle

STARTING_POSITIONS = [(-20, 0), (-40, 0), (-60, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.orientation = 0
        self.head = self.segment[0]

    def create_snake(self):
        for block in STARTING_POSITIONS:
            self.add_segment(block)

    def add_segment(self, position):
        snake_block = Turtle(shape="square")
        snake_block.penup()
        snake_block.color("white")
        snake_block.setpos(position)
        self.segment.append(snake_block)

    def extend(self):
        # position = tuple([pos - 20 for pos in self.segment[0]])
        self.add_segment(self.segment[-1].position())

    def reset(self):
        for seg in self.segment:
            seg.goto(500, 500)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0 , - 1):
            new_position = self.segment[seg_num - 1].position()
            self.segment[seg_num].goto(new_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.orientation = self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.orientation = self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.orientation = self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.orientation = self.head.setheading(RIGHT)

