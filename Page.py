import os
import pygame

from utils import *
from constant import *
from Button import Button

class Page(object):
    def __init__(self, screen, bg_img):
        self.screen = screen

        self.bg_img = bg_img

        self.buttons = []

    def display(self):
        self.screen.blit(self.bg_img, (0, 0))
        for button in self.buttons:
            button.display()

    def add_button(self, button):
        if isinstance(button, type([])):
            for item in button:
                item.set_screen(self.screen)
                self.buttons.append(item)
        elif isinstance(button, Button):
            button.set_screen(self.screen)
            self.buttons.append(button)
        else:
            raise NotImplementedError

    def check_button_click(self, x, y):
        for button in self.buttons:
            if button.is_mouse_in(x, y):
                button.click_function()
                return

    def check_mouse_in(self, x, y):
        for button in self.buttons:
            if button.is_mouse_in(x, y):
                button.mouse_in()
            else:
                button.mouse_out()