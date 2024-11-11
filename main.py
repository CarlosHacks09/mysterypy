import tkinter as tk
from threading import Thread
import time
import pygame
import random

audio_files = ['voice_gaster_1.wav', 'voice_gaster_2.wav', 'voice_gaster_3.wav', 'voice_gaster_4.wav', 'voice_gaster_5.wav', 'voice_gaster_6.wav', 'voice_gaster_7.wav']

pygame.mixer.init()

def play_sound():
    pygame.mixer.music.load(random.choice(audio_files))
    pygame.mixer.music.play()

def type_effect(label, text, speed):
    def run():
        def update_label(c):
            label_var.set(label_var.get() + c)
        
        for i, char in enumerate(text):
            if char.isalpha():
                play_sound()
            # Correctly capture the current character by passing it to a function
            root.after(int(speed * 1000) * (i+1), update_label, char)
            time.sleep(speed)

    Thread(target=run).start()

root = tk.Tk()
root.configure(bg='black')
root.title("Typing Effect")
root.attributes('-fullscreen', True)  # Make the window fullscreen

label_var = tk.StringVar()

typing_label = tk.Label(root, textvariable=label_var, fg="white", bg="black", font=("Wingdings", 80))
typing_label.pack()

# Start the typing effect with your desired text and speed
type_effect(typing_label, "ENTRY NUMBER SEVENTEEN.\nDARK DARKER YET DARKER.\nTHE DARKNESS KEEPS GROWING.\nTHE SHADOWS CUTTING DEEPER.\nPHOTON READINGS NEGATIVE.\nTHIS NEXT EXPERIMENT.\nSEEMS.\nVERY.\nVERY.\nINTERESTING.\nWHAT DO YOU TWO THINK", 0.1)  # Adjust text and speed here

# Schedule the window to close after 25 seconds
root.after(25000, root.destroy)

root.mainloop()