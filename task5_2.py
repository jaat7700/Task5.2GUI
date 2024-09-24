from tkinter import Tk, Label, Scale, HORIZONTAL
import tkinter.font as FONT
from gpiozero import PWMLED

# Set up PWM LEDs
red = PWMLED(17)
green = PWMLED(27)
blue = PWMLED(22)

# Create main window
window = Tk()
window.title("RGB LED Controller")

# Define font
font_style = FONT.Font(family='Helvetica', size=14, weight='bold')

# Function to update red LED value
def update_red(value):
    red.value = int(value) / 100

# Function to update green LED value
def update_green(value):
    green.value = int(value) / 100

# Function to update blue LED value
def update_blue(value):
    blue.value = int(value) / 100

# Red slider and label
Label(window, text="Red", font=font_style, fg="red").grid(row=0, column=0)
red_slider = Scale(window, from_=0, to=100, orient=HORIZONTAL, command=update_red)
red_slider.grid(row=0, column=1)

# Green slider and label
Label(window, text="Green", font=font_style, fg="green").grid(row=1, column=0)
green_slider = Scale(window, from_=0, to=100, orient=HORIZONTAL, command=update_green)
green_slider.grid(row=1, column=1)

# Blue slider and label
Label(window, text="Blue", font=font_style, fg="blue").grid(row=2, column=0)
blue_slider = Scale(window, from_=0, to=100, orient=HORIZONTAL, command=update_blue)
blue_slider.grid(row=2, column=1)

# Close function
def close():
    window.destroy()

window.protocol("WM_DELETE_WINDOW", close)

window.mainloop()
