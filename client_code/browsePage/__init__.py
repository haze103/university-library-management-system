from ._anvil_designer import browsePageTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from ..studentHomePage import studentHomePage
from ..studentAccPage import studentAccPage


class browsePage(browsePageTemplate):
    def __init__(self, **properties):
      self.init_components(**properties)

      self.secDataPanel.items = anvil.server.call('get_book_list')

    def cmdSearchBtn_click(self, **event_args):
      search_item = self.txtSearchBox.text
      self.secDataPanel.items = anvil.server.call('search_books', search_item)

    def cmdHomeBtn_click(self, **event_args):
      self.secContentPanel.clear()
      self.secContentPanel.add_component(studentHomePage())

    def cmdAccountBtn_click(self, **event_args):
      self.secContentPanel.clear()
      self.secContentPanel.add_component(studentAccPage())

    def cmdLogoutBtn_click(self, **event_args):
      session_id = anvil.server.session['session_id']  # Retrieve the session ID from the client session
      
      try:
          anvil.server.call('logout', session_id)  # Call the logout function with the session ID
          anvil.server.session['session_id'] = None  # Clear the session ID from the client session
          self.secContentPanel.clear()  # Clear the content panel after logging out
          
          from ..welcomePage import welcomePage
          self.secContentPanel.add_component(welcomePage())  # Show the welcome page after logout
      except Exception as e:
          alert("An error occurred during logout: " + str(e))
    
    



    