from ._anvil_designer import basePageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..welcomePage import welcomePage


class basePage(basePageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.secContentPanel.add_component(welcomePage())
