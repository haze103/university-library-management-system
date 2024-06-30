import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import requests
from datetime import datetime
import random
import string


@anvil.server.callable
def get_department_names():
    """Fetch all department names from the database."""
    departments = app_tables.tbldepartment.search()
    return [dept['strDepartmentName'] for dept in departments]

@anvil.server.callable
def get_college_names():
    """Fetch all college names from the database."""
    colleges = app_tables.tblcollege.search()
    return [college['strCollegeName'] for college in colleges]

@anvil.server.callable
def get_department_names_by_college(college_name):
    """Fetch department names for a given college."""
    college = app_tables.tblcollege.get(strCollegeName=college_name)
    if college:
      college_code = college['strCollegeCode']
      departments = app_tables.tbldepartment.search(strCollegeCode=college_code)
      return [dept['strDepartmentName'] for dept in departments]
    return []

def get_department_code(department_name):
    """Fetch department code for a given department name."""
    dept = app_tables.tbldepartment.get(strDepartmentName=department_name)
    return dept['strDepartmentCode'] if dept else None

def generate_unique_user_id():
    """Generate a new unique numeric user ID."""
    all_users = app_tables.tblstudentaccount.search()
    max_user_id = 0

    for user in all_users:
      user_id = user['intStudentUserID']
      if user_id > max_user_id:
        max_user_id = user_id

    new_user_id = max_user_id + 1 if max_user_id > 0 else 800000001

    return new_user_id

def generate_unique_session_id():
    user_chars = string.ascii_letters + string.digits
    session_id = ''.join(random.choices(user_chars, k=10))  # Generate a random session ID
    
    # Ensure the generated session ID is unique in the table
    existing_sessions = [session['strSessionID'] for session in app_tables.tblloginsession.search()]
    while session_id in existing_sessions:
      session_id = ''.join(random.choices(user_chars, k=10))  # Regenerate the session ID if it already exists
    
    return session_id

@anvil.server.callable
def add_student(student_num, last_name, first_name, middle_name, department_name, email, password):
    """Add student information to the database."""
    if app_tables.tblstudentinformation.get(strStudentID=student_num):
        raise ValueError(f"Student number '{student_num}' already exists.")
      
    student_user_id = generate_unique_user_id()
    department_code = get_department_code(department_name)
  
    if department_code:
        app_tables.tblstudentinformation.add_row(
          strStudentID=student_num, 
          strStudentLastName=last_name, 
          strStudentFirstName=first_name,
          strStudentMiddleName=middle_name, 
          strDepartmentCode=department_code
        )
        app_tables.tblstudentaccount.add_row(
          intStudentUserID=student_user_id, 
          strStudentUserEmail=email, 
          strStudentUserPassword=password,
          strStudentID=student_num, 
          datStudentUserDateCreated=datetime.now()
        )
    else:
      raise ValueError(f"Department '{department_name}' not found.")

@anvil.server.callable
def login_stud_user(student_num, password):
    student_account = app_tables.tblstudentaccount.get(strStudentID=student_num)
    
    if student_account and student_account['strStudentUserPassword'] == password:
      session_id = generate_unique_session_id()  # Generate a unique session ID
      app_tables.tblloginsession.add_row(
        intStudentUserID=student_account['intStudentUserID'],
        strSessionID=session_id,
        datLastLogin=datetime.now()
      )
      return session_id  # Return the session ID upon successful login
    else:
      raise ValueError("Incorrect student number or password. Please try again.")

@anvil.server.callable
def check_session(session_id):
  session = app_tables.tblloginsession.get(strSessionID=session_id)
  
  if session:
    # Update the last login time
    session['datLastLogin'] = datetime.now()
    return session['intStudentUserID']  # Return the associated user ID
  else:
    raise ValueError("Session not found or expired.")

@anvil.server.callable
def logout(session_id):
    session = app_tables.tblloginsession.get(strSessionID=session_id)
    
    if session:
      session.delete()  # Remove the session from the table
      return "Logged out successfully"
    else:
      raise ValueError("Session not found or expired.")


@anvil.server.callable
def check_email(email):
    student_email = app_tables.tblstudentaccount.get(strStudentUserEmail=email)

    if student_email:
      return True
    else:
      raise ValueError(f"Email '{email}' not found.")


@anvil.server.callable
def get_book_list():
  return app_tables.tblbook.search()

@anvil.server.callable
def search_books(query):
    books = get_book_list()  # Retrieve the list of all books
  
    if query:
        # Filter books based on the query string matching any part of the title, ISBN, or status
        filtered_books = [
            book for book in books
            if query.lower() in book['strBookTitle'].lower()
            or query.lower() in book['intISBN']
        ]
        return filtered_books
    else:
        return books



@anvil.server.callable
def send_email_code(email, ver_code):
    api_key = os.environ['MJ_APIKEY_PUBLIC']
    api_secret = os.environ['MJ_APIKEY_PRIVATE']
    mailjet = Client(auth=(api_key, api_secret), version='v3')
    data = {
      'FromEmail': "ulms@mailjet.com",
      'FromName': "University Library Management System",
      'Recipients': [
        {
          "Email": email,
        }
      ],
      'Subject': "Verification Code for ULMS",
      'Text-part': ver_code,
    }
    result = mailjet.send.create(data=data)
    print (result.status_code)
    print (result.json())

