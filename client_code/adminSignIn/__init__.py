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

  def validate_credentials(self, strEmail, strPassword):
    strResult = anvil.server.call("validate_admin_credentials", strEmail, strPassword)
    return strResult

  def cmdConfirmBtn_click(self, **event_args):
    strEmail = self.txtEmail.text.strip()
    strPassword = self.txtPassword.text.strip()

    if self.validate_credentials(strEmail, strPassword):
      alert(title = "Access Granted. ", content = "You now have access to admin page", buttons=[])
      self.navigate_to_adminPage()
    else:
      alert("Invalid email or password. Please try again.")

  def navigate_to_adminPage(self):
    self.clear()
    open_form('adminPage')
