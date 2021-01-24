import random
play = True
ps = 0
cs = 0
Input = ["Stone", "Paper", "Scissors","Stone", "Paper", "Scissors"]
plyname = input('Enter you Name--')
E = int()

while play == True:
    computer = random.choice(Input)
    player = str(input(str(plyname) + ' your turn("Stone", "Paper", "Scissors")-- '))
    print('Computer turns- '+computer)
    if player == computer:
        print('Tie')
        ps = ps + 5
        cs = cs + 5
    elif player == 'Stone':
        if computer == 'Scissors':
            print('well done Human, you made it , you smashed computer')
            ps = ps + 10
        else:
            print('you loose! computer covered you')
            cs = cs + 10  # paper
    elif player == 'Paper':
        if computer == 'Stone':
            print("well done Human, you made it , you covered computer ")
            ps = ps + 10
        else:
            print('you loose! computer cut down you in halves')  # Scissors
            cs = cs + 10
    elif player == 'Scissors':
        if computer == 'Paper':
            print('well done Human, you made it , you cut the computer in halves')
            ps = ps + 10
        else:
            print('you loose! computer cut down you in halves')  # stone
            cs = cs + 10
    else:
        print('Invalid command, you Noob! Spelling CHeck KAr ullu!')
        print('Correct Spellings \n Stone \n Paper \n Scissors')

    E = int(input("Wanna Play(1) or Exit()2--"))
    if E == 2:
        break



print('Score of Computer '+ str(cs) + ' Points' +'\n Score of '+ str(plyname) +' '+str(ps) + ' Points')

#for compairing scores
if cs == ps:
    print('Match Score ties, no one wins , you both are noob')
elif cs >= ps:
    print('Computer Wins')
else:
    print(str(plyname) +' Wins')
