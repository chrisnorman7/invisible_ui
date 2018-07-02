"""Element classes."""

from accessible_output2.outputs.auto import Auto


def cancel(parentElement, message='Canceled.'):
    """Perform a cancel."""
    ao2 = Auto()
    parentElement.control = None

    if message:
        ao2.output(message)


from invisible_ui.elements.button import Button
from invisible_ui.elements.checkbox import Checkbox
from invisible_ui.elements.dialog import Dialog
from invisible_ui.elements.group import Group
from invisible_ui.elements.label import Label
from invisible_ui.elements.menu import Menu
from invisible_ui.elements.textbox import Textbox
