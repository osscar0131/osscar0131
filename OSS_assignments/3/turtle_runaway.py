# This example is not working in Spyder directly (F5 or Run)
# Please type '!python turtle_runaway.py' on IPython console in your Spyder.

#TODO
#Add a timer : 5 points - done
#Add a (intelligent) Turtle : 8 points - kinda?
#Add a concept of score : 7 points

#OPTIONAL
#Change window title to "Turtle Runaway" - done
#Add background or game arena
#Add a concept of stages
#Add opening, closing, and ending
#Fix a bug (e.g. switching colors)



import tkinter as tk
import turtle, random

import time

class RunawayGame:
    def __init__(self, canvas, runner, chaser, timer, catch_radius=50):
        self.canvas = canvas
        self.runner = runner
        self.chaser = chaser
        self.timer = timer
        self.catch_radius2 = catch_radius**2

        # Initialize 'runner' and 'chaser'
        self.runner.shape('turtle')
        self.runner.color('blue')
        self.runner.penup()

        self.chaser.shape('turtle')
        self.chaser.color('red')
        self.chaser.penup()

        # Instantiate an another turtle for drawing
        self.drawer = turtle.RawTurtle(canvas)
        self.drawer.hideturtle()
        self.drawer.penup()

        self.timer.hideturtle()
        self.timer.penup()
        self.timer.setpos(0, 300)
        self.timer.color("black")

        self.isCatching = False


    def is_catched(self):
        p = self.runner.pos()
        q = self.chaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        return dx**2 + dy**2 < self.catch_radius2

    def start(self, init_dist=400, ai_timer_msec=100):
        self.runner.setpos((-init_dist / 2, 0))
        self.runner.setheading(0)
        self.chaser.setpos((+init_dist / 2, 0))
        self.chaser.setheading(180)

        # TODO) You can do something here and follows.
        self.start = time.time()
        self.ai_timer_msec = ai_timer_msec
        self.canvas.ontimer(self.step, self.ai_timer_msec)



    def step(self):
        self.runner.run_ai(self.chaser.pos(), self.chaser.heading())
        self.chaser.run_ai(self.runner.pos(), self.runner.heading())

        # TODO) You can do something here and follows.
        is_catched = self.is_catched()
        self.drawer.undo()
        self.drawer.penup()
        self.drawer.setpos(-300, 300)
        self.drawer.write(f'Is catched? {is_catched}')

        self.timer.clear()
        self.timer.write(round(time.time() - self.start, 1))
        

        # Note) The following line should be the last of this function to keep the game playing
        self.canvas.ontimer(self.step, self.ai_timer_msec)

class ManualMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

        # Register event handlers
        canvas.onkeypress(lambda: self.forward(self.step_move), 'Up')
        canvas.onkeypress(lambda: self.backward(self.step_move), 'Down')
        canvas.onkeypress(lambda: self.left(self.step_turn), 'Left')
        canvas.onkeypress(lambda: self.right(self.step_turn), 'Right')
        canvas.listen()

    def run_ai(self, opp_pos, opp_heading):
        pass

class RandomMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

    def run_ai(self, opp_pos, opp_heading):
        mode = random.randint(0, 2)
        modeDuration = random.randint(30, 50) / 10 # random 3~5 seconds, 0.1 seconds precision
        modeStart = time.process_time() # Timer for mode duration check

        if (time.process_time() - modeStart > modeDuration):       # Has time passed enough?
            mode = random.randint(0, 2)                 # Select new mode
            modeDuration = random.randint(10, 50) / 10  # New mode's duration
            modeStart = time.process_time()                     # Reset timer to current time
        #else:
            #time.sleep(0.05)                            # Wait for another 0.05 seconds before checking

        

        if mode == 0:
            self.forward(self.step_move)
        elif mode == 1:
            self.left(self.step_turn)
        elif mode == 2:
            self.right(self.step_turn)

class GameTimer(turtle.RawTurtle):
    def __init__(self, canvas):
        super().__init__(canvas)

        self.hideturtle()
        self.penup()

    

if __name__ == '__main__':
    # Use 'TurtleScreen' instead of 'Screen' to prevent an exception from the singleton 'Screen'
    root = tk.Tk(className=" Turtle Runaway ")
    canvas = tk.Canvas(root, width=700, height=700)
    canvas.pack()
    screen = turtle.TurtleScreen(canvas)

    # TODO) Change the follows to your turtle if necessary
    runner = RandomMover(screen)
    chaser = ManualMover(screen)
    timer = GameTimer(screen)
    
    
    
    game = RunawayGame(screen, runner, chaser, timer)
    game.start()
    screen.mainloop()
