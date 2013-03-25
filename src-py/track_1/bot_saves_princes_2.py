'''
Created on Mar 26, 2013

@author: anuvrat
'''

def main():
    M = int(input())
    bot = list(map(int, input().strip().split()))
    for i in range(0, M):
        col = input().strip().find('p')
        if col != -1: 
            princess = [i, col]
            break
    
    diff = [p - b for p, b in zip(princess, bot)]
    
    if diff[1] == 0:
        print('UP' if diff[0] < 0 else 'DOWN')
    else:
        print('LEFT' if diff[1] < 0 else 'RIGHT')
        
main()