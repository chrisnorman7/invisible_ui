"""Button class."""

import pygame

from invisible_ui.elements import Element


class Button(Element):
    """Perform an action when the enter key is pressed."""

    def __init__(self, title, action):
        """Action will be called when the enter key is pressed."""
        super().__init__(title)
        self.type = 'Button'
        self.help = 'Press enter or space to activate this button.'
        self.handled_keys[pygame.K_RETURN] = action
        self.handled_keys[pygame.K_SPACE] = action
