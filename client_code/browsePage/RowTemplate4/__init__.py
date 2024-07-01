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
    # Access the parent containers to find secContentPanel
    parent_panel_1 = self.parent
    parent_panel_2 = parent_panel_1.parent
    parent_panel_3 = parent_panel_2.parent
    parent_panel_4 = parent_panel_3.parent
    parent_panel_5 = parent_panel_4.parent
    sec_content_panel = parent_panel_5.secContentPanel  # To access the secContentPanel
    
    button_text = self.cmdStatusBtn.text.lower()
    
    if button_text == "available":
        sec_content_panel.clear()
        sec_content_panel.add_component(borrowerSlipPage())
    else:
        # Book is unavailable, show alert message
        alert("Book is currently unavailable.")

