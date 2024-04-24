import pygame
pygame.init()

##=========================================================================================================================================
##GLOBALS

WIDTH = 900
HEIGHT = 800
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))                                           #Setting up the pygame window
pygame.display.set_caption("CHESS")

FONT = pygame.font.Font("freesansbold.ttf", 18)
MED_FONT = pygame.font.Font("freesansbold.ttf", 36)
BIG_FONT = pygame.font.Font("freesansbold.ttf", 48)

TIMER = pygame.time.Clock()

turn_step = 0                                                                            #0: White Turn, 1: White Piece Selected, 3,4: Black
selection = 100                                                                          #Set as index of selected piece from playing lists
w_captured = []
b_captured = []
valid_moves = []
castling_moves= []

counter = 0                                                                              #Game winning variables
check = False
winner = ''
game_over = False

w_ep = (100, 100)                                                                        #En Passant indexes
b_ep = (100, 100)

w_promotion = False                                                                      #Pawn Promotion variables
b_promotion = False
promote_i = 100

##=========================================================================================================================================
##Pieces

PIECE_LIST = ['Rook', 'Knight', 'Bishop', 'Commander', 'King', 'Pawn']
w_pieces = ['Rook', 'Knight', 'Bishop', 'King', 'Commander', 'Bishop', 'Knight', 'Rook',
            'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn']
w_location = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
b_pieces = ['Rook', 'Knight', 'Bishop', 'King', 'Commander', 'Bishop', 'Knight', 'Rook',
            'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn']
b_location = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
promotions = ['Commander', 'Bishop', 'Rook', 'Knight']
w_moved = [False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False ]
b_moved = [False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False ]
w_options = []
b_options = []
castling_moves = []