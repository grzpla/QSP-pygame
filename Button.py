import pygame


class Button(object):
    def __init__(self, screen=None, rect=(0, 0, 10, 10), text="BUTTON",
                 bg_color='white', color='black', mouse_on_bg_bg_color="white", mouse_on_color='red',
                 click_function=None):
        self.screen = screen
        self.rect = rect

        self.bg_color, self.color = bg_color, color
        self.mouse_on_bg_color, self.mouse_on_color = mouse_on_bg_bg_color, mouse_on_color

        self.click_function = click_function(self)

        self.text = text

        self.font_name = pygame.font.match_font("kaiti")
        self.surface = pygame.font.Font(self.font_name, 40)
        self.surface = self.surface.render(self.text, True, self.color, self.bg_color)

        text_width, text_height = self.surface.get_size()

        self.x, self.y, self.width, self.height = rect
        self.text_x, self.text_y = self.x + (self.width - text_width) // 2, self.y + (self.height - text_height) // 2

    def display(self):
        pygame.draw.rect(self.screen, self.mouse_on_bg_color, self.rect, 0)
        self.screen.blit(self.surface, (self.text_x, self.text_y))

    def is_mouse_in(self, x, y):
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False

    def mouse_in(self):
        self.surface = pygame.font.Font(self.font_name, 40)
        self.surface = self.surface.render(self.text, True, self.mouse_on_color, self.mouse_on_bg_color)
        self.display()

    def mouse_out(self):
        self.surface = pygame.font.Font(self.font_name, 40)
        self.surface = self.surface.render(self.text, True, self.color, self.bg_color)
        self.display()

    def set_screen(self, screen):
        from Page import Page
        if isinstance(screen, Page):
            self.screen = screen.screen
        else:
            self.screen = screen
