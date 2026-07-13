# Blackjack
Python Blackjack to play in terminal

How to install 
-
- `git clone https://github.com/Dai-Major72/Blackjack.git`
- or download the zip and extract it
- `sudo ./install`

How to play
-
- write `blackjack` in terminal
- You first give your name, then choose to Bet, change player, or quit.
- you can close and come back later, saved on the name you gave.

Rules
-
 2 wins conditions : Score under 22, and higher than the dealer.
You'll get 2 cards that will get you a score, you can choose to take another card (Hit), or to stop here and let the Dealer start his round (Stay).
When you stay, and if you didn't Bust (score higer than 21), the Dealer start the same process.
The Dealer cannot go higher than 21, and will stop drawing cards at 17.
If the dealer Bust, and you didn't, you win
 If your score's higher than the Dealer's, you win

Card values : 
- From 2 to 10 cards values are worth their numbers
- Faces are worth 10 (from jack to king)
- Aces are worth either 1 or 11, depends on if your score will go above 21 or not. It will always be shown the highest actual score
- Ex :  
    Ace + king = 21 (11 + 10)    
    Ace + Queen + 5 = 16 (1 + 10 + 5)    
    here the ace is lowered because the max score is too high
  
Why
-
There's my first so called 'project', wich is a little tiny python blackjack.
I did it to train with python class, list, file handling...
Then i realised that i need to understand how you share somethhing online correclty !
So i made a bash script (wow)

Next to come : 'Double' and 'Split' game mechanics. Better output and maybe a GUI with pygame. maybe.
