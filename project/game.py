import tkinter as tk
from tkinter import PhotoImage
from time import sleep
import random
import pygame


class CarRacingTkinter:
    def __init__(self, master):
        self.master = master
        self.master.title("tab3 alasfelt -- hassan & hegag")
        self.master.geometry("800x600")

        self.canvas = tk.Canvas(self.master, width=800, height=600, bg="black")
        self.canvas.pack()

        self.initialize()

    def initialize(self):
        self.crashed = False

        self.car_image = PhotoImage(file='.\img\minicooper.png')
        self.car_x_coordinate = 405
        self.car_y_coordinate = 480
        self.car_width = 50
        
        # enemy_car
        self.enemy_car_image = PhotoImage(file='.\img\enemy.png')
        self.enemy_car_startx = random.randrange(310, 450)
        self.enemy_car_starty = -600
        self.enemy_car_speed = 5
        self.enemy_car_width = 50
        self.enemy_car_height = 50

        # Background
        self.bg_image = PhotoImage(file=".\\img\\33.png")
        self.bg_x1, self.bg_y1 = 250, 250
        self.bg_x2, self.bg_y2 = 250, -350
        self.bg_speed = 3
        self.count = 0

        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)
        self.master.bind("<Up>", self.move_up)
        self.master.bind("<Down>", self.move_down)

        self.run_car()

    def car(self):
        self.canvas.create_image(self.car_x_coordinate, self.car_y_coordinate, anchor=tk.NW, image=self.car_image)

    def back_ground_road(self):
        self.canvas.create_image(self.bg_x1, self.bg_y1, anchor=tk.NW, image=self.bg_image)
        self.canvas.create_image(self.bg_x2, self.bg_y2, anchor=tk.NW, image=self.bg_image)

        self.bg_y1 += self.bg_speed
        self.bg_y2 += self.bg_speed

        if self.bg_y1 >= 600:
            self.bg_y1 = -600

        if self.bg_y2 >= 600:
            self.bg_y2 = -600

    def run_enemy_car(self, thingx, thingy):
        self.canvas.create_image(thingx, thingy, anchor=tk.NW, image=self.enemy_car_image)

    def highscore(self):
        self.canvas.create_text(50, 20, anchor=tk.NW, text="Score : " + str(self.count), fill="white")

    def display_message(self, msg):
        self.canvas.create_text(400, 240, anchor=tk.CENTER, text=msg, fill="white", font=("comicsansms", 36, "bold"))
        self.master.update()
        sleep(1)
        self.initialize()

    def move_left(self, event):
        self.car_x_coordinate -= 25

    def move_right(self, event):
        self.car_x_coordinate += 25
    
    def move_up(self, event):
        self.car_y_coordinate -= 5
    
    def move_down(self, event):
        self.car_y_coordinate += 5

    def run_car(self):
        while not self.crashed:
            self.master.update()
            sleep(0.02)

            self.canvas.delete("all")
            self.back_ground_road()

            self.run_enemy_car(self.enemy_car_startx, self.enemy_car_starty)
            self.enemy_car_starty += self.enemy_car_speed

            if self.enemy_car_starty > 600:
                self.enemy_car_starty = 0 - self.enemy_car_height
                self.enemy_car_startx = random.randrange(310, 450)

            self.car()
            self.highscore()
            self.count += 1
            if self.count % 100 == 0:
                self.enemy_car_speed += 1
                self.bg_speed += 1

            if (self.car_y_coordinate < self.enemy_car_starty + self.enemy_car_height
                ):
                if (
                    self.car_x_coordinate > self.enemy_car_startx
                    and self.car_x_coordinate < self.enemy_car_startx + self.enemy_car_width
                    or self.car_x_coordinate + self.car_width > self.enemy_car_startx
                    and self.car_x_coordinate + self.car_width < self.enemy_car_startx + self.enemy_car_width
                ):
                    pygame.mixer.init()
                    sound = pygame.mixer.Sound(".\\img\\exp_snd.wav")
                    sound.play()
                    self.explosion_image = PhotoImage(file=".\\img\\clown.gif")
                    self.canvas.create_image(
                    self.car_x_coordinate-100, self.car_y_coordinate-100, anchor=tk.NW, image=self.explosion_image)
                    self.master.update()
                    self.crashed = True
                    self.display_message("Game Over !!!")
                    sleep(1)
                    self.initialize()

            if self.car_x_coordinate < 310 or self.car_x_coordinate > 480:
                self.crashed = True
                self.display_message("Game Over !!!")


if __name__ == "__main__":
    root = tk.Tk()
    car_racing_tkinter = CarRacingTkinter(root)
    root.mainloop()
