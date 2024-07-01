from ._anvil_designer import RowTemplate4Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...borrowerSlipPage import borrowerSlipPage


class RowTemplate4(RowTemplate4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def cmdStatusBtn_click(self, **event_args):
    secPanel1 = self.parent
    secPanel2 = secPanel1.parent
    secPanel3 = secPanel2.parent
    secPanel4 = secPanel3.parent
    secPanel5 = secPanel4.parent
    secMainContentPanel = secPanel5.secContentPanel  # To access the secContentPanel

    strBtnTxt = self.cmdStatusBtn.text.lower()
    
    if strBtnTxt == "available":
        secMainContentPanel.clear()
        secMainContentPanel.add_component(borrowerSlipPage())
    else:
        alert("Book is currently unavailable.")

