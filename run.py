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
    while True:
        enter_name = input("enter your name:\n")
        results_info = enter_name.split(",")
        if validate_name(results_info):
            print("successful")
            break

    return results_info
        

def validate_name(values):
    """
    This function will raise valueerror if
    there are written more names then one
    """
    try:
        if len(values) != 1:
            raise ValueError(f"only one value is permitted, you wrote{len(values)}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

def update_names_worksheet(data):
    """
    Updating players name in the worksheet
    """
    print("updating")
    update_names = SHEET.worksheet("results")
    update_names.append_row(data)
    print("funker")

class Game:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

questions = [
    "who is Frodo`s loyal friend that walked into the Mount Doom?\n(a) Gandalf\n(b) Samwise Gamgee\n(c)Aragorn\n\n"
    ]

answers = [
    Game(questions[0],"b")
    ]

def run_game(questions):
    score = 0
    for question in questions:
        answer = input(question)
        print("hei")

run_game(questions)

#data = get_players_names()
#results_info = [str(elem) for elem in data]

#update_names_worksheet(results_info)

