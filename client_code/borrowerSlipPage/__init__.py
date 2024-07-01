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

    def cmdHomeBtn_click(self, **event_args):
      from ..homePage import homePage
      self.secContentPanel.clear()
      self.secContentPanel.add_component(homePage())

    def cmdConfBtn_click(self, **event_args):
      strUserID = self.txtUniqueID.text.strip()
      strFullName = self.txtName.text.strip()
      intIsbn = self.txtISBN.text.strip()
      strTitle = self.txtBookTitle.text.strip()
      datBorrowed = self.txtDateBorrowed.date

      strResult = anvil.server.call('validate_reservation_details', strUserID, strFullName, intIsbn, strTitle, datBorrowed)

      if strResult == "Valid":
        alert(content=confirmReservation(), title="Confirm your reservation", large=True, buttons=[])
      else:
        alert(strResult)

