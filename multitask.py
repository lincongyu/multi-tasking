import numpy as np
import math
import random
from expyriment import design, control, stimuli

##experiment setting
N_TRAINING_TRIAL=4
N_BLOCK=3
N_TRIAL_PER_BLOCK=4
N_TRIALS=N_BLOCK*N_TRIAL_PER_BLOCK

MIN_WAIT_TIME = 1000
MAX_WAIT_TIME = 2000
MAX_RESPONSE_DELAY = 4000

exp = design.Experiment(name="multitask")
control.initialize(exp)

## screen and canvas setting
white=(255,255,255)
blankscreen = stimuli.BlankScreen(colour=white)
frame_size=(400,300)
black = (0,0,0)
font_size = 32
shape_text = "SHAPE"
filling_text = "FILLING"
screen_size = exp.screen.size

## make canvas
frame1 = stimuli.Rectangle(frame_size, colour=black, position=(0, 0 - frame_size[1]/2), line_width=2)
frame2 = stimuli.Rectangle(frame_size, colour=black, position=(0, 0 + frame_size[1]/2), line_width=2)
shape = stimuli.TextLine(shape_text, position=(0, 0 - (frame_size[1]) - 2*font_size), text_size=font_size)
filling = stimuli.TextLine(filling_text, position=(0, 0 + (frame_size[1]) + 2*font_size), text_size=font_size)


## make stimuli matrix
stimuliname = ['diamond_with_2_dots', 'diamond_with_3_dots', 'square_with_2_dots', 'square_with_3_dots']
stimuliindex = np.repeat([0,1,2,3],N_TRIAL_PER_BLOCK/4)
indexmeaning = {0: 'diamond2', 1: 'diamond3', 2:'square2' , 3: 'square3'}
random.shuffle(stimuliindex)
stimuliposition = [(0 , - frame_size[1]/2), (0 , frame_size[1]/2)]
positionindex = np.repeat([0,1],N_TRIAL_PER_BLOCK/2)
positionmeaning = {0:'shape',1:'filling'}
random.shuffle(positionindex)
keymeaning = {102:'f', 106:'j'}

instructions = stimuli.TextScreen("Instructions",
    f"""Welcome to the multi-task experiment.

    There will be a diamond or a square appearing on the screen, with two or three dots in it.

    If the stimuli appears on the upper half of the screen, please indicate the shape you see,

    press F for diamond and press J for square.

    Otherwise, if the stimuli appears on the bottom half of the screen, please indicate the number of dots you see,

    press F for 2 dots and press J for 3 dots.

    Your task is to press the SPACEBAR as quickly and correctly as possible when you see it.

    There will be {N_TRIALS} trials in total.

    Press the spacebar to start.""")


control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

###first block
for i in range(N_TRIAL_PER_BLOCK):
    try:
        frame1.plot(blankscreen)
        frame2.plot(blankscreen)
        shape.plot(blankscreen)
        filling.plot(blankscreen)
        blankscreen.present()

        waiting_time = random.randint(MIN_WAIT_TIME, MAX_WAIT_TIME)
        exp.clock.wait(waiting_time)

        image = stimuli.Picture(stimuliname[stimuliindex[i]] + '.png')
        image.anchor = (0.5, 0.5)  # set the anchor to the center of the image
        image.position = stimuliposition[positionindex[i]] 
        image.plot(blankscreen)
        blankscreen.present()

        
        key, rt = exp.keyboard.wait(duration=MAX_RESPONSE_DELAY)
        key = keymeaning[key]
        exp.data.add([i, waiting_time, key, rt, positionmeaning[positionindex[i]], indexmeaning[stimuliindex[i]]])
        blankscreen.clear_surface()
        blankscreen.present()
        exp.clock.wait(1000)

    except Exception as e:
        print(f"Error loading image: {e}")

control.end()
