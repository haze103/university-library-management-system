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

    def cmdStudBtn_click(self, **event_args):
      email = self.txtEmail.text
      anvil.server.call('check_email', email)
      ver_code = self.generate_ver_code()
      
      try:
          anvil.server.call('send_email_code', email, ver_code)
          alert("Email sent successfully!", title="Success")
      except Exception as e:
          alert(f"An error occurred while sending the email: {e}", title="Error")
          print(f"Email send error: {e}")


    def generate_ver_code(self):
      alphanumeric_characters = string.ascii_letters + string.digits
      ver_code = ''.join(random.sample(alphanumeric_characters, 8))
      return ver_code


