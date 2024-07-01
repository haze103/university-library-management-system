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
def search_books(strQuery):
    books = get_book_list()  # Retrieve the list of all books
  
    if strQuery:
      filtered_books = [
        book for book in books
        if strQuery.lower() in book['strBookTitle'].lower()
        or strQuery.lower() in book['intISBN']
      ]
      return filtered_books
    else:
      return books

@anvil.server.callable
def validate_reservation_details(strUserID, strFullName, intIsbn, strTitle, datBorrowed):
    strUserInfo = app_tables.tbluserinformation.get(strUniversityID=strUserID, strUserFirstName=strFullName.split()[0], strUserLastName=strFullName.split()[-1])
    strBookInfo = app_tables.tblbooks.get(intISBN=intIsbn, strBookTitle=strTitle)
  
    datCurrent = date.today()
    if datBorrowed > datCurrent + timedelta(days=14):
      return "Borrowed date should be within 2 weeks from the current date."
    
    if not strUserInfo:
      return "User information does not match."
    
    if not strBookInfo:
      return "Book information does not match."
    
    return "Valid"

@anvil.server.callable
def validate_user_credentials(strEmail, strPassword):
    strUserAccount = app_tables.tbluseraccounts.get(strUserEmail=strEmail, strUserPassword=strPassword)
    
    if strUserAccount:
      return True
    else:
      return False

@anvil.server.callable
def validate_admin_ID(admin_id):
    strAdminAccount = app_tables.tbladmininformation.get(strAdminID=admin_id)
    
    if strAdminAccount:
      return True
    else:
      return False

@anvil.server.callable
def validate_admin_credentials(strEmail, strPassword):
    strAdminLogin = app_tables.tbladminaccounts.get(strAdminEmail=strEmail, strAdminPassword=strPassword)
    
    if strAdminLogin:
      return True
    else:
      return False

@anvil.server.callable
def get_reserved_books():
    return app_tables.tblreservationlog.search()


@anvil.server.callable
def get_currently_borrowed_books():
    return app_tables.tblborrowerlog.search()