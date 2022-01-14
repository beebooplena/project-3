"""
imported
"""
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Quiz Lord Of The Rings')


def get_players_names():
    """
    This function will store the players name in
    the worksheet
    """
    enter_name = input("enter your name:\n")
    results_info = enter_name.split(",")
    validate_name(results_info)


def validate_name(values):
    """
    jjj
    """
    try:
        if len(values) != 1:
            raise ValueError(f"Only one name is permitted, you wrote {len(values)}")
    except ValueError as e:
        print(f"invalid data {e} please try again")
    
get_players_names()
