'''
Created on Jan 26, 2014

@author: anuvrat
'''

class QuickFind(object):
    def __init__(self, size, debug = False):
        self.group_count = self.size = size
        self.group = [i for i in range(size)]
        self.debug = debug
        
    def union(self, child, parent):
        if self.group[child] == self.group[parent]: return
        
        self.group = [self.group[parent] if self.group[idx] == self.group[child] else self.group[idx] for idx in range(self.size)]
        self.group_count = self.group_count - 1
        if self.debug: print(self.group_count, self.group)
        
    def find(self, element):
        return self.group[element]
    
    def get_count_of_groups(self):
        return self.group_count
    
    def connected(self, element_a, element_b):
        return self.group[element_a] == self.group[element_b]
    
    def get_components(self):
        components = {}
        for i in range(self.size):
            if self.group[i] in components: components[self.group[i]].append(i)
            else: components[self.group[i]] = [i]
        return components

class Board(object):
    def __init__(self, x, y, grid):
        self.x, self.y, self.grid = x, y, grid
        self.__find_components()
    
    def __next_neighbour(self, a, b):
        for x, y in [(a + i, b + j) for i in (0, 1) for j in (0, 1) if not(i == j == 0) and not (i == j == 1) and a + i < self.x and b + j < self.y]:
            yield (x, y)

    def encode_position(self, a, b):
        return a * self.y + b
    
    def decode_position(self, pos):
        return (int(pos / self.y), int(pos % self.y))
    
    def __find_components(self):
        self.qf = QuickFind(self.x * self.y, False)
        for x_idx, y_idx in ((a, b) for a in range(self.x) for b in range(self.y) if not self.grid[a][b] == '-' ):
            for neighbour_x, neighbour_y in self.__next_neighbour(x_idx, y_idx):
                if self.grid[x_idx][y_idx] == self.grid[neighbour_x][neighbour_y]:
                    self.qf.union(self.encode_position(neighbour_x, neighbour_y), self.encode_position(x_idx, y_idx))
    
    def get_components(self):
        components = []
        for _, sites in self.qf.get_components().items():
            if len(sites) == 1:
                x, y = self.decode_position(sites[0])
                if self.grid[x][y] == '-': continue
            components.append(sites)
        return sorted(components, key = len, reverse = True)
    
    def remove_component(self, site_ids):
        grid_copy = [row[:] for row in self.grid]
        for x_idx, y_idx in map(self.decode_position, site_ids): grid_copy[x_idx][y_idx] = '-'

        # If a column is all empty then shift all the columns to the left        
        for col_idx in (idx for idx in range(self.y - 1) if [row[idx] for row in grid_copy] == ['-'] * self.x):
            for x_idx, y_idx in ((a, b) for a in range(self.x) for b in range(col_idx, self.y - 1)):
                grid_copy[x_idx][y_idx] = grid_copy[x_idx][y_idx + 1]
            for x_idx in range(self.x): grid_copy[x_idx][self.y - 1] = '-'
        
        # If a site is empty then shift all elements above it down
        for x_idx, y_idx in ((a, b) for a in range(1, self.x) for b in range(self.y) if grid_copy[a][b] == '-'):
            for temp_x_idx in range(x_idx, 0, -1):
                grid_copy[temp_x_idx][y_idx] = grid_copy[temp_x_idx - 1][y_idx]
            grid_copy[0][y_idx] = '-'

        return grid_copy
    
    def __repr__(self):
        return '\n' + '\n'.join([''.join(row[:]) for row in self.grid])

def recursive_next_move(x, y, color, grid):
    board = Board(x, y, grid)
    sum_units = 0
    min_component_size, min_component_sites = x*y + 1, []
    for sites in board.get_components():
        if len(sites) < 2:
            sum_units = sum_units + len(sites)
            continue
        grid_copy = board.remove_component(sites)
        copy_min_component_size, _, _ = recursive_next_move(x, y, color, grid_copy)
        if copy_min_component_size == 0: return copy_min_component_size, sites, board.decode_position(sites[0])
        if copy_min_component_size < min_component_size:
            min_component_size = copy_min_component_size
            min_component_sites = sites
    if len(min_component_sites) == 0: return sum_units, [], ()
    else: return min_component_size, min_component_sites, board.decode_position(min_component_sites[0])
    
def nextMove(x, y, color, grid):
    _, _, site = recursive_next_move(x, y, color, grid)
    if site == (): return
    else: 
        x_idx, y_idx = site
        print(x_idx, y_idx)
    
if __name__ == '__main__':
    x,y,k = [ int(i) for i in input().strip().split() ] 
    grid = [[i for i in str(input().strip())] for _ in range(x)] 
    nextMove(x, y, k, grid)
