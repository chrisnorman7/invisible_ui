"""Button class."""

import pygame

from invisible_ui.elements.element import Element


class Button(Element):
    """Perform an action when the enter key is pressed."""

    def __init__(self, parent, title, action):
        """Action will be called when the enter key is pressed."""
        super().__init__(parent, title)
        self.help = "Press enter or space to activate this button."
        self.type = "button"

        self.activateActionHandler = self.add_keydown(action, key=(lambda v: v ==pygame.K_RETURN or v == pygame.K_SPACE))
