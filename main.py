import pygame
from variables import *
pygame.init()

##=========================================================================================================================================
##Loading Board Pieces

def load_pieces():
    '''
    Load up the images from the assets folder
    Makes up two versions of them depending upon size
    Declares Global lists of these images seperately
    i.e w_images, ws_images, b_images, bs_images
    '''
    w_rook = pygame.image.load('assets\\W_Rook.png')
    w_knight = pygame.image.load('assets\\W_Knight.png')
    w_bishop = pygame.image.load('assets\\W_Bishop.png')
    w_commander = pygame.image.load('assets\\W_Commander.png')
    w_king = pygame.image.load('assets\\W_King.png')
    w_pawn = pygame.image.load('assets\\W_Pawn.png')
    b_rook = pygame.image.load('assets\\B_Rook.png')
    b_knight = pygame.image.load('assets\\B_Knight.png')
    b_bishop = pygame.image.load('assets\\B_Bishop.png')
    b_commander = pygame.image.load('assets\\B_Commander.png')
    b_king = pygame.image.load('assets\\B_King.png')
    b_pawn = pygame.image.load('assets\\B_Pawn.png')

    w_rook = pygame.transform.scale(w_rook, (60, 60))
    w_knight = pygame.transform.scale(w_knight, (60, 60))
    w_bishop = pygame.transform.scale(w_bishop, (60, 60))
    w_commander = pygame.transform.scale(w_commander, (60, 60))
    w_king = pygame.transform.scale(w_king, (60, 60))
    w_pawn = pygame.transform.scale(w_pawn, (50, 50))
    b_rook = pygame.transform.scale(b_rook, (60, 60))
    b_knight = pygame.transform.scale(b_knight, (60, 60))
    b_bishop = pygame.transform.scale(b_bishop, (60, 60))
    b_commander = pygame.transform.scale(b_commander, (60, 60))
    b_king = pygame.transform.scale(b_king, (60, 60))
    b_pawn = pygame.transform.scale(b_pawn, (50, 50))

    ws_rook = pygame.transform.scale(w_rook, (40, 40))
    ws_knight = pygame.transform.scale(w_knight, (40, 40))
    ws_bishop = pygame.transform.scale(w_bishop, (40, 40))
    ws_commander = pygame.transform.scale(w_commander, (40, 40))
    ws_king = pygame.transform.scale(w_king, (40, 40))
    ws_pawn = pygame.transform.scale(w_pawn, (35, 35))
    bs_rook = pygame.transform.scale(b_rook, (40, 40))
    bs_knight = pygame.transform.scale(b_knight, (40, 40))
    bs_bishop = pygame.transform.scale(b_bishop, (40, 40))
    bs_commander = pygame.transform.scale(b_commander, (40, 40))
    bs_king = pygame.transform.scale(b_king, (40, 40))
    bs_pawn = pygame.transform.scale(b_pawn, (35, 35))

    global w_images
    w_images = [w_rook, w_knight, w_bishop, w_commander, w_king, w_pawn]
    global ws_images
    ws_images = [ws_rook, ws_knight, ws_bishop, ws_commander, ws_king, ws_pawn]
    global b_images
    b_images = [b_rook, b_knight, b_bishop, b_commander, b_king, b_pawn]
    global bs_images
    bs_images = [bs_rook, bs_knight, bs_bishop, bs_commander, bs_king, bs_pawn]

##=========================================================================================================================================
##Drawing up the Chess

