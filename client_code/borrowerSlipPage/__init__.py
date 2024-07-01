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
        self.init_components(**properties)
        self.cmdReservationDate.date = date.today() 
        self.cmdReservationDate.enabled = False

    def cmdHomeBtn_click(self, **event_args):
        from ..homePage import homePage
        self.secContentPanel.clear()
        self.secContentPanel.add_component(homePage())

    def cmdConfBtn_click(self, **event_args):
        user_id = self.txtUniqueID.text.strip()
        full_name = self.txtName.text.strip()
        isbn = self.txtISBN.text.strip()
        title = self.txtBookTitle.text.strip()
        borrowed_date = self.txtDateBorrowed.date

        result = anvil.server.call('validate_reservation_details', user_id, full_name, isbn, title, borrowed_date)

        if result == "Valid":
            alert(content=confirmReservation(), title="Confirm your reservation", large=True, buttons=[])
        else:
            alert(result)

