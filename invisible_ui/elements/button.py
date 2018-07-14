"""Button class."""

import logging

import pygame

from invisible_ui.elements.element import Element


class Button(Element):
    """Perform an action when the enter key is pressed."""

    def __init__(self, parent, title, actions):
        """Action will be called when the enter key is pressed."""
        super().__init__(parent, title, "Button", logger=logging.getLogger("Button"),
                        help="Press enter or space to activate this button.")

        self.activateActionHandler = self.add_keydown(actions, key=(lambda v: v ==pygame.K_RETURN or v == pygame.K_SPACE))
