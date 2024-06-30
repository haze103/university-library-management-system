from ._anvil_designer import welcomePageTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from ..studentSignInPage import studentSignInPage


class welcomePage(welcomePageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def cmdStudBtn_click(self, **event_args):
    self.secContentPanel.clear()
    self.secContentPanel.add_component(studentSignInPage())

  def cmdFcltyBtn_click(self, **event_args):
    self.secContentPanel.add_component(studentSignInPage())
    

  
