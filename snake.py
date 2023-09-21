from turtle import Turtle

SEGMENTS_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_segments()
        self.head = self.segments[0]

    # create each segment of the snake
    def create_segments(self):
        for position in SEGMENTS_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("green")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_segments()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def remove_segment(self):
        segment_to_remove = self.segments.pop()
        segment_to_remove.goto(1000, 1000)  # Move the segment to an arbitrary location off-screen
        segment_to_remove.hideturtle()  # Hide the segment
        del segment_to_remove

    # function to move each segment of the snake
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # last segment -> second to last
            # second segment -> first segment
            #  -> move forward by 1
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