def draw_board():
    """Draws the chess board."""
    for i in range(32):                                           
        col = i % 4
        row = i // 4
        if row%2 == 0:
            pygame.draw.rect(WIN, 'light gray', [540 - (col*180), row*90, 90, 90])
        else:
            pygame.draw.rect(WIN, 'light gray', [630 - (col*180), row*90, 90, 90])
    pygame.draw.rect(WIN, 'black', [0, 720, WIDTH, 80])
    pygame.draw.rect(WIN, 'gray', [0, 720, WIDTH, 80], 4)
    pygame.draw.rect(WIN, 'black', [720, 0, 180, 720])
    pygame.draw.rect(WIN, 'gray', [720, 0, 180, HEIGHT], 4)

    status_text = ["White: Select a Piece to move",
                    "White: Place the move",
                    "Black: Select a Piece to move",
                    "Black: Place the move"]
    WIN.blit(BIG_FONT.render(status_text[turn_step], True, (200, 200, 200)), (15, 735))

    for i in range(9):
        pygame.draw.line(WIN, 'black', (0, 90 * i), (720, 90 * i), 2)
        pygame.draw.line(WIN, 'black', (90 * i, 0), (90 * i, 720), 2)
    WIN.blit(MED_FONT.render('FORFEIT', True, 'white'), (730, 742))

    if w_promotion or b_promotion:
        pygame.draw.rect(WIN, 'black', [0, 720, WIDTH, 80])
        pygame.draw.rect(WIN, 'gray', [0, 720, WIDTH, 80], 4)
        WIN.blit(BIG_FONT.render('Select Piece to Promote to', True, (200, 200, 200)), (15, 735))


def draw_pieces():
    '''
    Fetches the piece's image from the image list acc to PIECE_LIST list
    Draws the pieces on the board according to the location array
    '''
    for i in range( len(w_pieces) ):
        index = PIECE_LIST.index(w_pieces[i])
        if w_pieces[i] == 'pawn':
            WIN.blit(w_images[index], (w_location[i][0] * 90 + 40, w_location[i][1] * 90 + 52))
        else:
            WIN.blit(w_images[index], (w_location[i][0] * 90 + 17, w_location[i][1] * 90 + 27))

        if turn_step <= 1:                                                               #Highlighting the box
            if selection == i:
                pygame.draw.rect(WIN, 'red', [w_location[i][0]*90+1, w_location[i][1]*90+1, 90, 90], 2)

    for i in range( len(b_pieces) ):
        index = PIECE_LIST.index(b_pieces[i])
        if b_pieces[i] == 'pawn':
            WIN.blit(b_images[index], (b_location[i][0] * 90 + 40, b_location[i][1] * 90 + 52))
        else:
            WIN.blit(b_images[index], (b_location[i][0] * 90 + 17, b_location[i][1] * 90 + 27))
            
        if turn_step >= 2:                                                               #Highlighting the box
            if selection == i:
                pygame.draw.rect(WIN, 'blue', [b_location[i][0]*90+1, b_location[i][1]*90+1, 90, 90], 2)


def draw_valid(moves):
    '''Draws up all the valid moves from the given moves list'''
    color = ''
    if turn_step <= 1:
        color = 'red'
    else:
        color = 'blue'

    for i in range( len(moves) ):
        pygame.draw.circle(WIN, color, (moves[i][0] * 90 + 45, moves[i][1] * 90 + 45), 5)
    

def draw_captured():
    for i in range( len(w_captured) ):
        piece = w_captured[i]
        index = PIECE_LIST.index(piece)
        WIN.blit(bs_images[index], (750, 8 + 40*i))
    for i in range( len(b_captured) ):
        piece = b_captured[i]
        index = PIECE_LIST.index(piece)
        WIN.blit(ws_images[index], (830, 8 + 40*i))


def draw_check():
    '''Drawing a flashing square around king if in check'''

    if turn_step <= 1:
        if 'King' in w_pieces:
            king_i = w_pieces.index('King')
            king_loc = w_location[king_i]
            for i in range( len(b_options) ):
                if king_loc in b_options[i]:
                    if counter < 15:
                        pygame.draw.rect(WIN, 'dark red', [w_location[king_i][0]*90 +1,
                                                            w_location[king_i][1]*90 +1, 90, 90], 5)
    else:
        if 'King' in b_pieces:
            king_i = b_pieces.index('King')
            king_loc = b_location[king_i]
            for i in range( len(w_options) ):
                if king_loc in w_options[i]:
                    if counter < 15:
                        pygame.draw.rect(WIN, 'dark blue', [b_location[king_i][0]*90 +1,
                                                            b_location[king_i][1]*90 +1, 90, 90], 5)


