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
    global score
    score += 1
   
    
def update_score_worksheet(score):
    total = [str(score)]
    print(total)
    update_points = SHEET.worksheet("results")
    update_points.append_row[2](total)
    print("du klarte det")
    



def main():
    print("********************************")
    print("*    LORD OF THE RINGS QUIZ    *")
    print("*                              *")
    print("********************************")
    data = get_players_names()
    results_info = [str(elem) for elem in data]

    update_names_worksheet(results_info)
    print(type(results_info))
    print(results_info)

    run_game(questions)
    update_score()
    update_score_worksheet(score)


main()
