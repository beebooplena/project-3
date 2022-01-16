"""
gspread is imported to get access to the spreadsheet
APi and google drive API

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
    This function will ask for the player`s
    name. If you type numbers, raise value
    error will happen, and you can try again.
    If the name is longer then 20 letters,
    raise valueerror will happen.
    """
    while True:
        print("Welcome!\n")
        name = input("Enter your name:\n")
        try:
            if name.isdigit() == True:
                raise ValueError(f"No numbers permitted, you wrote: {name}")
            elif len(name) >= 20:
                raise ValueError(f"Your name was over 20 caracters: {name}")
            elif name == "":
                raise ValueError("You left name empty")
               
            else: break
        except ValueError as e:
            print(f"Invalid data:{e}, please try again.\n")
    return name
  
        
def update_names_worksheet(data):
    """
    This function will store the names
    in the spreadsheet Quiz Lord Of The Rings.
    This code is borrowed from the Love sandwich
    project with small changes.
    """
    print("updating")
    update_names = SHEET.worksheet("results")
    update_names.append_row(data)
    

"""
I got inspired after watching a video,
  where somebody made a quiz using a 
  class in python. I used this idea.
  The link will take you to the youtube
  video:https://youtu.be/SgQhwtIoQ7o
"""

class Game:
    def __init__(self, grill, answer):
        self.grill = grill
        self.answer = answer


game_quiz = [
    "\nWho is Frodo`s loyal friend that walked with him to Mount doom?\n(a) Gandalf\n(b) Samwise Gamgee\n(c) Aragorn\n\n",
    "How many rings were made for the elves?\n(a) 2\n(b) 4\n(c) 3\n\n",
    ]
questions = [
    Game(game_quiz[0],"b"),
    Game(game_quiz[1],"c"),
]

def run_game(questions):
    """
    This function will run the quiz.
    It will raise a valueerror if 
    a, b, or c is not clicked.
    Then you can try again by using
    while True. It also checks if the answers
    are correct.
    """
    for question in questions:
        while True:
            response = input(question.grill)
            try:
                if response not in ("a", "b", "c"):
                    raise ValueError(f"only a, b or c permitted, you wrote:{response}")
                elif response == question.answer:
                    update_score()
                    break
                else:
                    break
            except ValueError as e:
                print(f"Invalid data: {e}, please try again.\n")
    

score = 0
def update_score():
    """
    This function will increment
    the score by 1
    """
    global score
    score += 1
    return score


def thank_player():
    print("Thank you", playerName, "for taking the quiz, you got:", score, "points")
    print("This is the scorelist of all players:")
    show = SHEET.worksheet("results").get_all_values()
    for row in show:
        print(row)

def main():
    """
    This is the main function and it
    will run all the functions in a
    correct order
    """
    print("********************************")
    print("*    LORD OF THE RINGS QUIZ    *")
    print("*                              *")
    print("********************************\n")
    
    global playerName
    playerName = get_players_names()
    run_game(questions)
    data = [playerName, score]
    results_info = [str(elem) for elem in data]
    update_names_worksheet(results_info)
    thank_player()
 
    
main()
