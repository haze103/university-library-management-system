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

   # def cmdStudBtn_click(self, **event_args):
    def validate_credentials(self, email, password):
      result = anvil.server.call('validate_user_credentials', email, password)
      return result

    def cmdConfirmBtn_click(self, **event_args):
        """This method is called when the button is clicked"""
        email = self.txtEmail.text.strip()
        password = self.txtPassword.text.strip()

        if self.validate_credentials(email, password):
            alert("Reservation Confirmed")
            # Add any further logic here after successful validation
        else:
            alert("Invalid email or password. Please try again.")




