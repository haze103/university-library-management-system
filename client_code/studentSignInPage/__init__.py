from ._anvil_designer import studentSignInPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..popupForgotPass import popupForgotPass
from ..studentSignUpPage import studentSignUpPage

class studentSignInPage(studentSignInPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def cmdForgotPassBtn_click(self, **event_args):
    alert(content = popupForgotPass(), title = "Login Using Code",
         large = True, buttons = [],)

  def linkSignUp_click(self, **event_args):
    self.secContentPanel.clear()
    self.secContentPanel.add_component(studentSignUpPage())

  def enter_click(self):
    student_num = self.txtStudNum.text
    password = self.txtStudPass.text

    if not all([student_num, password]):
      alert("Please fill in all required fields.")
      return

    try:
      anvil.server.call('login_stud_user', student_num, password)
      Notification('Successfully Logged In').show()
      self.clear_inputs()
      self.navigate_to_home_page()
            
    except ValueError as e:
      alert({str(e)})

  def clear_inputs(self):
    self.txtStudNum.text = ""
    self.txtStudPass.text = ""

  def navigate_to_home_page(self):
    from ..studentHomePage import studentHomePage
    self.secContentPanel.clear()
    self.secContentPanel.add_component(studentHomePage())

  def cmdSignInBtn_click(self, **event_args):
    self.enter_click()
    
  def txtStudPass_pressed_enter(self, **event_args):
    self.enter_click()

  def txtStudNum_pressed_enter(self, **event_args):
    self.enter_click()
