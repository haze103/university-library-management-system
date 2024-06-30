from ._anvil_designer import studentSignUpPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class studentSignUpPage(studentSignUpPageTemplate):
    def __init__(self, **properties):
      # Set Form properties and Data Bindings.
      self.init_components(**properties)
      
      # Call the server function to get college names
      college_names = anvil.server.call('get_college_names')
      # Populate the dropdown with the college names
      self.lstColleges.items = college_names
      
      # Initialize departments list with an empty list
      self.lstDepartments.items = []
      
      # Bind the change event for the college dropdown
      self.lstColleges.set_event_handler('change', self.lst_colleges_change)
      
      # Set the initial value and trigger the change handler
      if college_names:
        self.lstColleges.selected_value = college_names[0]  # Default to the first college
        self.lst_colleges_change()  # Call the change handler to populate departments initially
  
    def lst_colleges_change(self, **event_args):
      # Get the selected college
      selected_college = self.lstColleges.selected_value
      if selected_college:
        # Call the server function to get department names for the selected college
        department_names = anvil.server.call('get_department_names_by_college', selected_college)
        # Populate the dropdown with the department names
        self.lstDepartments.items = department_names

    def cmdCancelBtn_click(self, **event_args):
      self.navigate_to_student_sign_in_page()

    def cmdStudBtn_click(self, **event_args):
      student_num = self.txtStudNum.text
      last_name = self.txtLName.text
      first_name = self.txtFName.text
      middle_name = self.txtMName.text
      department_name = self.lstDepartments.selected_value
      email = self.txtEmailAdd.text
      password = self.txtPassword.text

      if not all([student_num, last_name, first_name, department_name, email, password]):
        alert("Please fill in all required fields.")
        return

      # Check for correct email validity
      if not email.endswith("@gmail.com"):
        alert("Please enter a valid email ending")
        return
      
      try:
        anvil.server.call('add_student', student_num, last_name, first_name, middle_name, department_name, email, password)
        Notification('Account Created!').show()
        self.clear_inputs()
        self.navigate_to_student_sign_in_page()
        
      except ValueError as e:
        alert(f"Error creating account: {str(e)}")

    def clear_inputs(self):
      self.txtStudNum.text = ""
      self.txtLName.text = ""
      self.txtFName.text = ""
      self.txtMName.text = ""
      self.lstColleges.selected_index = 0
      self.lstDepartments.items = []
      self.txtEmailAdd.text = ""
      self.txtPassword.text = ""

    def navigate_to_student_sign_in_page(self):
      self.secContentPanel.clear()
      from ..studentSignInPage import studentSignInPage
      self.secContentPanel.add_component(studentSignInPage())
