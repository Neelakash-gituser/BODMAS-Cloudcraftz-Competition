# BODMAS-Cloudcraftz-Competiton
This is first in the CloudCraftz internal competition series designed to help employees hone their
end-to-end development and deployment skills with a focus on algorithm design.

## Round 1 
- a .Breaking up the problem into its component parts
- b. High level design
- c. Algorithm design
- d. Language Choice
- e. Web deployment choice

## Round 2
- a. Gameplay
- b. UI
- c. Web deployment
- d. Documentation and Testing

## The problem Statement

The BODMAS game is based on simple arithmetic equations, with the principle that in solving an
equation read from left to right, we first perform Division, then Multiplication, then addition and
subtraction. As an example,

Consider 4 + 3 x 5. If we solve from left to right the answer is 35. However with BODMAS the
answer is 19 and this is the arithmetic convention.
Similarly let us consider 6 + 8 / 2 . The Division operator takes precedence, Hence the answer will
be 10 and not 7.

We keep this principle in mind in setting up a simple arithmetic game, which combines BODMAS and
the same structure that is present in a game like mastermind.

The player is given a grid that looks like this:
N1 O1 N2 O2 N3 = N4
N1, N2, N3 are single digit numbers from 0 to 9.
N4 can be a one or two digit number.
O1 is an arithmetic operator It can be + - x / (add subtract multiply divide)
O2 is an arithmetic operator It can be + - x / (add subtract multiply divide)
In playing the game, N4 is given to the player at the beginning of the game.

**Example 1) Consider the true equation as 6 + 5 x 7 = 41**
The player to start of with only has 41 to start with. As a simple example, the player could start with
various alternatives:

5 x 9 - 4 = 41
8 X 5 + 1 = 41
4 X 9 + 5 = 41
6 x 6 + 5 = 41
6 + 5 x 7 = 41

(many other feasible solutions exist)

Let us assume we give a player 3 guesses in maximum.
Let us say the first guess is 5 x 9 - 4 = 41
We use a traffic signal type system to give feedback.
N1- 5 -5 is present in the equation but in the wrong position. This is colour coded yellow.
O1 X X is present but in the wrong position. Colour coded yellow.
N2-9 9 is not present in the equation. Colour coded red.
02 - - is not present in the equation . Colour coded red.
N3-4 4 is not present in the equation. Colour coded red.
We know 5 is present in a different position x(multiply) is present , 9,4 are not.
A feasible guess which meets this is: 1 + 8 x 5 = 41.
Now both the signs are in the right position so the feedback is
N1 red O1 green N2 red O2 green N3 yellow
Now we know both operators, we also know 1,8, 9, 4 are not present. By elimination we also know
the position of 5.
This leaves us with 0,2, 3,6 ,7,9. Through looking back at our original feasible equations we can see
that the only solution possible is: 6 + 5 x 7 = 41.

**Example 2) Consider the following equation 2 + 2 + 2 = 6**
The player only has 6 as initial information. Combinations could include
6 + 1 – 1 = 6
2 x 2 + 2 = 6
3 + 3 / 1 = 6
1 + 4 + 1 = 6
3 x 3 - 3 = 0
6 + 0 - 0 = 6
Let us say the first guess is 3 x 3 – 3 = 0
In this case all are red, and the player knows that the possible operators are + and / and 3 is not
present.
Let us say the guess is 4 + 2 / 1 = 6
Here N1 is red, O1 is green N2 is green O2 is red N3 is red,
We now effectively know both operators. We know 3,4,1 are not there.
Effectively we get 2 + 2 + 2 = 6

**Example 3) Consider a third equation 5 x 3 + 0 = 15**
Suppose an initial guess is 2 x 7 + 1 = 15
In this case N1 is red O1 is green N2 is red O2 is green N3 is red
We know both operators we know 2, 7, 1 are not present.
So one guess that is logical is 4 x 3 + 3 = 15

Feedback N1 red O1 green N2 green O2 green N3 green
We now know a second 3 is not present, as is 4,2,7,1 are ruled out. So the balance digits available
are 5, 6, 8, 9,0 .
Given the structure, the only option possible is 5 X 3 + 0.

**Example 4) We consider one final instance 7 x 0 + 6 = 6**
Consider the first guess 2 + 2 + 2 = 6, only 1 plus sign is in the right place. (O2)
Consider a second guess 6 - 3 + 3 = 6 Again only the plus is in the right place. 6, 3, 2, and two signs
are ruled out.
8 x 0 + 6 = 6 Now all the responses are right, except N1.
4, 7, 9 are still possibilities and it can take more chances.
Therefore while 3 chances should be adequate in most cases and 2 in many cases, there are
situations in which you could guess reasonably and not get the answer in 3 chances.
We need to code this in a manner similar to wordle with boxes in the following structure:
N1 01 N2 O2 N3 = N4
The true equation will be stored somewhere.
The program will check values and code as follows
Position wrong, value correct : yellow
Position and value both correct : green
Position and value both wrong : red.
As the guesses come, we need an entry key-board with the operators and numbers 0-9 displayed
with the colours changing as feedback is obtained on the presence/absence of the number and
operator.



