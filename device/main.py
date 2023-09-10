#!/usr/bin/python3

from gpiozero import MCP3008
import time
import tkinter as tk
import cv2
import random
from PIL import Image, ImageTk


x = MCP3008(0)
y = MCP3008(1)
z = MCP3008(2)
soil = MCP3008(3)
rain = MCP3008(4)

p = 2
chart_width = 17
x_xlocation = 10
x_ylocation = 120
y_xlocation = 370
y_ylocation = 120
z_xlocation = 10
z_ylocation = 360

x_base = round(317 / p)
y_base = round(250 / p)
z_base = round(320 / p)
x_history = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y_history = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
z_history = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

rainTotal = 0
soil_val = 0

width, height = 720, 480

vid = cv2.VideoCapture(0)
# vid = cv2.VideoCapture('temp.mp4')


vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

window = tk.Tk()

show_video = True


def switch_option():
    global show_video
    if show_video:
        label_widget.pack_forget()
        canvas.pack()
        show_video = False
    else:
        label_widget.pack()
        canvas.pack_forget()
        show_video = True


def accel():
    global x_base, y_base, z_base, soil_val
    if not show_video:
        for i in range(20):
            x_history[i] = x_history[i + 1]
            y_history[i] = y_history[i + 1]
            z_history[i] = z_history[i + 1]
        try:
            x_history[20] = round((x.value * 1000) / p)
            y_history[20] = round((y.value * 1000) / p)
            z_history[20] = round((z.value * 1000) / p)
            soil_val = round(((1 - soil.value) * 100 - 10) * 100 / 30)
        except:
            a = 1
        if soil_val > 100:
            soil_val = 100
        elif soil_val < 0:
            soil_val = 0
    window.after(50, accel)


def screen():
    global x_base, y_base, z_base, soil_val
    if not show_video:
        canvas.delete("all")
        canvas.create_text(180, 20, text="左右(X)", font=("Arial", 20), fill="white")
        canvas.create_text(540, 20, text="前後(Y)", font=("Arial", 20), fill="white")
        canvas.create_text(180, 260, text="上下(Z)", font=("Arial", 20), fill="white")
        canvas.create_text(
            540,
            260,
            text="土壤含水量: " + str(soil_val) + "%",
            font=("Arial", 20),
            fill="white",
        )
        canvas.create_text(
            540,
            300,
            text="累計降雨量: " + str(round(rainTotal * 100) / 100) + "mm",
            font=("Arial", 20),
            fill="white",
        )
        for i in range(20):
            canvas.create_line(
                x_xlocation + chart_width * i,
                x_ylocation + x_history[i] - x_base,
                x_xlocation + chart_width * (i + 1),
                x_ylocation + x_history[i + 1] - x_base,
                fill="red",
                width=3,
            )
            canvas.create_line(
                y_xlocation + chart_width * i,
                y_ylocation + y_history[i] - y_base,
                y_xlocation + chart_width * (i + 1),
                y_ylocation + y_history[i + 1] - y_base,
                fill="yellow",
                width=3,
            )
            canvas.create_line(
                z_xlocation + chart_width * i,
                z_ylocation + z_history[i] - z_base,
                z_xlocation + chart_width * (i + 1),
                z_ylocation + z_history[i + 1] - z_base,
                fill="blue",
                width=3,
            )
    window.after(50, screen)


def refresh_rain():
    global rainTotal
    r = rain.value
    if r < 0.5:
        while r < 0.5:
            r = rain.value
        rainTotal = rainTotal + 0.2
    window.after(20, refresh_rain)


def upload():
    try:
        with open("info.txt", "w") as f:
            f.write(str(round(rainTotal * 100) / 100) + ",")
            f.write(str(soil_val) + ",")
            for i in range(20):
                f.write(str(x_history[i]))
                if i != 19:
                    f.write("x")
            f.write(",")
            for i in range(20):
                f.write(str(y_history[i]))
                if i != 19:
                    f.write("x")
            f.write(",")
            for i in range(20):
                f.write(str(z_history[i]))
                if i != 19:
                    f.write("x")
    except:
        a = 1
    window.after(200, upload)


def open_camera():
    global width, height
    if show_video:
        _, frame = vid.read()
        frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
        opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        captured_image = Image.fromarray(opencv_image)
        photo_image = ImageTk.PhotoImage(image=captured_image)
        label_widget.photo_image = photo_image
        label_widget.configure(image=photo_image)
    window.after(50, open_camera)


def end_program(event=None):
    exit()


switch_button = tk.Button(window, text="switch", command=switch_option)
switch_button.pack()

label_widget = tk.Label(window)
label_widget.pack()

canvas = tk.Canvas(window, width=width, height=height, bg="black")
canvas.pack_forget()


accel()
screen()
refresh_rain()
upload()
open_camera()


window.bind("<Escape>", end_program)
window.attributes("-fullscreen", True)
window.config(cursor="none")
window.mainloop()

"""
sudo bpi-bootsel /usr/lib/u-boot/bananapi/bpi-m3/BPI_M3_720P.img.gz
"""
