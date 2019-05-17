from tkinter import *
import pygame
 
root = Tk()
root.title("Tuturu")
root.geometry("220x100")

def play():
    pygame.init()
    pygame.mixer.music.load('Tuturu.mp3')
    pygame.mixer.music.play()
    clock = pygame.time.Clock()
    song.play()
    while True:
        clock.tick(60)
    pygame.quit()

btn = Button(text="Tuturu",          # текст кнопки 
             background="#2B1287",     # фоновый цвет кнопки
             foreground="#ccc",     # цвет текста
             padx="75",             # отступ от границ до содержимого по горизонтали
             pady="50",              
             font="7", 
             command = play
             )
       
btn.pack()
 
root.mainloop()
