'''
Created on Mar 25, 2013

@author: anuvrat
'''

def print_path(direction, count):
    for _ in range(count): print(direction)

def main():
    M = int(input())
    for i in range(0, M):
        row = input().strip()
        if row.find('m') != -1: bot = [i, row.find('m')]
        if row.find('p') != -1: princess = [i, row.find('p')]
    
    diff = [p - b for p, b in zip(princess, bot)]
    direction = ['DOWN', 'RIGHT']
    
    if diff[0] < 0:
        direction[0] = 'UP'
        diff[0] *= -1
    if diff[1] < 0:
        direction[1] = 'LEFT'
        diff[1] *= -1
    
    print_path(direction[0], diff[0])
    print_path(direction[1], diff[1])
    
main()