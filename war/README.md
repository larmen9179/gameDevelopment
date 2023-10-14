# war

For this project, we'll be trying to recreate a card game I've been playing since my middle school days. 

I am talking about the card-game WAR. 


There are several iterations of this card game, including Egyptian War amongst many others. However, for this project we will only be implementing the generic war version.  

RULES

All you really have to know is that ace beats king, king beats queen, queen beats jack, jack beats 10, 10 beats 9 ... and so on. 

The most common way to play this game is with two players, which will be the scope of this project for time's sake. The objective is simple, get all the cards. Shuffle the deck, cut it in half and each player has their deck face down in front of them. This program will handle shuffling and allocating cards for each player, so you don't have to worry about that. 

Whenever the players are ready, they turn all their top card over at the same time. Whichever card is higher wins. The winner takes all the cards and puts them on the bottom of their pile. This basically continues on and on and on... until there are players with identical cards. When this happens, it means WAR!! For clarification, only the card values and numbers can be identical, we DON'T care about suites. 

So what happens during WAR? The two identical cards are left face-up. The players that had identical cards now pull another card from the top of their decks, but this time they leave it face down on their previous card. When the two players are ready, the will once again draw a third card from the top of their decks, now face up. Whichever player has the higher card at this point takes all 6 cards, putting them at the bottom of their deck. If the cards are matching again, then it's DOUBLE WAR. Two cards are placed faced down this time and the third goes face up. It is very unlikely that multiple wars will happen but if they do, there is one rule to remember. For every war that's happend, that's how many cards you place face down before you place them face up to compare. For example, if DOUBLE WAR happens, then each player places TWO cards face down, then they place the third card face up. If TRIPLE WAR happens, then each player places THREE cards down, then they place the fourth face up. If somehow there has been QUINTUPLE WAR, this means the players place FIVE cards face down, before placing their sixth card face up. You get the idea... hopefully. 

Thanks for reading the rules.

PREPARE FOR WAR!!

PS. I created this project within a virtual environment. For any need to use this code, this is optional. If not you would only need the war.py file and make sure you install the packages in the correct directory.