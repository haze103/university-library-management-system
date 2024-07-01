from ._anvil_designer import homePageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class homePage(homePageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def cmdBooksBtn_click(self, **event_args):
    from ..browsePage import browsePage
    self.secContentPanel.clear()
    self.secContentPanel.add_component(browsePage())






  


