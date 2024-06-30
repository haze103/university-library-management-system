from ._anvil_designer import homePageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..browsePage import browsePage
from ..studentActivityPage import studentActivityPage
from ..studentAccPage import studentAccPage

class homePage(homePageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def cmdBooksBtn_click(self, **event_args):
    self.secContentPanel.clear()
    self.secContentPanel.add_component(browsePage())

  def cmdFcltyBtn_click(self, **event_args):
    self.secContentPanel.clear()
    self.secContentPanel.add_component(studentActivityPage())

  def cmdAccountBtn_click(self, **event_args):
    self.secContentPanel.clear()
    self.secContentPanel.add_component(studentAccPage())

  def cmdLogoutBtn_click(self, **event_args):
    self.secContentPanel.clear()
    from ..welcomePage import welcomePage
    self.secContentPanel.add_component(welcomePage())




  


