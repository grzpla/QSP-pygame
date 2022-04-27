import os
import sys
import pygame

from Page import Page
from constant import *
from Button import Button
from utils import get_button_on_click


def main():
    pygame.init()

    map_name = {
        "FARM": ["HOME", "CAVE"],
        "DOWNTOWN": ["Emily_Hailee_HOME",
                     "Jody_Kent_Tom_HOME",
                     "Lewis_HOME",
                     "Leah_HOME",
                     "Pierre_HOME",
                     "Harvey_HOME",
                     "BAR",
                     "George_Evelynn_Alex_HOME",
                     "CEMETERY",
                     "SUPERMARKET",
                     "Museums_AND_Libraries",
                     "Anne_HOME",
                     "Community_Center",
                     "Robin_HOME"]
    }

    logo = pygame.image.load(os.path.join(images_resource, 'logo.jpeg'))
    pygame.display.set_icon(logo)
    pygame.display.set_caption("星露谷物语")
    screen = pygame.display.set_mode((1270, 666))

    start_page_bg_img = pygame.image.load(os.path.join(images_resource, "start.png"))
    start_page = Page(screen, start_page_bg_img)

    create_button = Button(text="创建", rect=(210, 510, 120, 60), click_function=get_button_on_click)
    load_button = Button(text="载入", rect=(450, 510, 120, 60), click_function=get_button_on_click)
    setting_button = Button(text="设置", rect=(700, 510, 120, 60), click_function=get_button_on_click)
    exit_button = Button(text="退出", rect=(950, 510, 120, 60), click_function=get_button_on_click)

    start_page.add_button([create_button, load_button, setting_button, exit_button])
    start_page.display()

    map_name_button = {}
    for name in map_name:
        v = map_name[name]
        if isinstance(v, type({})):
            for name1, v1 in v:
                tmp_button = Button(screen=screen, text=name1, rect=(0, 0, 200, 200), click_function=get_button_on_click)
                map_name_button[name1] = tmp_button
        elif isinstance(v, type([])):
            for i in v:
                tmp_button = Button(screen=screen, text=i, rect=(0, 0, 30, 30), click_function=get_button_on_click)
                map_name_button[i] = tmp_button
        else:
            tmp_button = Button(screen=screen, text=name, rect=(0, 0, 30, 30), click_function=get_button_on_click)
            map_name_button[name] = tmp_button

    running = True

    screen_width, screen_height = screen.get_size()

    pages = {"start_page": start_page}

    cur_page = pages["start_page"]
    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()

                cur_page.check_button_click(x, y)

        x, y = pygame.mouse.get_pos()
        cur_page.check_mouse_in(x, y)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
