#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 18:58:36 2017

@author: adamraveret
"""
###############################################################################
# STEP 1
###############################################################################

from random import randint
from random import seed
import pandas as pd
import numpy as np

seed(1)

sit = []
sit_prior = []
result = []
turn = []

board = [['0','1','2'],['3','4','5'],['6','7','8']]
    
win_combos = [[0,1,2],[3,4,5],[6,7,8],\
              [0,3,6],[1,4,7],[2,5,8],\
              [0,4,8],[2,4,6]]

selected = []
x_selected = []
o_selected = []

x = True
win = False
turn_count = 0

print(board[0])
print(board[1])
print(board[2])
print()

while (win == False)&(len(selected)<9):
    if x == True:
        x_num = randint(0,8)
        while x_num in selected:
                x_num = randint(0,8)
        board[int(x_num/3)][int(x_num%3)] = 'X'
        selected_prior = selected.copy()
        selected.append(x_num)
        x_selected.append(x_num)
        for combo in win_combos:
            count = 0
            for item in combo:
                if item in x_selected:
                    count += 1
            if count == 3:
                win = True
        x = False
        turn.append(turn_count)
        turn_count += 1
        sit_prior.append(str(selected_prior.copy()))
        sit.append(str(selected.copy()))
        result.append('x') 
        
        print(board[0])
        print(board[1])
        print(board[2])
        print()
        
    else:
        o_num = randint(0,8)
        while o_num in selected:
            o_num = randint(0,8)
        board[int(o_num/3)][int(o_num%3)] = 'O'
        selected_prior = selected.copy()
        selected.append(o_num)
        o_selected.append(o_num)
        for combo in win_combos:
            count = 0
            for item in combo:
                if item in o_selected:
                    count += 1
            if count == 3:
                win = True
        x = True
        turn.append(turn_count)
        turn_count += 1
        sit_prior.append(str(selected_prior.copy()))
        sit.append(str(selected.copy()))
        result.append('o')
        
        print(board[0])
        print(board[1])
        print(board[2])
        print()
        
game_data = pd.DataFrame(0.0,columns=['result','sit_prior','sit','turn'],index=range(len(result)))

game_data['result'] = result
game_data['sit_prior'] = sit_prior
game_data['sit'] = sit
game_data['turn'] = turn     
        
if win == True:
    if turn_count%2 == 0:
        game_data['result'] = np.where(game_data['result']=='o',1,0)
    else:
        game_data['result'] = np.where(game_data['result']=='x',1,0)
else:
    game_data['result'] = 0.5

print(game_data[['result','sit','turn']])

###############################################################################
# STEP 2
###############################################################################
    
rand_data = pd.DataFrame(0.0,columns=['result','sit','turn'],index=range(0))

for build_count in range(1000):    
    sit = []
    sit_prior = []
    result = []
    turn = []
    
    board = [['0','1','2'],['3','4','5'],['6','7','8']]
        
    win_combos = [[0,1,2],[3,4,5],[6,7,8],\
                  [0,3,6],[1,4,7],[2,5,8],\
                  [0,4,8],[2,4,6]]
    
    selected = []
    x_selected = []
    o_selected = []
    
    x = True
    win = False
    turn_count = 0
    
    while (win == False)&(len(selected)<9):
        if x == True:
            x_num = randint(0,8)
            while x_num in selected:
                    x_num = randint(0,8)
            board[int(x_num/3)][int(x_num%3)] = 'X'
            selected_prior = selected.copy()
            selected.append(x_num)
            x_selected.append(x_num)
            for combo in win_combos:
                count = 0
                for item in combo:
                    if item in x_selected:
                        count += 1
                if count == 3:
                    win = True
            x = False
            turn.append(turn_count)
            turn_count += 1
            sit_prior.append(str(selected_prior.copy()))
            sit.append(str(selected.copy()))
            result.append('x') 
            
#            print(board[0])
#            print(board[1])
#            print(board[2])
            
        else:
            o_num = randint(0,8)
            while o_num in selected:
                o_num = randint(0,8)
            board[int(o_num/3)][int(o_num%3)] = 'O'
            selected_prior = selected.copy()
            selected.append(o_num)
            o_selected.append(o_num)
            for combo in win_combos:
                count = 0
                for item in combo:
                    if item in o_selected:
                        count += 1
                if count == 3:
                    win = True
            x = True
            turn.append(turn_count)
            turn_count += 1
            sit_prior.append(str(selected_prior.copy()))
            sit.append(str(selected.copy()))
            result.append('o')
            
#            print(board[0])
#            print(board[1])
#            print(board[2])
            
    game_data = pd.DataFrame(0.0,columns=['result','sit_prior','sit','turn'],index=range(len(result)))

    game_data['result'] = result
    game_data['sit_prior'] = sit_prior
    game_data['sit'] = sit
    game_data['turn'] = turn     
            
    if win == True:
        if turn_count%2 == 0:
            game_data['result'] = np.where(game_data['result']=='o',1,0)
        else:
            game_data['result'] = np.where(game_data['result']=='x',1,0)
    else:
        game_data['result'] = 0.5

    rand_data = rand_data.append(game_data.copy())

rand_data = rand_data.reset_index(drop=True)
result_1000 = rand_data.copy()

print(result_1000[(result_1000['turn']==0)&(result_1000['sit_prior']=='[]')].groupby('sit')['result'].mean().sort_values(ascending=False))
print(result_1000[(result_1000['turn']==0)].groupby('result')['result'].count())

###############################################################################
# STEP 3
###############################################################################

result_2000 = pd.DataFrame(0.0,columns=['result','sit_prior','sit','turn'],index=range(0))

for build_count in range(1000):    
    sit = []
    sit_prior = []
    result = []
    turn = []
    
    board = [['0','1','2'],['3','4','5'],['6','7','8']]
        
    win_combos = [[0,1,2],[3,4,5],[6,7,8],\
                  [0,3,6],[1,4,7],[2,5,8],\
                  [0,4,8],[2,4,6]]
    
    selected = []
    x_selected = []
    o_selected = []
    
    x = True
    win = False
    turn_count = 0
    
    while (win == False)&(len(selected)<9):
        data = rand_data[(rand_data['turn']==turn_count)&(rand_data['sit_prior']==str(selected))].copy()
        if x == True:
            if len(data) != 0:
                if data.groupby('sit')['result'].mean().sort_values(ascending=False)[0] >= 0.4:
                    x_num = int(data.groupby('sit')['result'].mean().sort_values(ascending=False).index[0].split('[')[1].split(']')[0].split(', ')[-1])
                else:
                    x_num = randint(0,8)
                    while x_num in selected:
                        x_num = randint(0,8)
            else:
                x_num = randint(0,8)
                while x_num in selected:
                    x_num = randint(0,8)
            board[int(x_num/3)][int(x_num%3)] = 'X'
            selected_prior = selected.copy()
            selected.append(x_num)
            x_selected.append(x_num)
            for combo in win_combos:
                count = 0
                for item in combo:
                    if item in x_selected:
                        count += 1
                if count == 3:
                    win = True
            x = False
            turn.append(turn_count)
            turn_count += 1
            sit_prior.append(str(selected_prior.copy()))
            sit.append(str(selected.copy()))
            result.append('x')
        else:
            if len(data) != 0:
                if data.groupby('sit')['result'].mean().sort_values(ascending=False)[0] >= 0.4:
                    o_num = int(data.groupby('sit')['result'].mean().sort_values(ascending=False).index[0].split('[')[1].split(']')[0].split(', ')[-1])
                else:
                    o_num = randint(0,8)
                    while o_num in selected:
                        o_num = randint(0,8)
            else:
                o_num = randint(0,8)
                while o_num in selected:
                    o_num = randint(0,8)
            board[int(o_num/3)][int(o_num%3)] = 'O'
            selected_prior = selected.copy()
            selected.append(o_num)
            o_selected.append(o_num)
            for combo in win_combos:
                count = 0
                for item in combo:
                    if item in o_selected:
                        count += 1
                if count == 3:
                    win = True
            x = True
            turn.append(turn_count)
            turn_count += 1
            sit_prior.append(str(selected_prior.copy()))
            sit.append(str(selected.copy()))
            result.append('o')
            
    game_data = pd.DataFrame(0.0,columns=['result','sit_prior','sit','turn'],index=range(len(result)))

    game_data['result'] = result
    game_data['sit_prior'] = sit_prior
    game_data['sit'] = sit
    game_data['turn'] = turn     
            
    if win == True:
        if turn_count%2 == 0:
            game_data['result'] = np.where(game_data['result']=='o',1,0)
        else:
            game_data['result'] = np.where(game_data['result']=='x',1,0)
    else:
        game_data['result'] = 0.5

    result_2000 = result_2000.append(game_data.copy()) 
    rand_data = rand_data.append(game_data.copy())

print(result_2000[(result_2000['turn']==0)&(result_2000['sit_prior']=='[]')].groupby('sit')['result'].mean().sort_values(ascending=False))
print(result_2000[(result_2000['turn']==0)].groupby('result')['result'].count())

print(rand_data[(rand_data['turn']==0)&(rand_data['sit_prior']=='[]')].groupby('sit')['result'].mean().sort_values(ascending=False))
print(rand_data[(rand_data['turn']==0)].groupby('result')['result'].count())

###############################################################################
# STEP 4
###############################################################################    
    
result_3000 = pd.DataFrame(0.0,columns=['result','sit_prior','sit','turn'],index=range(0))

for build_count in range(1000):    
    sit = []
    sit_prior = []
    result = []
    turn = []
    
    board = [['0','1','2'],['3','4','5'],['6','7','8']]
        
    win_combos = [[0,1,2],[3,4,5],[6,7,8],\
                  [0,3,6],[1,4,7],[2,5,8],\
                  [0,4,8],[2,4,6]]
    
    selected = []
    x_selected = []
    o_selected = []
    
    x = True
    win = False
    turn_count = 0
    
    while (win == False)&(len(selected)<9):
        data = rand_data[(rand_data['turn']==turn_count)&(rand_data['sit_prior']==str(selected))].copy()
        if x == True:
            if len(data) != 0:
                if data.groupby('sit')['result'].mean().sort_values(ascending=False)[0] >= 0.4:
                    x_num = int(data.groupby('sit')['result'].mean().sort_values(ascending=False).index[0].split('[')[1].split(']')[0].split(', ')[-1])
                else:
                    x_num = randint(0,8)
                    while x_num in selected:
                        x_num = randint(0,8)
            else:
                x_num = randint(0,8)
                while x_num in selected:
                    x_num = randint(0,8)
            board[int(x_num/3)][int(x_num%3)] = 'X'
            selected_prior = selected.copy()
            selected.append(x_num)
            x_selected.append(x_num)
            for combo in win_combos:
                count = 0
                for item in combo:
                    if item in x_selected:
                        count += 1
                if count == 3:
                    win = True
            x = False
            turn.append(turn_count)
            turn_count += 1
            sit_prior.append(str(selected_prior.copy()))
            sit.append(str(selected.copy()))
            result.append('x')
        else:
            if len(data) != 0:
                if data.groupby('sit')['result'].mean().sort_values(ascending=False)[0] >= 0.4:
                    o_num = int(data.groupby('sit')['result'].mean().sort_values(ascending=False).index[0].split('[')[1].split(']')[0].split(', ')[-1])
                else:
                    o_num = randint(0,8)
                    while o_num in selected:
                        o_num = randint(0,8)
            else:
                o_num = randint(0,8)
                while o_num in selected:
                    o_num = randint(0,8)
            board[int(o_num/3)][int(o_num%3)] = 'O'
            selected_prior = selected.copy()
            selected.append(o_num)
            o_selected.append(o_num)
            for combo in win_combos:
                count = 0
                for item in combo:
                    if item in o_selected:
                        count += 1
                if count == 3:
                    win = True
            x = True
            turn.append(turn_count)
            turn_count += 1
            sit_prior.append(str(selected_prior.copy()))
            sit.append(str(selected.copy()))
            result.append('o')
            
    game_data = pd.DataFrame(0.0,columns=['result','sit_prior','sit','turn'],index=range(len(result)))

    game_data['result'] = result
    game_data['sit_prior'] = sit_prior
    game_data['sit'] = sit
    game_data['turn'] = turn     
            
    if win == True:
        if turn_count%2 == 0:
            game_data['result'] = np.where(game_data['result']=='o',1,0)
        else:
            game_data['result'] = np.where(game_data['result']=='x',1,0)
    else:
        game_data['result'] = 0.5

    result_3000 = result_3000.append(game_data.copy()) 
    rand_data = rand_data.append(game_data.copy())

print(result_3000[(result_3000['turn']==0)&(result_3000['sit_prior']=='[]')].groupby('sit')['result'].mean().sort_values(ascending=False))
print(result_3000[(result_3000['turn']==0)].groupby('result')['result'].count())

print(rand_data[(rand_data['turn']==0)&(rand_data['sit_prior']=='[]')].groupby('sit')['result'].mean().sort_values(ascending=False))
print(rand_data[(rand_data['turn']==0)].groupby('result')['result'].count())
    