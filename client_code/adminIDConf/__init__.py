from ._anvil_designer import adminIDConfTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import random
import string
from ..adminSignIn import adminSignIn


class adminIDConf(adminIDConfTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  # def cmdStudBtn_click(self, **event_args):
  def validate_credentials(self, admin_id):
    result = anvil.server.call("validate_admin_ID", admin_id)
    return result

  def cmdConfirmBtn_click(self, **event_args):
    admin_id = self.txtAdminID.text.strip()

    if self.validate_credentials(admin_id):
      alert(title="Sign in to have full access.",
           content = adminSignIn(), large=True, buttons=[])
      
    else:
      alert(title = "Access Denied!",
         content = "You have no permission to access this page.")
