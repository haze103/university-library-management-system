from ._anvil_designer import adminSignInTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import random
import string


class adminSignIn(adminSignInTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  # def cmdStudBtn_click(self, **event_args):
  def validate_credentials(self, email, password):
    result = anvil.server.call("validate_admin_credentials", email, password)
    return result

  def cmdConfirmBtn_click(self, **event_args):
    """This method is called when the button is clicked"""
    email = self.txtEmail.text.strip()
    password = self.txtPassword.text.strip()

    if self.validate_credentials(email, password):
      alert(title = "Access Granted. ", content = "You now have access to admin page")
      # Add any further logic here after successful validation
    else:
      alert("Invalid email or password. Please try again.")
