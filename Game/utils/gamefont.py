import pygame
from utils.config import *

class GameFont:
    """
    A class that represents a font at multiple sizes, enabling easy
    management and rendering of text.

    Attributes:
        fontpath (str): The file path to the font.
        fonts (dict): Maps size labels to pygame.Font objects.
        sizes (dict): Maps size labels to their corresponding sizes in pixels.
        color (pygame.Color): The current font color.
        curr_font (pygame.Font): The currently selected font.
        curr_label (str): The label associated with the current font.

    Methods:
        add_size(label, size): Adds a custom font size with a label.
        get_size(): Returns the size of the current font in pixels.
        set_color(color): Updates the font's color.
        set_size(size_label): Changes the current font to the specified size.
        print(screen, message, x, y, antialiasing):
            Renders text on the screen at the specified position.
    """
    def __init__(self, fontpath, color=WHITE):
        """
        Initializes the GameFont class with the font path and default color.

        Args:
            fontpath (str): The path to the font file.
            color (pygame.Color, optional): The default color of the font. Defaults to WHITE.
        """
        self.fontpath = fontpath
    
        self.fonts = {
            "small": pygame.font.Font(fontpath, SM_FONT_SIZE),
            "medium": pygame.font.Font(fontpath, MED_FONT_SIZE),
            "large": pygame.font.Font(fontpath, LG_FONT_SIZE)
        }

        self.sizes = {
            "small": SM_FONT_SIZE,
            "medium": MED_FONT_SIZE,
            "large": LG_FONT_SIZE
        }

        self.color = color
        self.curr_font = self.fonts.get("medium")
        self.curr_label = "medium"

    def add_size(self, label, size):
        """ 
        Adds a new font size with a custom label.

        Args:
            label (str): A label for the new font size.
            size (int): The size of the new font in pixels.
        """
        self.fonts[label] = pygame.font.Font(self.fontpath, size)
        self.sizes[label] = size

    def get_size(self):
        """
        Returns the size of the currently selected font.

        Returns:
            int: The size in pixels of the current font.
        """
        return self.sizes[self.curr_label]

    def set_color(self, color):
        """ 
        Updates the color of the font.

        Args:
            color (pygame.Color): The new color for the font.
        """
        self.color = color

    def set_size(self, size_label):
        """ 
        Changes the size of the current font.

        Args:
            size_label (str or int): A key corresponding to a font size in self.fonts.

        Raises:
            ValueError: If size_label is not found in self.fonts.
        """
        if isinstance(size_label, str):
            if size_label not in self.fonts:
                raise ValueError(f"Size label must be one of {list(self.fonts)}. You passed set_size({size_label})")

            self.curr_font = self.fonts[size_label]
            self.curr_label = size_label
        else:
            self.add_size(f"{size_label}", size_label)
            self.set_size(f"{size_label}")

    def print(self, screen, message, x, y, antialiasing=False):
        """ 
        Draws a message to the screen at the specified position.

        Args:
            screen (pygame.Surface): The game screen where the text is drawn.
            message (str): The text to display.
            x (int): The x-coordinate of the text's center.
            y (int): The y-coordinate of the text's center.
            antialiasing (bool, optional): Whether to use antialiasing. Defaults to False.
        """
        render = self.curr_font.render(message, antialiasing, self.color)
        rect = render.get_rect()
        rect.center = (x, y)

        screen.blit(render, rect)