def draw_game_over():
    pygame.draw.rect(WIN, 'black', [200, 200, 400, 70])
    WIN.blit(FONT.render(f'{winner.upper()} won the game!', True, 'white'), (210, 210))
    WIN.blit(FONT.render(f'Press ENTER to Restart!', True, 'white'), (210, 240))


def draw_promotion():
    color = ''
    pygame.draw.rect(WIN, 'dark gray', [720, 0, 180, 380])
    if w_promotion:
        color = 'white'
        for i in range( len(promotions) ):
            piece = promotions[i]
            index = PIECE_LIST.index(piece)
            WIN.blit(w_images[index], (770, 5 + 90*i))
    elif b_promotion:
        color = 'black'
        for i in range( len(promotions) ):
            piece = promotions[i]
            index = PIECE_LIST.index(piece)
            WIN.blit(b_images[index], (770, 5 + 90*i))
    pygame.draw.rect(WIN, color, [720, 0, 180, 380], 4)


##=========================================================================================================================================
##FUNCTIONS
    
def check_pawn(pos, color):
    '''Checking all the valid pawn moves position and populating moves list'''
    moves_list = []
    x, y = pos

    if color == 'white':
        if ((x, y+1) not in w_location) and ((x,y+1) not in b_location) and (y < 7):     #One Step forward & Not off board
            moves_list.append((x, y+1))
            if ((x, y+2) not in w_location) and ((x,y+2) not in b_location) and (y == 1):#First move two step forward
                moves_list.append((x, y+2))
        if (x+1, y+1) in b_location:                                                     #Right Diagonal Attack Down
            moves_list.append((x+1,y+1))
        if (x-1, y+1) in b_location:                                                     #Left Diagonal Attack Down
            moves_list.append((x-1,y+1))
        if (x+1, y+1) == b_ep:                                                           #Right Diagonal En Passant
            moves_list.append((x+1,y+1))
        if (x-1, y+1) == b_ep:                                                           #Left Diagonal En Passant
            moves_list.append((x-1,y+1))
            

    elif color == 'black':
        if ((x, y-1) not in w_location) and ((x,y-1) not in b_location) and (y > 0):     #One Step forward & Not off board
            moves_list.append((x, y-1))
            if ((x, y-2) not in w_location) and ((x,y-2) not in b_location) and (y == 6):#First move two step forward
                moves_list.append((x, y-2))
        if (x+1, y-1) in w_location:                                                     #Right Diagonal Attack Up
            moves_list.append((x+1,y-1))
        if (x-1, y-1) in w_location:                                                     #Left Diagonal Attack Up
            moves_list.append((x-1,y-1))
        if (x+1, y-1) == w_ep:                                                           #Right Diagonal En Passant
            moves_list.append((x+1,y-1))
        if (x-1, y-1) == w_ep:                                                           #Left Diagonal En Passant
            moves_list.append((x-1,y-1))

    return moves_list


def check_ep(old_coords, new_coords):
    '''Function to handle en passant capture'''
    if turn_step <= 1:
        index = w_location.index(old_coords)
        ep_coords = (new_coords[0], new_coords[1]-1)
        piece = w_pieces[index]
    else:
        index = b_location.index(old_coords)
        ep_coords = (new_coords[0], new_coords[1]+1)
        piece = b_pieces[index]

    if piece == 'Pawn' and abs(old_coords[1] - new_coords[1]) > 1:
        pass
    else:
        ep_coords = (100, 100)
    return ep_coords


