#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 18:58:36 2017

@author: adamraveret
"""
###############################################################################
# SET UP
###############################################################################

from random import randint
from random import seed
import pandas as pd
import numpy as np

seed(1)

all_data = pd.DataFrame(0.0,columns=['result','sit','turn'],index=range(0))
sample_data = pd.DataFrame(0.0,columns=['result','sit','turn'],index=range(0))

def print_board(board):
    print(board[0])
    print(board[1])
    print(board[2])
    print()

def check_win(win_combos, x_selected, win):
    for combo in win_combos:
        count = 0
        for item in combo:
            if item in x_selected:
                count += 1
        if count == 3:
            win = True 
    return win
            
def turn_func(x_num, selected, turn_count, board, result, x_selected, turn, sit_prior, sit, win_combos, win):
    while x_num in selected:
        x_num = randint(0,8)
    if turn_count%2 == 0:
        board[int(x_num/3)][int(x_num%3)] = 'X'
        result.append('x') 
    else:
        board[int(x_num/3)][int(x_num%3)] = 'O'
        result.append('o')
    selected_prior = selected.copy()
    selected.append(x_num)
    x_selected.append(x_num)
    turn.append(turn_count)
    turn_count += 1
    sit_prior.append(str(selected_prior.copy()))
    sit.append(str(selected.copy()))
    win = check_win(win_combos, x_selected, win)
    return selected, turn_count, board, result, x_selected, turn, sit_prior, sit, win

def learn_func(data, selected):
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
    return x_num
    
def tic_tac_toe(all_data, sample_data, random):    
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
    
    win = False
    turn_count = 0
    
#    print_board(board)
    if random == 'random': 
        while (win == False)&(len(selected)<9):
            if turn_count%2 == 0:
                x_num = randint(0,8)
                selected, turn_count, board, result, x_selected, turn, sit_prior, sit, win = \
                turn_func(x_num, selected, turn_count, board, result, x_selected, turn, sit_prior, sit, win_combos, win)
#               print_board(board)
            else:
                o_num = randint(0,8)
                selected, turn_count, board, result, o_selected, turn, sit_prior, sit, win = \
                turn_func(o_num, selected, turn_count, board, result, o_selected, turn, sit_prior, sit, win_combos, win)
#               print_board(board)
    elif random == 'learn':
        while (win == False)&(len(selected)<9):
            data = all_data[(all_data['turn']==turn_count)&(all_data['sit_prior']==str(selected))].copy()
            if turn_count%2 == 0:
                x_num = learn_func(data, selected)
                selected, turn_count, board, result, x_selected, turn, sit_prior, sit, win = \
                turn_func(x_num, selected, turn_count, board, result, x_selected, turn, sit_prior, sit, win_combos, win)
#               print_board(board)
            else:
                o_num = learn_func(data, selected)
                selected, turn_count, board, result, o_selected, turn, sit_prior, sit, win = \
                turn_func(o_num, selected, turn_count, board, result, o_selected, turn, sit_prior, sit, win_combos, win)
#               print_board(board)
            
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
    
    all_data = all_data.append(game_data.copy())
    sample_data = sample_data.append(game_data.copy())
    return all_data, sample_data
    
def vis_data(all_data):
    print()
    print(all_data[(all_data['turn']==0)&(all_data['sit_prior']=='[]')].groupby('sit')['result'].mean().sort_values(ascending=False))
    print()
    print(all_data[(all_data['turn']==0)].groupby('result')['result'].count())

###############################################################################
# STEP 1
###############################################################################    
    
all_data, sample_data = tic_tac_toe(all_data, sample_data, 'random')
all_data
    
###############################################################################
# STEP 2
###############################################################################
    
for item in range(999):
    all_data, sample_data = tic_tac_toe(all_data, sample_data, 'random')

vis_data(all_data)  
    
###############################################################################
# STEP 3
###############################################################################

sample_data = pd.DataFrame(0.0,columns=['result','sit','turn'],index=range(0))

for item in range(1000):
    all_data, sample_data = tic_tac_toe(all_data, sample_data, 'learn')

vis_data(all_data)
vis_data(sample_data) 

###############################################################################
# STEP 4
###############################################################################    
    
sample_data = pd.DataFrame(0.0,columns=['result','sit','turn'],index=range(0))

for item in range(1000):
    all_data, sample_data = tic_tac_toe(all_data, sample_data, 'learn')

vis_data(all_data)
vis_data(sample_data)

###############################################################################
# STEP 5
###############################################################################    
    
sample_data = pd.DataFrame(0.0,columns=['result','sit','turn'],index=range(0))

for item in range(1000):
    all_data, sample_data = tic_tac_toe(all_data, sample_data, 'learn')

vis_data(all_data)
vis_data(sample_data)