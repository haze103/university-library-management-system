import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import requests
from datetime import datetime
import random
import string


@anvil.server.callable
def confirm_user_reservation(student_num, password):
    student_email = app_tables.tblstudentaccount.get(strStudentUserEmail=email)
    
    if student_email and student_email['strStudentUserPassword'] == password:
      session_id = generate_unique_session_id()  # Generate a unique session ID
      app_tables.tblloginsession.add_row(
        intStudentUserID=student_email['strStudentUserEmail'],
        strSessionID=session_id,
        datLastLogin=datetime.now()
      )
      return session_id  # Return the session ID upon successful login
    else:
      raise ValueError("Incorrect student number or password. Please try again.")

@anvil.server.callable
def check_user_cred(student_num, password):
    student_account = app_tables.tblstudentaccount.get(strStudentID=student_num)
    
    if student_account and student_account['strStudentUserPassword'] == password:
      app_tables.tblloginsession.add_row(
        intStudentUserID=student_account['intStudentUserID'],
        datLastLogin=datetime.now()
      )
    else:
      raise ValueError("Incorrect student number or password. Please try again.")


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
