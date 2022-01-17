

# Welcome To The Lord of The Rings Mock Terminal Python Quiz

This quiz will check the players knowledge about the lord of the rings triology. It contains ten questions that are randomed shuffled each time the user are playing. It can be a nice quiz to be used with friends or be used as a fun activity, that can be done with colleges. The quiz master can use the spreadsheet to get an overview of the players names and scores.

Visit the quiz game here: https://lord-of-the-ringsquiz.herokuapp.com/


![Responsive](assets/screenshots/responsive.png)

### How to play the quiz game
* First the quiz game will ask for you name. The quiz starts if the name is correctly typed. The name can not be empty or in numbers.
* The player will be asked one question at a time, and the player needs to choose answer alternatives a, b or c.
* After the questions are answered, the player will get an overview of his/her score.
* The player will also get an overview of the other players scores.
* The players name and score will be updated in a spreadsheet.

![start](assets/screenshots/start-screen.png)

### Owner`s goal
* To get players play and enjoy the quiz game.
* To get names and scores into to the spreadsheet, and
then be able to evaluate the players.


### User`s goals
* They want to play a quiz game that are easy to understand.
* The user wants to know what kind of game/ quiz this is.
* The user wants to see the score.
* The user wants to see other players score.




### Lucid chart program overview
I used Lucid chart program to make an overview of how the quiz program works. It is a nice way to get an practical overview of the program. As displayed here, the steps goes like this:

*  The program starts, and ask the player for his or her name.
*  If the player writes in numbers or more then 20 caracters long, or just type enter, an valueerror arise and the player must try again to write the name.

* When the name is valid, the quiz starts and the player receives the first question. 

* To answer, the player needs to type a, b or c. If the player types numbers, other letters or empty, an valueerror will arise, and the player must try again.

* If the answer is valid, the next question will happen.

* After the quiz, the player will get an overview of the score. The player will also get an overview of other players names and scores.

* The player's name and score will then be updated in a spreadsheet.

* The program ends.

![Lucid chart](assets/screenshots/lucidchart.png)


## Features
The questions will be in different order each time a player plays the quiz. This makes the quiz a bit more difficult.

<br>

![quiz-screen](assets/screenshots/quiz-screen.png)

<br>

The terminal will raise valueerrors if the player writes the name in numbers, or if the name is longer then 20 caracters and if the name is empty.

<br>


![number-error](assets/screenshots/number-valueerror.png)
<br>

![empty-error](assets/screenshots/invalid-data-empty.png)

<br>

![name is to long](assets/screenshots/invalid-data-to-long.png)

The player name and score is displayed after the quiz is finished. The player also receives an overview of other players that has played the quiz.

<br>

![score](assets/screenshots/showing-score.png)

<br>

Another feature is that the names and scores are updated to a spreadsheet. A quizmaster/ owner can evaluate the players score. The owner can delete the players scores and names in the spreadsheet.

![sheet](assets/screenshots/spreadsheet.png)


### Future Features
* Include a highscore record of the players.
* Make the quiz more exciting by developing the usage of the class and adding more exciting ways to answer questions.


### Technology
I used different technologies and languages to make this python quiz. Here are some of the languages and technologies:
* Lucid chart
* VS-code
* Git Hub
* Python
* Heroku
* Node.js
* google spreadsheet
* Google spreadsheet API
* Google drive API
* PEP8 online
* Am I responsive? website
* import random

## Model
The quiz is a commandline based python program, where I also included a class. The class has questions and answers as properties. A list holding the questions and answer alternatives are passed to question property and the correct answers are passed to the answer property. The way I used the class consept, is a bit different from what I have learned about it. It does not include another function below with self passed into it.

## Testing
* First I checked if the name input worked. I checked in the local terminal and then in the Code Institute Heroku terminal. I typed in a number and an valuerror occurred.
I tried again, now just pushing enter. A new valueerror occurred. I tried again and wrote more then 20 caracters and a new valueerror occurred. The valueerrors works with the name input. Lastly I wrote a name and it worked.
*  Secondely I checked if the quiz is working. I checked this first in the local terminal and then in the Code Institute Heroku terminal. First I check if the questions are randomely shuffled, and it does. I then check if I type another letter then a, b or c. I test different letters and numbers as answers and a valueerror occurs correctly.
* I check if the right name and if the score is displayed correctly at the end at the overview. I also check if the spreadsheet is updating correctly and it does.


### Game and buttons



### Validator tester








## Bugs



### Unfixed Bugs

## Deployment



## Credits 

* I would like to thank my mentor Dick Vlaanderen for guiding me.



* I would like to thank the tutor support of code institute for supporting me.

* I would like to thank the slack community for help.





## Content





### Media
