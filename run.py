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
    name and store it in a list. The name
    will be validated in another function
    This code is borrowed from the
    Love sandwitch project with samll changes.
    """
    while True:
        enter_name = input("Enter your name:\n")
        results_info = enter_name.split(",")
        if validate_name(results_info):
            print("successful")
            break

    return results_info
        

def validate_name(values):
    """
    This function will raise valueerror if
    there are written more names then one.
    Then it will ask again for your name.
    This code is borrowed from Love Sandwitch
    project, with small changes.
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
    This function will store the names
    in the spreadsheet Quiz Lord Of The Rings.
    This code is borrowed from the Love sandwich
    project with small changes.
    """
    print("updating")
    update_names = SHEET.worksheet("results")
    update_names.append_row(data)
    print("funker")

"""
I got inspired after watching a video where somebody made a quiz
by using class in python. I borrowed some of his ideas
 https://youtu.be/SgQhwtIoQ7o
"""

class Game:
    def __init__(self, grill, answer):
        self.grill = grill
        self.answer = answer


game_quiz = [
    "Who is Frodo`s loyal friend that walked with him to Mount doom?\n(a) Gandalf\n(b) Samwise Gamgee\n(c) Aragorn\n\n",
    "How many rings were made for the elves?\n(a) 2\n(b) 4\n(c) 3\n\n",
    ]
questions = [
    Game(game_quiz[0],"b"),
    Game(game_quiz[1],"c"),
]

def run_game(questions):
    """
    This function will run the quiz
    is will also validate the correct
    input. It will raise valueerror
    if a, b, or c is not clicked on.
    It will ask the question
    again with because of the while true.
    It also checks if the answer is correct.
    """
    for question in questions:
        while True:
            response = input(question.grill)
            try:
                if response not in ("a", "b", "c"):
                    raise ValueError(f"only a, b or c permitted, you wrote{response}")
                elif response == question.answer:
                    update_score()
                    print(score)
                    print("hurra")
                    break
                else:
                    print("Feil svar")
                    print(score)
                    break
            except ValueError as e:
                print(f"Invalid data: {e}, please try again.\n")
    

score = 0
def update_score():
    """
    This function will increminent
    the score by 1 if the answer
    is correct
    """
    global score
    score += 1
    return score


def update_score_worksheet(score):
    """
    This function will store the players
    score in the spreadsheet column 2
    """
    total = [str(score)]
    update_points = SHEET.worksheet("results").col_values(2)
    update_points.append_row(total)
    update_names.append_row(data)
    print(column)
    


def showing_spreadsheet():
    show = SHEET.worksheet("results").get_all_values()
    print(f"{results_info} Thank you for playing the Lord Of The Rings quiz. Your score is: {total}")
    print(show)
   



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
    data = get_players_names()
    results_info = [str(elem) for elem in data]
    update_names_worksheet(results_info)
    print(type(results_info))
    print(results_info)
    run_game(questions)
    update_score()
    
    showing_spreadsheet()


main()
