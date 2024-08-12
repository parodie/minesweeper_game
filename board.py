import random
import sys

class mines_board:
    
    def __init__(self, dim, num_mines):
        self.dim = dim
        self.num_mines = num_mines
        self.values = [[0 for i in range(self.dim)] for j in range(self.dim)]
        self.mines_values =  [[' ' for i in range(self.dim)] for j in range(self.dim)]    
        self.visited = []   
        self.count = 0
        self.play_state = True

    def print_board(self):
        print('\n\tMINESWEEPER\n')
        
        first = '     '
        line = '   '
        for i in range(self.dim):
            first = first + str(i+1) + '     '
            line = line +'______'
        line += '_'
        print(first)
        
        for i in range(self.dim):
            column = ''
            print(line)
            column = str(i + 1)
            for j in range(self.dim):
                column = column + '  |  ' + str(self.mines_values[i][j])
            column = column + '  |'
            print(column)
          
    def implant_mines(self):
        count = 0
        while count < self.num_mines:
            index = random.randint(0, self.dim * self.dim - 1)
            row = index // self.dim
            column = index % self.dim
            
            if self.values[row][column] != '*':
                count += 1
                self.values[row][column] = '*'
                
    def get_surroundings(self):
        for row in range(self.dim):
            for col in range(self.dim):
                
                if self.values[row][col] == '*':
                    continue
              
                """horizontal checks"""
                if col > 0 and self.values[row][col-1] == '*':
                    self.values[row][col] += 1
                
                if col < self.dim-1 and self.values[row][col+1] == '*':
                    self.values[row][col] += 1
                    
                """vertical checks"""
                if row > 0 and self.values[row-1][col] == '*':
                    self.values[row][col] += 1   
                
                if row < self.dim-1 and self.values[row+1][col] == '*':
                    self.values[row][col] += 1 
                    
                """diagonal checks"""
                if row > 0 and col > 0 and self.values[row-1][col-1] == '*':     
                    self.values[row][col] += 1
                    
                if row < self.dim-1 and col < self.dim-1 and self.values[row+1][col+1] == '*':     
                    self.values[row][col] += 1
                
                if row < self.dim-1 and col > 0 and self.values[row+1][col-1] == '*':
                    self.values[row][col] += 1
                
                if row > 0 and col < self.dim-1 and self.values[row-1][col+1] == '*':
                    self.values[row][col] += 1
                
                   
                
    def play(self, row, col):
        #step 1: create the board & implant the mines
        #step 2: show the user the board & ask for row, col inputs
        #step 3: victory(dig mines until next to a boomb and repeat until victory or loss :() or loss(location is a bomb)
        
        if self.values[row][col] == '*':
            for i in range(self.dim):
                for j in range(self.dim):
                    self.mines_values[i][j] = self.values[i][j]
            self.print_board()
            print('A mine !! You lost.')
            self.play_state = False
            
        else:
            self.neighbour(row,col)
            self.ckeck_winner()
            self.print_board()  
            print('no mine!')
            
            
            
    def neighbour(self,row,col):
        
        if [row,col] not in self.visited:
            if self.values[row][col] == 0 :
                self.mines_values[row][col] = self.values[row][col]
                self.visited.append([row,col])
                
                if row > 0:
                    #top
                    self.neighbour(row-1,col)
                if col > 0:
                    #left
                    self.neighbour(row,col-1)
                if row < self.dim-1:
                    #bottom
                    self.neighbour(row+1,col)
                if col < self.dim-1:
                    #right
                    self.neighbour(row,col+1)
                if row > 0 and col > 0:
                    #top left
                    self.neighbour(row-1, col-1)
                if row > 0 and col < self.dim-1:
                    #top right
                    self.neighbour(row-1, col+1)
                if row < self.dim-1 and col > 0:
                    #bottom left
                    self.neighbour(row+1, col-1)
                if row < self.dim-1 and col < self.dim-1:
                    #bottom right
                    self.neighbour(row+1, col+1)  
                    
            if self.values[row][col] != 0:
                self.mines_values[row][col] = self.values[row][col]
                self.visited.append([row,col])
                
  
    def ckeck_winner(self):
        up = self.dim*self.dim - self.num_mines
        for i in range(self.dim):
            for j in range(self.dim):
                if self.mines_values[i][j] != ' ':
                    self.count +=1
                    
        if self.count == up:
            print('You win!')
            self.mines_values == [row[:] for row in self.values]
            self.print_board()  
            self.play_state = False
                
                    
                    
                    

def instructions():
    print('\nInstructions: \n - Column & row coordinates start from 1! \n - The inputs you provide should be separated by a space!')
    

if __name__ == '__main__':
    M = mines_board(10,15)
    M.implant_mines()
    M.get_surroundings()
    M.print_board()
    
    state = True
    
    instructions()
    
   
    while M.play_state:
        #handling input
        stateE = True
        while stateE :
            try:
                row, col = input('\nEnter row number followed by space and column number: ').split(' ')
                r = int(row)-1
                c = int(col)-1
                
                while state:
                    if [r,c] in M.visited :
                        row, col = input(f'Coordinates [{r},{c}] already checked! Retry: ').split(" ")
                        r = int(row)-1
                        c = int(col)-1
                        
                    elif r > M.dim - 1 or c > M.dim - 1:
                        row, col = input(f'false row or column coordinates, the dimension of the board is {M.dim}x{M.dim}. Retry :').split(" ")
                        r = int(row)-1
                        c = int(col)-1 
                        
                    else :
                        state = False
                print(f'row: {r+1}, column: {c+1}')
                stateE = False
                
            except ValueError:
                print('Wrong input! \n')
                instructions()
            
        M.play(r,c)
        
        
    
        
        
            
            
    

            
