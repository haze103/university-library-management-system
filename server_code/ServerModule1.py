import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import requests
from datetime import *
import random
import string


@anvil.server.callable
def get_book_list():
  return app_tables.tblbooks.search()

@anvil.server.callable
def search_books(query):
    books = get_book_list()  # Retrieve the list of all books
  
    if query:
        filtered_books = [
            book for book in books
            if query.lower() in book['strBookTitle'].lower()
            or query.lower() in book['intISBN']
        ]
        return filtered_books
    else:
        return books

@anvil.server.callable
def validate_reservation_details(user_id, full_name, isbn, title, borrowed_date):
  user_info_row = app_tables.tbluserinformation.get(strUniversityID=user_id, strUserFirstName=full_name.split()[0], strUserLastName=full_name.split()[-1])
  book_row = app_tables.tblbooks.get(intISBN=isbn, strBookTitle=title)
  
  current_date = date.today()
  if borrowed_date > current_date + timedelta(days=14):
      return "Borrowed date should be within 2 weeks from the current date."
  
  if not user_info_row:
      return "User information does not match."
  
  if not book_row:
      return "Book information does not match."
  
  return "Valid"

@anvil.server.callable
def validate_user_credentials(email, password):
    user_account = app_tables.tbluseraccounts.get(strUserEmail=email, strUserPassword=password)
    
    if user_account:
        return True
    else:
        return False


@anvil.server.callable
def validate_admin_ID(admin_id):
    admin_account = app_tables.tbladmininformation.get(strAdminID=admin_id)
    
    if admin_account:
        return True
    else:
        return False

@anvil.server.callable
def validate_admin_credentials(email, password):
    admin_login = app_tables.tbladminaccounts.get(strAdminEmail=email, strAdminPassword=password)
    
    if admin_login:
        return True
    else:
        return False