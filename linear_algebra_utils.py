#!/usr/bin/python3

from sympy import pprint
import sys
from sympy import *
import json

args = sys.argv

commands = {
    'help': [
        "help",
        "h"
    ],
    'create_stochastic': [
        "create_stochastic",
        "cstoch"
    ]
}

def main():
    while(true):
        args = input("Please enter a command: ").split(' ')
        command = args[0].lower()
        print("")
        if(command == "help"):
            runHelp(args)
        elif(command == "create_stochastic" or command == "cstoch"):
            create_stochastic(args[1])

def create_stochastic(filename):
    with open(filename) as jsonfile:
        config = json.load(jsonfile)

    #Unpackage config
    dice_size = config["dice_size"]
    board_length = config["board_length"]
    paths = config["paths"]
    chance = Rational(1)/dice_size
    board = zeros(board_length,board_length)

    for col in range(board_length):
        for roll in range(1,dice_size + 1):
            #repetition at the end
            current_row = min(col + roll, board_length - 1)

            #if path to follow
            if(str(col) in paths):
                for row in range(board_length):
                    if(paths[str(col)] == row):
                        board[row,col] = 1
                    else:
                        board[row,col] = 0
            elif(str(current_row) in paths):
                board[current_row,col] = 0
                board[paths[str(current_row)],col] += chance
            else:
                board[current_row,col] += chance
    pprint(board)
    return board

a = create_stochastic(args[1])
