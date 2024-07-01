from ._anvil_designer import confirmReservationTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import random
import string

class confirmReservation(confirmReservationTemplate):
    def __init__(self, **properties):
      # Set Form properties and Data Bindings.
      self.init_components(**properties)

    def validate_credentials(self, strEmail, strPassword):
      result = anvil.server.call('validate_user_credentials', strEmail, strPassword)
      return result

    def cmdConfirmBtn_click(self, **event_args):
      strEmail = self.txtEmail.text.strip()
      strPassword = self.txtPassword.text.strip()

      if self.validate_credentials(strEmail, strPassword):
        alert("Reservation Confirmed")
        return True
      else:
        alert("Invalid email or password. Please try again.")




