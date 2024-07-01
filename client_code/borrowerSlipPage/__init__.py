from ._anvil_designer import borrowerSlipPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..confirmReservation import confirmReservation
from datetime import date


class borrowerSlipPage(borrowerSlipPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.cmdReservationDate.date = date.today() 
    self.cmdReservationDate.enabled = False
    # Any code you write here will run before the form opens.

  def cmdHomeBtn_click(self, **event_args):
    from ..homePage import homePage
    self.secContentPanel.clear()
    self.secContentPanel.add_component(homePage())

  def cmdStudBtn_click(self, **event_args):
    alert(content = confirmReservation(), title = "Confirm your reservation",
         large = True, buttons = [],)

