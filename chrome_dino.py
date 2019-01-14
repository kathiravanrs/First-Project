from PIL import ImageGrab
import pyautogui
import time


def jump():
    pyautogui.keyDown('space')
    time.sleep(0.1)
    pyautogui.keyUp('space')
    print("jump")


def duck():
    pyautogui.keyDown('down')
    time.sleep(0.15)
    pyautogui.keyUp('down')
    print("duck")


time.sleep(3)
light = (83, 83, 83)
dark = (172, 172, 172)
black = (0, 0, 0)
white = (255, 255, 255)
# a = pyautogui.position()
# print(ImageGrab.grab().getpixel(a))

while True:
    image = ImageGrab.grab()
    background = image.getpixel((300, 250))
    a = image.getpixel((755, 285))
    b = image.getpixel((750, 285))
    c = image.getpixel((760, 285))
    d = image.getpixel((745, 285))

    e = image.getpixel((735, 230))
    f = image.getpixel((745, 230))
    g = image.getpixel((750, 230))
    h = image.getpixel((755, 230))

    i = image.getpixel((735, 245))
    j = image.getpixel((745, 245))
    k = image.getpixel((750, 245))
    l = image.getpixel((755, 245))

    if background == black:
        if a == dark or b == dark or c == dark or d == dark:
            jump()
        if e == dark or f == dark or g == dark or h == dark or i == dark or j == dark or k == dark or l == dark:
            duck()
    elif background == white:

        if a == light or b == light or c == light or d == light:
            jump()
        if e == light or f == light or g == light or h == light or i == light or j == light or k == light or l == light:
            duck()
    else:
        time.sleep(.5)
        jump()
