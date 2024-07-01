from ._anvil_designer import browsePageTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class browsePage(browsePageTemplate):
    def __init__(self, **properties):
      # Set Form properties and Data Bindings.
      self.init_components(**properties)
      self.secDataPanel.items = anvil.server.call('get_book_list')

    def cmdSearchBtn_click(self, **event_args):
      strSearchItem = self.txtSearchBox.text
      self.secDataPanel.items = anvil.server.call('search_books', strSearchItem)

    def cmdHomeBtn_click(self, **event_args):
      from ..homePage import homePage
      self.secContentPanel.clear()
      self.secContentPanel.add_component(homePage())


  
    



    