def check_rook(pos, color):
    '''Checking all the valid Rook moves and populating the moves_list'''
    moves_list = []
    a, b = pos

    if color == "white":
        enemies = b_location
        friends = w_location
    else:
        enemies = w_location
        friends = b_location

    for i in range(4):                                                                   #Going in four directions
        path = True                                                                      #Path exists for now
        chain = 1                                                                        #Increasingly checking for next position
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        elif i == 3:
            x = -1
            y = 0
        while path:
            if (a + x*chain, b + y*chain) not in friends and \
                0 <= a + x*chain <= 7 and 0 <= b + y*chain <= 7:                         #Front should be no be in friends
                moves_list.append((a + x * chain, b + y * chain))
                
                if (a + x*chain, b + y*chain) in enemies:                                #Once enemy encountered, no checking ahead of it
                    path = False

                chain += 1                                                               #Increasing to check the next position that direction
            else:
                path = False                                                             #Front is covered by friends

    return moves_list


def check_knight(pos, color):
    '''Checking all the valid Knight moves and populating the moves_list'''
    moves_list = []
    x, y = pos

    knight_moves = [(2, 1), (2, -1), (1, 2), (1, -2),
                     (-1, 2), (-1, -2), (-2, 1), (-2, -1)]                               #8 night directions
    for dx, dy in knight_moves:
        new_x, new_y = x + dx, y + dy
        if new_x >= 8 or new_x < 0 or new_y >= 8 or new_y < 0:                           #Skipping that direction if out of board
            continue
        if (new_x, new_y) in w_location:                                                 #Can't step on the same color pieces
            if color == 'white':
                continue
        if (new_x, new_y) in b_location:
            if color == 'black':
                continue
        moves_list.append((new_x, new_y))                                                #Everything else is valid

    return moves_list


def check_bishop(pos, color):
    '''Checking all the valid Bishop moves and populating the moves_list'''
    moves_list = []
    a, b = pos

    if color == "white":
        enemies = b_location
        friends = w_location
    else:
        enemies = w_location
        friends = b_location

    for i in range(4):                                                                   #Going in four directions
        path = True                                                                      #Path exists for now
        chain = 1                                                                        #Increasingly checking for next position
        if i == 0:
            x = 1
            y = 1
        elif i == 1:
            x = 1
            y = -1
        elif i == 2:
            x = -1
            y = -1
        elif i == 3:
            x = -1
            y = 1
        while path:
            if (a + x*chain, b + y*chain) not in friends and \
                0 <= a + x*chain <= 7 and 0 <= b + y*chain <= 7:                         #Front should be no be in friends
                moves_list.append((a + x * chain, b + y * chain))
                
                if (a + x*chain, b + y*chain) in enemies:                                #Once enemy encountered, no checking ahead of it
                    path = False

                chain += 1                                                               #Increasing to check the next position that direction
            else:
                path = False                                                             #Front is covered by friends

    return moves_list


def check_commander(pos, color):
    '''Checking all the valid Commander moves and populating the moves_list'''
    moves_list = check_rook(pos, color)
    
    m = check_bishop(pos, color)
    for move in m:
        if move not in moves_list:
            moves_list.append(move)

    return moves_list


def check_king(pos, color):
    '''Checking all the valid king moves and populating the moves_list'''
    moves_list = []
    x, y = pos
    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (1, -1), (1, 1), (-1,-1)]:
        new_x, new_y = x + dx, y + dy
        if new_x >= 8 or new_x < 0 or new_y >= 8 or new_y < 0:
            continue
        if (new_x, new_y) in w_location:
            if color == 'white':
                continue
        if (new_x, new_y) in b_location:
            if color == 'black':
                continue
        moves_list.append((new_x, new_y))

    return moves_list


def check_options(pieces, locations, turn):
    moves_list = []
    all_moves = []

    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'Pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'Rook':
            moves_list = check_rook(location, turn)
        elif piece == 'Knight':
            moves_list = check_knight(location, turn)
        elif piece == 'Bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'Commander':
            moves_list = check_commander(location, turn)
        elif piece == 'King':
            moves_list = check_king(location, turn)
        
        all_moves.append(moves_list)

    return all_moves


