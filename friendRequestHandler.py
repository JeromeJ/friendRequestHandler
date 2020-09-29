#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'JeromeJ'

import cv2
import numpy
import pyscreenshot
import time

from pynput.mouse import Button, Controller

mouse = Controller()

print("Finding next target")

s = cv2.cvtColor(numpy.array(pyscreenshot.grab()), cv2.COLOR_RGB2BGR)
cv2.imwrite("screenshot.png", s)

c = cv2.imread('rsrc/confirm.png')
matches = cv2.matchTemplate(s, c, cv2.TM_CCOEFF_NORMED)
loc = numpy.where(matches >= .7)
loc = list(zip(*loc[::-1]))

print("Right clicking")

mouse.position = loc[0]
mouse.move(0, -20)

mouse.click(Button.right, 1)
time.sleep(.5)

#s = cv2.cvtColor(numpy.array(pyscreenshot.grab()), cv2.COLOR_RGB2BGR)
#cv2.imwrite("screenshot.png", s)

#c = cv2.imread('rsrc/inspectElement.png')
#matches = cv2.matchTemplate(s, c, cv2.TM_CCOEFF_NORMED)
#loc = numpy.where(matches >= .9)
#loc = list(zip(*loc[::-1]))

#mouse.position = loc[0]
#mouse.click(Button.left, 1)

from pynput.keyboard import Key, Controller

keyboard = Controller()


print("Opening inspector")
keyboard.press("Q")
keyboard.release("Q")
time.sleep(2)

print("Switching to console")

with keyboard.pressed(Key.ctrl):
	with keyboard.pressed(Key.shift):
		keyboard.press("k")
		keyboard.release("k")

time.sleep(2.5)

print("Switching to JS")

keyboard.type("$0.in")
# Seems to have an issue with the double n otherwise
keyboard.type("nerText.match('([0-9]+) mutual friend')")
keyboard.press(Key.enter)
keyboard.release(Key.enter)