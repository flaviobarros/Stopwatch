# template for "Stopwatch: The Game"

# import modules
import simplegui
import random

# Global state
time = 0
score = 0
attempts = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    """Format state string."""
    global state
    minutos = time // 600
    segundos = (time - 600*minutos) // 10
    decimos = time % 10
    if segundos >= 10:
        return str(minutos) + ':' + str(segundos) + '.' + str(decimos)
    else:
        return str(minutos) + ':' + '0' + str(segundos) + '.' + str(decimos)
    
# Handler for buttons: "Start", "Stop", "Reset"
def start_button_handler():
    """Increment the size."""
    timer.start()
    
def stop_button_handler():
    """Decrement the size."""
    global score, attempts
    if timer.is_running(): # Once the game is stoped is not possible change the scores
        attempts = attempts + 1
        string = format(time)
        position = string.find('.')
        digit = string[position + 1]
        if digit == '0':
            score = score + 1
    timer.stop()
       
def reset_button_handler():
    """Reset the time."""
    global time, score, attempts
    time = 0
    score = 0
    attempts = 0
    timer.stop()

# Event handler for timer with 0.01 sec interval
def tick():
    global time
    time = time + 1
    
# Draw handler
def draw(canvas):
    """Print time when game is running."""
    global score, attempts
    canvas.draw_text(format(time), [120, 110], 35, "yellow")
    canvas.draw_text(str(score) + '/' + str(attempts), [200, 20], 20, "red")
    
# Create a frame 
frame = simplegui.create_frame("Home", 300, 200)

# Register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)
frame.add_button("Start", start_button_handler)
frame.add_button("Stop", stop_button_handler)
frame.add_button("Reset", reset_button_handler)

# Start the frame animation
frame.start()