def check_valid_moves():
    if turn_step <= 1:
        options_list = w_options
    else:
        options_list = b_options

    valid_options = options_list[selection]
    return valid_options


def check_promotion():
    '''Returns the index and color of the pawn that can be promoted'''
    pawn_indexes = []
    w_promotion = False
    b_promotion = False
    promote_i = 100
    
    for i in range( len(w_pieces) ):                                                     #Saving the index of the pawn from w_pieces list
        if w_pieces[i] == 'Pawn':
            pawn_indexes.append(i)
    for i in range( len(pawn_indexes) ):                                                 #If that's y location == 7, promotion possible
        if w_location[pawn_indexes[i]][1] == 7:
            w_promotion = True
            promote_i = pawn_indexes[i]                                                  #Saving the promotion index
    
    pawn_indexes = []                                                                    #Emptying and checking for black on its turn
    for i in range( len(b_pieces) ):                                                     #Saving index of pawn from the b_pieces list
        if b_pieces[i] == 'Pawn':
            pawn_indexes.append(i)
    for i in range( len(pawn_indexes) ):                                                 #If its y location == 0, promotion possible
        if b_location[pawn_indexes[i]][1] == 0:
            b_promotion = True
            promote_i = pawn_indexes[i]                                                  #Saving the index to be promoted

    return w_promotion, b_promotion, promote_i                                           #Returning which promotion and its index


def pawn_promote():
    '''Prmotes the pawn to the selected piece'''
    mouse_pos = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    x = mouse_pos[0] // 90
    y = mouse_pos[1] // 90

    if w_promotion and left_click and x > 7 and y < 4:
        w_pieces[promote_i] = promotions[y]
    elif b_promotion and left_click and x > 7 and y < 4:
        b_pieces[promote_i] = promotions[y]

##=========================================================================================================================================
##MAIN BODY

