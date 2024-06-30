from ._anvil_designer import adminSignInPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..popupForgotPass import popupForgotPass
from ..studentSignUpPage import studentSignUpPage


class adminSignInPage(adminSignInPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def cmdForgotPassBtn_click(self, **event_args):
    alert(
      content=popupForgotPass(),
      title="Login Using Code",
      large=True,
      buttons=[],
    )

  def linkSignUp_click(self, **event_args):
    self.secContentPanel.clear()
    self.secContentPanel.add_component(studentSignUpPage())
