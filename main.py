"""
1. Players give input over the command line by giving the position as numbers (could also be col, row)
2. After every input the board is drawn in the console
3. the program checks if 3 in a line have been achieved
4. if not, continue with the next player
5. if yes, finish game and anounce winner
6. if all spaces have been filled but there is no winner, say its a draw 

"""

# dictionary which saves the game state, could also be done in an array/list
# just some sample data to test, can be cleaned
game_state = {(0,0): "o", (0,1): "x",  (0,2): "x",
              (1,0): "x", (1,1): " ", (1,2): "x",
              (2,0): "o", (2,1): "x",  (2,2): "o"}



def draw_game_dict():
    print(f'''
 {game_state[(0,0)]} | {game_state[(0,1)]} | {game_state[(0,2)]} 
-----------
 {game_state[(1,0)]} | {game_state[(1,1)]} | {game_state[(1,2)]}
-----------
 {game_state[(2,0)]} | {game_state[(2,1)]} | {game_state[(2,2)]}

          ''')



#draw_game_dict()



def clear_game_dict():
    global game_state 
    game_state = dict.fromkeys(game_state," ")
    # or:
    # game_state = {key: " " for key in game_state}
    draw_game_dict()

clear_game_dict()

def set_position(row,col,Player):
    global game_state
    if Player == 1:
        game_state[(row,col)] = "o"
        print(game_state)
    if Player == 2:
        game_state[(row,col)] = "x"
        print(game_state)
    

# checks if the Player has won
def check_win_condition():
    # rows equal
    for i in range(3):
        if game_state[(i,0)]!=" " and game_state[(i,0)] == game_state[(i,1)] and game_state[(i,0)] == game_state[(i,2)]:
            return True
    
    ## cloumns equal
    for i in range(3):
        if game_state[(0,i)]!=" " and game_state[(0,i)] == game_state[(1,i)] and game_state[(0,i)] == game_state[(2,i)]:
            return True
        
    # diagonal down
    if game_state[(0,0)]!=" " and game_state[(0,0)] == game_state[(1,1)] and game_state[(0,0)] == game_state[(2,2)]:
        return True
    
    # diagonal up
    if game_state[(2,0)]!=" " and game_state[(2,0)] == game_state[(1,1)] and game_state[(2,0)] == game_state[(0,2)]:
        return True
    
    # nobody has won yet
    return False
    

game_running = True
Player = 1
while game_running:
    row = int(input(f"Player {Player} row: "))
    col = int(input(f"Player {Player} col: "))
    set_position(row,col,Player)
    draw_game_dict()
    result = check_win_condition()
    if result:
        print(f"Player {Player} has won!!! Congratiulations!")
        game_running = False
    if Player == 1:
        Player = 2
        continue
    if Player == 2:
        Player = 1
        continue  










    """
Do everything with lists, just to see whats the better data type
game_stat = [["o","x","x"],["x"," ","x"],["o","x","o"]]


def draw_game_list():
    print(f'''
 {game_stat[0][0]} | {game_stat[0][1]} | {game_stat[0][2]} 
-----------
 {game_stat[1][0]} | {game_stat[1][1]} | {game_stat[1][2]}
-----------
 {game_stat[2][0]} | {game_stat[2][1]} | {game_stat[2][2]}

          ''')
    
draw_game_list()

def clear_game_list():
    global game_stat
    game_stat = [[" " for i in range(3)] for j in range(3)]
    draw_game_list()
clear_game_list()

"""