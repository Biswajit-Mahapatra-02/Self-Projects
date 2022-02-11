from typing import Any


positions={'00':' ','01': ' ','02': ' ','10': ' ','11': ' ','12': ' ','20': ' ','21': ' ','22': ' '}
itr=0
itr0=0
player1=Any
player2=Any
def printer():
    itr=0
    itr0=0
    global positions
    print('Current situation:\n')
    for x in range(0,3):
        print('-------------')
        for y in range(0,13):
            if y%4==0:
                print('|',end='')
                check=0
            else:
                if check == 1:
                    global positons
                    a=str(itr0)+str(itr)
                    print(positions[a],end ='')
                    itr+=1
                    if itr>2:
                        itr=0
                        itr0+=1
                    check+=1
                    continue
                check+=1
                print(' ', end='')
            if y == 12: print('')
        if x == 2: 
            print('-------------')
def x_engine(pos):
    global positions
    if pos == 1 and positions['00']==' ': positions['00']='x'
    elif pos == 2 and positions['01']==' ': positions['01']='x'
    elif pos == 3 and positions['02']==' ': positions['02']='x'
    elif pos == 4 and positions['10']==' ': positions['10']='x'
    elif pos == 5 and positions['11']==' ': positions['11']='x'
    elif pos == 6 and positions['12']==' ': positions['12']='x'
    elif pos == 7 and positions['20']==' ': positions['20']='x'
    elif pos == 8 and positions['21']==' ': positions['21']='x'
    elif pos == 9 and positions['22']==' ': positions['22']='x'
    else: print('value already recorded there, please select a new cell')

def o_engine(pos):
    global positions
    if pos == 1 and positions['00']==' ': positions['00']='o'
    elif pos == 2 and positions['01']==' ': positions['01']='o'
    elif pos == 3 and positions['02']==' ': positions['02']='o'
    elif pos == 4 and positions['10']==' ': positions['10']='o'
    elif pos == 5 and positions['11']==' ': positions['11']='o'
    elif pos == 6 and positions['12']==' ': positions['12']='o'
    elif pos == 7 and positions['20']==' ': positions['20']='o'
    elif pos == 8 and positions['21']==' ': positions['21']='o'
    elif pos == 9 and positions['22']==' ': positions['22']='o'
    else: print('value already recorded there, please select a new cell')
    
def checking_engine():
    global positions
    if positions['00'] == positions['01'] == positions['02'] and positions['00']!=' ': 
        # print(positions['00']+" wins")
        if positions['00']=='x':
            print(f'{player1} wins!')
        else:
            print(f'{player2} wins!')
        exit()
    if positions['10'] == positions['11'] == positions['12'] and positions['10']!=' ': 
        # print(positions['10']+" wins")
        if positions['10']=='x':
            print(f'{player1} wins!')
        else:
            print(f'{player2} wins!')
        exit()
    if positions['20'] == positions['21'] == positions['22'] and positions['20']!=' ': 
        # print(positions['20']+" wins")
        if positions['20']=='x':
            print(f'{player1} wins!')
        else:
            print(f'{player2} wins!')
        exit()
    if positions['00'] == positions['10'] == positions['20'] and positions['00']!=' ': 
        # print(positions['00']+" wins")
        if positions['00']=='x':
            print(f'{player1} wins!')
        else:
            print(f'{player2} wins!')
        exit()
    if positions['01'] == positions['11'] == positions['21'] and positions['01']!=' ': 
        # print(positions['01']+" wins")
        if positions['01']=='x':
            print(f'{player1} wins!')
        else:
            print(f'{player2} wins!')
        exit()
    if positions['02'] == positions['12'] == positions['22'] and positions['02']!=' ': 
        # print(positions['02']+" wins")
        if positions['02']=='x':
            print(f'{player1} wins!')
        else:
            print(f'{player2} wins!')
        exit()
    if positions['00'] == positions['11'] == positions['22'] and positions['00']!=' ': 
        # print(positions['00']+" wins")
        if positions['00']=='x':
            print(f'{player1} wins!')
        else:
            print(f'{player2} wins!')
        exit()
    if positions['02'] == positions['11'] == positions['20'] and positions['02']!=' ': 
        # print(positions['02']+" wins")
        if positions['02']=='x':
            print(f'{player1} wins!')
        else:
            print(f'{player2} wins!')
        exit()
    
def vacant_checker(pos):
    if pos == 1 and positions['00']!=' ': return False
    elif pos == 2 and positions['01']!=' ': return False
    elif pos == 3 and positions['02']!=' ': return False
    elif pos == 4 and positions['10']!=' ': return False
    elif pos == 5 and positions['11']!=' ': return False
    elif pos == 6 and positions['12']!=' ': return False
    elif pos == 7 and positions['20']!=' ': return False
    elif pos == 8 and positions['21']!=' ': return False
    elif pos == 9 and positions['22']!=' ': return False
    else: return True
import os
winner='NOT DECIDED'
print('Welcome to TicTacToe')
player1=input('Enter player1 name: ') or 'player1'
player2=input('Enter player2 name: ') or 'player2'
x1=0
x2=0
while winner=='NOT DECIDED':
    os.system('cls')
    printer()
    x1=0
    x2=0
    while x1 not in range(1,11):
        x1=int(input(f'Go {player1}: '))
        if(x1 in range(1,11)): break
        if vacant_checker(x1)==False: 
            print('Cell already occupied. Try again!')
            x2=0
            continue
        print('Sorry that postion was out of the table. Try again!')
    x_engine(x1)
    os.system('cls')
    printer()
    checking_engine()
    while x2 not in range(1,11):
        x2=int(input(f'Go {player2}: '))
        if vacant_checker(x2)==False: 
            print('Cell already occupied. Try again!')
            x2=0
            continue
        if(x2 in range(1,11)): break
        print('Sorry that postion was out of the table. Try again!')
    o_engine(x2)
    os.system('cls')
    printer()
    checking_engine()