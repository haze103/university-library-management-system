from ._anvil_designer import adminPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class adminPage(adminPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.dataPanel1.items = anvil.server.call('get_reserved_books')
    self.dataPanel2.items = anvil.server.call('get_currently_borrowed_books')