if __name__ == '__main__':                                                               ##The below code will run iff file's run directly
    load_pieces()

    b_options = check_options(b_pieces, b_location, 'black')
    w_options = check_options(w_pieces, w_location, 'white')
        
    run = True
    while run:
        TIMER.tick(FPS)                                                                  #Frames transition speed per second
        if counter < 30:
            counter += 1
        else:
            counter = 0
        WIN.fill('dark gray')                                                            #Background Color
        draw_board()
        draw_pieces()
        draw_captured()
        draw_check()

        if not game_over:
            w_promotion, b_promotion, promote_i = check_promotion()
            if w_promotion or b_promotion:
                draw_promotion()
                pawn_promote()

        if selection != 100:                                                             #A piece is currently selected
            valid_moves = check_valid_moves()
            draw_valid(valid_moves)

        for event in pygame.event.get():                                                 #Event handling loop
            if event.type == pygame.QUIT:                                                #Closing the Pygame window on pressing X
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
                x_coord = event.pos[0] // 90                                             #Getting coords of mouse click and its box
                y_coord = event.pos[1] // 90
                click_coords = (x_coord, y_coord)
                
                if turn_step <= 1:                                                       #White's Turn
                    if click_coords == (8,8) or click_coords == (9,8):
                        winner = 'black'
                    if click_coords in w_location:                                       #Clicked on a White piece
                        selection = w_location.index(click_coords)                       #Selection set to the index of selected box
                        if turn_step == 0:
                            turn_step = 1
                    if click_coords in valid_moves and selection != 100:                 #Clicking valid spot after selecting a peice
                        w_ep = check_ep(w_location[selection], click_coords)             #Passing current and click coords to check ep
                        w_location[selection] = click_coords                             #Set piece location on board acc to click coors
                        if click_coords in b_location:                                   #If it's a capture
                            b_piece_i = b_location.index(click_coords)                   #Getting the captured black piece index
                            w_captured.append(b_pieces[b_piece_i])                       #Add captured piece to w_captured
                            if b_pieces[b_piece_i] == 'King':
                                winner = 'white'
                            b_pieces.pop(b_piece_i)                                      #Removing it from black's playing list
                            b_location.pop(b_piece_i)                                    #Removing its location as it no longer exists
                        if click_coords == b_ep:                                         #If it's an en passant capture
                            b_piece_i = b_location.index((b_ep[0], b_ep[1]-1))             #Getting the captured black piece index
                            w_captured.append(b_pieces[b_piece_i])                       #Add captured piece to w_captured
                            b_pieces.pop(b_piece_i)                                      #Removing it from black's playing list
                            b_location.pop(b_piece_i)                                    #Removing its location as it no longer exists

                        b_options = check_options(b_pieces, b_location, 'black')
                        w_options = check_options(w_pieces, w_location, 'white')
                        
                        turn_step = 2                                                    #Shifting turn over to black
                        selection = 100                                                  #Absurd value in selected as no selected
                        valid_moves = []                                                 #Reasonable, no valid moves currently

                if turn_step > 1:                                                       #Black's Turn
                    if click_coords == (8,8) or click_coords == (9,8):
                        winner = 'white'
                    if click_coords in b_location:                                       #Cicked on a black piece
                        selection = b_location.index(click_coords)                      #Selection set to the index of that piece's location
                        if turn_step == 2:
                            turn_step = 3
                    if click_coords in valid_moves and selection != 100:                 #Trying to make a valid move
                        b_ep = check_ep(b_location[selection], click_coords)             #Passing current and click coords to check ep
                        b_location[selection] = click_coords                             #Set piece location on board acc to click coors
                        if click_coords in w_location:                                   #If it's a capture
                            w_piece_i = w_location.index(click_coords)                   #Getting the captured black piece index
                            b_captured.append(w_pieces[w_piece_i])                       #Adding captured piece to b_captured
                            if w_pieces[w_piece_i] == 'King':
                                winner = 'black'
                            w_pieces.pop(w_piece_i)                                      #Removing it from the pieces list
                            w_location.pop(w_piece_i)                                    #Removing it from corresponding location list
                        if click_coords == w_ep:                                         #If it's an en passant capture
                            w_piece_i = w_location.index((w_ep[0], w_ep[1]+1))             #Getting the captured white piece index
                            b_captured.append(w_pieces[w_piece_i])                       #Add captured piece to b_captured
                            w_pieces.pop(w_piece_i)                                      #Removing it from white's playing list
                            w_location.pop(w_piece_i)                                    #Removing its location as it no longer exists

                        b_options = check_options(b_pieces, b_location, 'black')
                        w_options = check_options(w_pieces, w_location, 'white')

                        turn_step = 0                                                    #Shifting turn over to white
                        selection = 100                                                  #Absurd value in selected as nothing is
                        valid_moves = []                                                 #Reasonably, no valid moves currently

            if event.type == pygame.KEYDOWN and game_over:                               #Restarting the game if ENTER pressed
                if event.key == pygame.K_RETURN:
                    game_over = False
                    winner = ''
                    w_pieces = ['Rook', 'Knight', 'Bishop', 'King', 'Commander', 'Bishop', 'Knight', 'Rook',
                                'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn']
                    w_location = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                    b_pieces = ['Rook', 'Knight', 'Bishop', 'King', 'Commander', 'Bishop', 'Knight', 'Rook',
                                'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn']
                    b_location = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                    w_captured = []
                    b_captured = []
                    valid_moves = []
                    turn_step = 0
                    selection = 100
                    b_options = check_options(b_pieces, b_location, 'black')
                    w_options = check_options(w_pieces, w_location, 'white')

        if winner != '':
            game_over = True
            draw_game_over()

        pygame.display.update()
    pygame.quit()
