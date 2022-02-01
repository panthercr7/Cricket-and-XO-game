'************************************************************************************************************************************'
# ------------------------------------------2021-22 Project XI Project-[Dictionary]------------------------------------------------
'************************************************************************************************************************************'
'************************************************************************************************************************************'
#--------------------------------------------------------Synopsis------------------------------------------------------------------
'************************************************************************************************************************************'
# This program allows the user to play a cricket game with compiler and an XO game with his/her friend ^_^ 
###Group Members###
"--------------------------------------------------------------"
"|'     Class    Sec    R.no               Name                    '|"          
"|'     XI       C       37                V.Srikumar              '|"
"|'     XI       C       17                R.Aditya                '|"
"|'     XI       C       21                A.Deenathayalan         '|"
"--------------------------------------------------------------"
#This program uses while loop , if_else ,some string functions, dictionaries in python & that's it...
#------------------------------------------------------------------------------------------------------------------------------------
'************************************************************************************************************************************'
print("Hey!!Hello User , We're glad that you're here :-) :-) :-) ...")
print("Here u can play a cricket game with me and later you can play an XO game with your friend ")
print("Have fun ,but before that try to win the game against me...It's a challenge")
print("All the best")
print(""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Cricket ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 Rules:
* The user should select a number between 0 and 6.
* The computer will also select a number.
* If the number selected by the user and computer are same, then the batter is out.
* The user can choose either to bat or bowl first.
* Each innings lasts for 15 balls and has a maximum of 3 wickets. If either the balls get over or all 3
  wickets fall, the innings end.
* Result is based on who scored the maximum runs. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
print("*"*25,"\tReady for a cricket game??\t","*"*25)
print("Start the whistles!!!!!!")
import random
total1=0
total2=0
wickets=0
balls=0
scorecard1={'Player 1':' ',
           'Player 2':' ',
           'Player 3':' '
}
scorecard2={'Player 1':' ',
           'Player 2':' ',
           'Player 3':' '
}
q=input("\nDO YOU WANT TO BAT OR BOWL FIRST ?")
#If you choose batting
if q.title()=="Bat":
    print("\nYour Score\tComputer score")
    while wickets<3 and balls<15:
        print("\nBall",balls+1)
        y=random.randint(1,6)
        n=int(input())
        print('\t\t',y)
        if n!=y and n in range(1,7):
            total1+=n
            balls+=1
            if wickets<1:
                e=total1
                scorecard1['Player 1']=str(e)
            if wickets>=1 and wickets<2:
                f=total1-e
                scorecard1['Player 2']=str(f)
            if wickets>=2 and wickets<3:
                g=total1-(e+f)
                scorecard1['Player 3']=str(g)
        if n==y:
            wickets+=1
            balls+=1
            print("\tThat\'s OUT!!!\n",'\tScore:',total1,'-',wickets,'\n')
            if wickets==1:
                e=total1
                scorecard1['Player 1']=str(e)
            if wickets==2:
                f=total1-e
                scorecard1['Player 2']=str(f)
            if wickets==3:
                g=total1-(e+f)
                scorecard1['Player 3']=str(g)
    print("\nYour score=",total1,'-',wickets)
    print("Player\'s individual score:\n",scorecard1)
    print("\nTarget=",total1+1)
#2nd innings
    print("*"*100)
    wickets=0
    balls=0
    print("\n\t\t\tYou are bowling now")
    print("\nYour Score\tComputer score")
    while wickets<3 and balls<15:
        print("\nBall",balls+1)
        y=random.randint(1,6)
        n=int(input())
        print('\t\t',y)
        if n!=y and n in range(1,7):
            total2+=y
            balls+=1
            if wickets<1:
                h=total2
                scorecard2['Player 1']=str(h)
            if wickets<2 and wickets>=1:
                i=total2-h
                scorecard2['Player 2']=str(i)
            if wickets<3 and wickets>=2:
                j=total2-(h+i)
                scorecard2['Player 3']=str(j)
            if total2 > total1:
                break
        if n==y:
            wickets+=1
            balls+=1
            print("\tThat\'s OUT!!!\n",'\tScore:',total2,'-',wickets,'\n')
            if wickets==1:
                h=total2
                scorecard2['Player 1']=str(h)
            if wickets==2:
                i=total2-h
                scorecard2['Player 2']=str(i)
            if wickets==3:
                j=total2-(h+i)
                scorecard2['Player 3']=str(j)
    print("\nComputer score=",total2,'-',wickets)
    print("Players\' individual score:\n",scorecard2,'\n\nRESULT:')
    if total2>total1:
        print("Computer win by",3-wickets,'wicket(s) with',15-balls,'ball(s) to spare\nBetter Luck Next Time:(')
    if total2 < total1:
        print("You win by",total1-total2,'run(s) :):)')
    if total2==total1:
        print("It\'s a tie")
    print("\n","*"*100)
    
#If you choose bowling
wickets=0
balls=0
if q.title()=="Bowl":
    print("\nYour Score\tComputer score")
    while wickets<3 and balls<15:
        print("Ball",balls+1)
        y=random.randint(1,6)
        n=int(input())
        print('\t\t',y)
        if n!=y and n in range(1,7):
            total1+=y
            balls+=1
            if wickets<1:
                e=total1
                scorecard1['Player 1']=str(e)
            if wickets<2 and wickets>=1:
                f=total1-e
                scorecard1['Player 2']=str(f)
            if wickets<3 and wickets>=2:
                g=total1-(e+f)
                scorecard1['Player 3']=str(g)
        if n==y:
            wickets+=1
            balls+=1
            print("\tThat\'s OUT!!!\n","\tScore:",total1,'-',wickets)
            if wickets==1:
                e=total1
                scorecard1['Player 1']=str(e)
            if wickets==2:
                f=total1-e
                scorecard1['Player 2']=str(f)
            if wickets==3:
                g=total1-(e+f)
                scorecard1['Player 3']=str(g)
    print("\nComputer score=",total1,'-',wickets,'\n')
    print("Players\' individual score:\n",scorecard1)
    print("Target=",total1+1)
#2nd innings
    print("*"*100)
    print("\nYou are batting now")
    wickets=0
    balls=0
    print("\nYour score\tComputer score")
    while wickets<3 and balls<15:
        print("Ball",balls+1)
        y=random.randint(1,6)
        n=int(input())
        print('\t\t',y)
        if n!=y and n in range(1,7):
            total2+=n
            balls+=1
            if wickets<1:
                h=total2
                scorecard2['Player 1']=str(h)
            if wickets<2 and wickets>=1:
                i=total2-h
                scorecard2['Player 2']=str(i)
            if wickets<3 and wickets>=2:
                j=total2-(h+i)
                scorecard2['Player 3']=str(j)
            if total2 > total1:
                break
        if n==y:
            wickets+=1
            balls+=1
            print("\tThat\'s OUT!!!\n",'\tScore:',total2,'-',wickets)
            if wickets==1:
                h=total2
                scorecard2['Player 1']=str(h)
            if wickets==2:
                i=total2-h
                scorecard2['Player 2']=str(i)
            if wickets==3:
                j=total2-(h+i)
                scorecard2['Player 3']=str(j)
    print("\nYour score=",total2,'-',wickets,'\n')
    print("Player\'s individual score:\n",scorecard2,'\n\nRESULT:')
    if total2>total1:
        print("You win by",3-wickets,'wicket(s) with',15-balls,'ball(s) to spare :):)')
    if total2 < total1:
        print("Computer win by",total1-total2,'run(s)\nBetter Luck Next Time:(')
    if total2==total1:
        print("It\'s a tie")
    print("\n","*"*100)
    
#XO game
print("\nHey hello user , Welcome back , hope you had a nice time playing with me , now enjoy playing XO with your friend")
print("Are you guys ready?")
print("---------------------------------------------------Initializing-XO---------------------------------------------")
print("---------------------------------------------------------XO----------------------------------------------------")
board = {
    'R1': ' ', 'R2': ' ', 'R3': ' ',
    'R4': ' ', 'R5': ' ', 'R6': ' ',
    'R7': ' ', 'R8': ' ', 'R9': ' ',
}


def check(pl1, pl2):
    if board['R1']==board['R2']==board['R3']=='X' or board['R4']==board['R5']==board['R6']=='X' or board['R7']==board['R8']==board['R9']=='X':
        print(pl1+' Won!')
        return 1
    elif board['R1']==board['R4']==board['R7']=='X' or board['R2']==board['R5']==board['R8']=='X' or board['R3']==board['R6']==board['R9']=='X':
        print(pl1+' Won!')
        return 1
    elif board['R1']==board['R5']==board['R9']=='X' or board['R3']==board['R5']==board['R7']=='X':
        print(pl1+' Won!')
        return 1
    elif board['R1']==board['R2']==board['R3']=='O' or board['R4']==board['R5']==board['R6']=='O' or board['R7']==board['R8']==board['R9']=='O':
        print(pl2+' Won!')
        return 1
    elif board['R1']==board['R4']==board['R7']=='O' or board['R2']==board['R5']==board['R8']=='O' or board['R3']==board['R6']==board['R9']=='O':
        print(pl2+' Won!')
        return 1
    elif board['R1']==board['R5']==board['R9']=='O' or board['R3']==board['R5']==board['R7']=='O':
        print(pl2+' Won!')
        return 1


print('R1 | R2 | R3')
print('------------')
print('R4 | R5 | R6')
print('------------')
print('R7 | R8 | R9')
print('****************************')

player1 = str(input('Name of player one :'))
player2 = str(input('Name of player two :'))
player = player1
rounds = 1

while True:
    print(board['R1']+' | '+board['R2']+' | '+board['R3'])
    print('---------')
    print(board['R4']+' | '+board['R5']+' | '+board['R6'])
    print('---------')
    print(board['R7']+' | '+board['R8']+' | '+board['R9'])
    print('****************************')
    if check(player1, player2):
        break
    if rounds > 9:
        print("Game over!!!")
        print("Draw!!!")
        break

    print(rounds)
    while True:
        if player == player1:
            p1 = input('Player one :')
            if p1.upper() in board and board[p1.upper()] == ' ':
                board[p1.upper()] = 'X'
                player = player2
                break
            else:
                print('Invalid input! Try again')
        else:
            p2 = input('Player two :')
            if p2.upper() in board and board[p2.upper()] == ' ':
                board[p2.upper()] = 'O'
                player = player1
                break
            else:
                print('Invalid input! Try again')

    rounds += 1

    print('****************************')


    
        
