if __name__ == '__main__':
 import pygame, logging, sys
 from invisible_ui.session import Session
 from invisible_ui.xtras.help_menu import HelpMenu
 from invisible_ui.xtras.int_textbox import IntTextbox
 from invisible_ui.elements import *
 
 logging.basicConfig(stream = sys.stdout, level = 'DEBUG')
 
 class ExampleMenu(Menu):
  def __init__(self, session):
   super(ExampleMenu, self).__init__(session, 'Example Menu')
   self.session = session
   self.add_item(Textbox('Username'))
   self.add_item(Textbox('Password', hidden = True))
   self.add_item(IntTextbox('Age'))
   self.add_item(Group('Level', ['User', 'Special Person', 'Administrator', 'God']))
   self.add_item(Button('OK', lambda s = self.session: session.do_quit()))
 
 class ExampleSession(Session):
  def __init__(self):
   super(ExampleSession, self).__init__()
   self.add_keydown(self.do_quit, key = pygame.K_q)
   self.add_keydown(HelpMenu, key = pygame.K_F1)
   self.control = ExampleMenu(self)
 
 pygame.init()
 screen = pygame.display.set_mode()
 session = ExampleSession()
 session.main_loop()