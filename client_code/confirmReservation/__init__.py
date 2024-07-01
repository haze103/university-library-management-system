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
      



