from random import *
import math
from tkinter import *
import msvcrt
import os
import sys
import time
from colorama import *

wall = Fore.WHITE + '#'
a = Fore.BLUE + '.'
hero = Fore.YELLOW + '@'
enemy = Fore.GREEN + 'a'
hp = 15
at = 5
status = Fore.WHITE + "HP: {};AT: {}".format(hp, at)
ep = 11
c = 10
ht = 15
wt = 25
aliens = []
for i in range(c):
    new = {'x': randrange(wt),'y':randrange(ht), 'hp': randrange(ep)}
    aliens.append(new)
h_x = randrange(wt)
h_y = randrange(ht)
init()
field = [[randrange(10) for i in range(wt)]for i in range(ht)]

def GenerateField():
    for i in range(ht):
        for j in range(wt):
            if field[i][j] > 8:
                field[i][j] = wall
            else:
                field[i][j] = a

def DrawField():
    os.system("cls")
    for i in range(ht):
        for j in range(wt):
            print(field[i][j],end='')
        print()
    print(status)
GenerateField()
DrawField()

def Place():
    field[h_y][h_x] = hero
    DrawField()
    
def Move():
    global aliens
    global h_x
    global h_y
    while True:
        key = msvcrt.getch()
        if key == b'w':
            if field[h_y-1][h_x] != wall and field[h_y-1][h_x] != enemy:
                field[h_y][h_x] = a
                h_y -= 1
                field[h_y][h_x] = hero
            else:
                h_y += 0
        elif key == b'a':
            if field[h_y][h_x-1] != wall and field[h_y][h_x-1] != enemy:
                field[h_y][h_x] = a
                h_x -= 1
                field[h_y][h_x] = hero    
            else:
                h_x += 0
        elif key == b's':
            if field[h_y+1][h_x] != wall and field[h_y+1][h_x] != enemy:
                field[h_y][h_x] = a
                h_y += 1
                field[h_y][h_x] = hero  
            else:
               h_y += 0
        elif key == b'd':
            if field[h_y][h_x+1] != wall and field[h_y][h_x+1] != enemy:
                field[h_y][h_x] = a
                h_x += 1
                field[h_y][h_x] = hero               
            else:
                h_x += 0
        
                
def Enemy():
    for alien in aliens:
        x = alien['x']
        y = alien['y']
        if field[y][x] == a:
            field[y][x] = enemy
        DrawField()

def moveTo():
    global aliens
    for alien in aliens:
        if alien.get('hp') == None:
            continue
        else:
            x = alien['x']
            y = alien['y']
        if x < h_x:
            if field[y][x+1] == a :
                field[y][x] = a
                x += 1
                alien['x'] += 1
                field[alien['y']][alien['x']] = enemy
        else:
            if field[y][x-1] == a:
                field[y][x] = a
                x -= 1
                alien['x'] -= 1
                field[alien['y']][alien['x']] = enemy
        if y < h_y:
            if field[y+1][x] == a:
                field[y][x] = a
                y += 1
                alien['y'] += 1
                field[alien['y']][alien['x']] = enemy
        else:
            if field[y-1][x] == a:
                field[y][x] = a
                y -= 1
                alien['y'] -= 1
                field[alien['y']][alien['x']] = enemy
def Ai(): 
    moveTo()

def Fight(x, y):
    global hp
    global at
    global aliens
    global status
    for alien in aliens:
        if alien.get('x') == x and alien.get('y') == y:
            del alien['hp']
            del alien['x']
            del alien['y']

Place()
Move()


