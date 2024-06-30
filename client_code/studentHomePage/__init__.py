from ._anvil_designer import studentHomePageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..browsePage import browsePage
from ..studentActivityPage import studentActivityPage
from ..studentAccPage import studentAccPage


class studentHomePage(studentHomePageTemplate):
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
        session_id = anvil.server.session['session_id']  # Retrieve the session ID from the client session
        
        try:
            anvil.server.call('logout', session_id)  # Call the logout function with the session ID
            anvil.server.session['session_id'] = None  # Clear the session ID from the client session
            self.secContentPanel.clear()  # Clear the content panel after logging out
            
            from ..welcomePage import welcomePage
            self.secContentPanel.add_component(welcomePage())  # Show the welcome page after logout
        except Exception as e:
            alert("An error occurred during logout: " + str(e))  # Display an error message if logout fails