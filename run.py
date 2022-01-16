"""
gspread is imported to get access to the spreadsheet
APi and google drive API

"""
import random
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
PLAYER_NAME = ""


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
            if name.isdigit():
                raise ValueError(f"No numbers permitted, you wrote: {name}")
            elif len(name) >= 20:
                raise ValueError(f"Your name was over 20 caracters: {name}")
            elif name == "":
                raise ValueError("You left name empty")
            else:
                break
        except ValueError as error:
            print(f"Invalid data:{error}, please try again.\n")
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


class Game:
    """
    I got inspired after watching a video,
    where somebody made a quiz using a
    class in python. I used the start
    of his idea.
    The link will take you to the youtube
    video:https://youtu.be/SgQhwtIoQ7o
    """
    def __init__(self, grill, answer):
        self.grill = grill
        self.answer = answer


game_quiz = [
    "\nWho is Frodo`s loyal friend that walked with him to Mount doom?"
    "\n(a) Gandalf\n(b) Samwise Gamgee\n(c) Aragorn\n\n",
    "How many rings were made for the elves?\n(a) 2\n(b) 4\n(c) 3\n\n",
    "Who released King Theoden from the spell of Saruman?\n(a) Elves\n(b)"
    " Gandalf\n(c) Frodo\n\n",
    "Name Sauron's fortress in Mordor\n(a) Barad-dûr\n(b) Barad-kar\n(c)"
    "Barad-mov\n\n",
    "What was the riddle that Gandalf could not figure out to open the door?"
    "\n(a) speak in tongues\n(b) speak wise and enter\n"
    "(c) speak friend and enter\n\n",
    "What are the names of the two towers?\n(a) Minas Tirith and Minas Morgul"
    "\n(b) Minas Tirith and Minas Morkul"
    "\n(c) Minas Trith and Minas Morgul\n\n",
    "Name Lady of Caras Galadhon.\n(a) Lady love\n(b) Lady of Caras Galadhon"
    "\n(c) Lady of sath Toth\n\n",
    "Who is Isildur's heir?\n(a) Legolas\n(b) Boromir\n(c) Aragorn\n\n",
    "Who did Sam eventually marry?\n(a) Rosie Cotton\n(b) Sally Rose\n(c)"
    " Mary Cotton\n\n",
    "What is Bilbo's relation to Frodo?\n(a)"
    "  Frodo is Bilbo's second cousin\n"
    "(b)  Frodo is Bilbo's third cousin\n(c)  "
    "Frodo is Bilbo's fourth cousin\n\n",


    ]
questions = [
    Game(game_quiz[0], "b"),
    Game(game_quiz[1], "c"),
    Game(game_quiz[2], "b"),
    Game(game_quiz[3], "a"),
    Game(game_quiz[4], "c"),
    Game(game_quiz[5], "a"),
    Game(game_quiz[6], "b"),
    Game(game_quiz[7], "c"),
    Game(game_quiz[8], "a"),
    Game(game_quiz[9], "a"),
]


def run_game():
    """
    This function will run the quiz.
    It will raise a valueerror if a,
    b, or c is not clicked.Then you
    can try again by using
    while True. The questions are
    shuffled. The function will also
    checks if the answers
    are correct.
    """
    for question in questions:
        random.shuffle(questions)
        while True:
            response = input(question.grill)
            try:
                if response not in ("a", "b", "c"):
                    raise ValueError(
                        f"only a, b or c permitted,you wrote:{response}")
                elif response == question.answer:
                    update_score()
                    break
                else:
                    break
            except ValueError as error:
                print(f"Invalid data: {error}, please try again.\n")


SCORE = 0


def update_score():
    """
    This function will increment
    the score by 1
    """
    global SCORE
    SCORE += 1
    return SCORE


def thank_player():
    """
    This function will print the
    name of the player and the
    player's score. It will
    also display all the
    players score
    """
    print("Thank you", PLAYER_NAME, "you got:", SCORE, "points")
    show = SHEET.worksheet("results")
    show_all = show.get_all_values()
    print("This is the scorelist of all players")
    for row in show_all:
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
    global PLAYER_NAME
    player_name = get_players_names()
    run_game()
    data = [player_name, SCORE]
    results_info = [str(elem) for elem in data]
    update_names_worksheet(results_info)
    thank_player()


main()
