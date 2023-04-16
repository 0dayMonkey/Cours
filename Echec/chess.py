import pygame

import time

import sys

board = [['  ' for _ in range(8)] for _ in range(8)]

class Piece:
    def __init__(self, equipe, type, image, tuable=False):
        self.equipe = equipe
        self.type = type
        self.tuable = tuable
        self.image = image

bp = Piece('b', 'p', 'assets/pion/pionnr.png')
wp = Piece('w', 'p', 'assets/pion/pionbl.png')
bk = Piece('b', 'k', 'assets/roi/roinr.png')
wk = Piece('w', 'k', 'assets/roi/roibl.png')
br = Piece('b', 'r', 'assets/tour/tournr.png')
wr = Piece('w', 'r', 'assets/tour/tourbl.png')
bb = Piece('b', 'b', 'assets/fou/founr.png')
wb = Piece('w', 'b', 'assets/fou/foubl.png')
bq = Piece('b', 'q', 'assets/reine/reinenr.png')
wq = Piece('w', 'q', 'assets/reine/reinebl.png')
bkn = Piece('b', 'kn', 'assets/cavalier/cavaliernr.png')
wkn = Piece('w', 'kn', 'assets/cavalier/cavalierbl.png')


board_depart = {(0, 0): pygame.image.load(br.image), (1, 0): pygame.image.load(bkn.image),
                  (2, 0): pygame.image.load(bb.image), (3, 0): pygame.image.load(bq.image),
                  (4, 0): pygame.image.load(bk.image), (5, 0): pygame.image.load(bb.image),
                  (6, 0): pygame.image.load(bkn.image), (7, 0): pygame.image.load(br.image),
                  (0, 1): pygame.image.load(bp.image), (1, 1): pygame.image.load(bp.image),
                  (2, 1): pygame.image.load(bp.image), (3, 1): pygame.image.load(bp.image),
                  (4, 1): pygame.image.load(bp.image), (5, 1): pygame.image.load(bp.image),
                  (6, 1): pygame.image.load(bp.image), (7, 1): pygame.image.load(bp.image),

                  (0, 2): None, (1, 2): None, (2, 2): None, (3, 2): None,
                  (4, 2): None, (5, 2): None, (6, 2): None, (7, 2): None,
                  (0, 3): None, (1, 3): None, (2, 3): None, (3, 3): None,
                  (4, 3): None, (5, 3): None, (6, 3): None, (7, 3): None,
                  (0, 4): None, (1, 4): None, (2, 4): None, (3, 4): None,
                  (4, 4): None, (5, 4): None, (6, 4): None, (7, 4): None,
                  (0, 5): None, (1, 5): None, (2, 5): None, (3, 5): None,
                  (4, 5): None, (5, 5): None, (6, 5): None, (7, 5): None,

                  (0, 6): pygame.image.load(wp.image), (1, 6): pygame.image.load(wp.image),
                  (2, 6): pygame.image.load(wp.image), (3, 6): pygame.image.load(wp.image),
                  (4, 6): pygame.image.load(wp.image), (5, 6): pygame.image.load(wp.image),
                  (6, 6): pygame.image.load(wp.image), (7, 6): pygame.image.load(wp.image),
                  (0, 7): pygame.image.load(wr.image), (1, 7): pygame.image.load(wkn.image),
                  (2, 7): pygame.image.load(wb.image), (3, 7): pygame.image.load(wq.image),
                  (4, 7): pygame.image.load(wk.image), (5, 7): pygame.image.load(wb.image),
                  (6, 7): pygame.image.load(wkn.image), (7, 7): pygame.image.load(wr.image),}


def initialisation_board(board):
    board[0] = [Piece('b', 'r', 'assets/tour/tournr.png'), Piece('b', 'kn', 'assets/cavalier/cavaliernr.png'), Piece('b', 'b', 'assets/fou/founr.png'), \
               Piece('b', 'q', 'assets/reine/reinenr.png'), Piece('b', 'k', 'assets/roi/roinr.png'), Piece('b', 'b', 'assets/fou/founr.png'), \
               Piece('b', 'kn', 'assets/cavalier/cavaliernr.png'), Piece('b', 'r', 'assets/tour/tournr.png')]

    board[7] = [Piece('w', 'r', 'assets/tour/tourbl.png'), Piece('w', 'kn', 'assets/cavalier/cavalierbl.png'), Piece('w', 'b', 'assets/fou/foubl.png'), \
               Piece('w', 'q', 'assets/reine/reinebl.png'), Piece('w', 'k', 'assets/roi/roibl.png'), Piece('w', 'b', 'assets/fou/foubl.png'), \
               Piece('w', 'kn', 'assets/cavalier/cavalierbl.png'), Piece('w', 'r', 'assets/tour/tourbl.png')]

    for i in range(8):
        board[1][i] = Piece('b', 'p', 'assets/pion/pionnr.png')
        board[6][i] = Piece('w', 'p', 'assets/pion/pionbl.png')
    return board


def verif_board(position):
    if position[0] > -1 and position[1] > -1 and position[0] < 8 and position[1] < 8:
        return True


def affiche_matrice(board):
    sortie = ''

    for i in board:
        for j in i:
            try:
                sortie += j.equipe + j.type + ', '
            except:
                sortie += j + ', '
        sortie += '\n'
    return sortie

def deselect():
    for ligne in range(len(board)):
        for colone in range(len(board[0])):
            if board[ligne][colone] == 'x ':
                board[ligne][colone] = '  '
            else:
                try:
                    board[ligne][colone].tuable = False
                except:
                    pass
    return affiche_matrice(board)


def highlight(board):
    highlighted = []
    for _ in range(len(board)):
        for j in range(len(board[0])):
            if board[_][j] == 'x ':
                highlighted.append((_, j))
            else:
                try:
                    if board[_][j].tuable:
                        highlighted.append((_, j))
                except:
                    pass
    return highlighted

def verif_equipe(mouvements, index):
    ligne, colo = index
    if mouvements%2 == 0:
        if board[ligne][colo].equipe == 'w':
            return True
    else:
        if board[ligne][colo].equipe == 'b':
            return True

def selection_mouv(piece, index, mouvements):
    if verif_equipe(mouvements, index):
        if piece.type == 'p':
            if piece.equipe == 'b':
                return highlight(mouv_pion_noir(index))
            else:
                return highlight(mouv_pion_blanc(index))

        if piece.type == 'k':
            return highlight(mouv_roi(index))

        if piece.type == 'r':
            return highlight(mouv_tour(index))

        if piece.type == 'b':
            return highlight(mouv_fou(index))

        if piece.type == 'q':
            return highlight(queen_moves(index))

        if piece.type == 'kn':
            return highlight(mouv_cavalier(index))


def mouv_pion_noir(index):
    if index[0] == 1:
        if board[index[0] + 2][index[1]] == '  ' and board[index[0] + 1][index[1]] == '  ':
            board[index[0] + 2][index[1]] = 'x '
    bottom3 = [[index[0] + 1, index[1] + i] for i in range(-1, 2)]

    for positions in bottom3:
        if verif_board(positions):
            if bottom3.index(positions) % 2 == 0:
                try:
                    if board[positions[0]][positions[1]].equipe != 'b':
                        board[positions[0]][positions[1]].tuable = True
                except:
                    pass
            else:
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
    return board

def mouv_pion_blanc(index):
    if index[0] == 6:
        if board[index[0] - 2][index[1]] == '  ' and board[index[0] - 1][index[1]] == '  ':
            board[index[0] - 2][index[1]] = 'x '
    top3 = [[index[0] - 1, index[1] + i] for i in range(-1, 2)]

    for positions in top3:
        if verif_board(positions):
            if top3.index(positions) % 2 == 0:
                try:
                    if board[positions[0]][positions[1]].equipe != 'w':
                        board[positions[0]][positions[1]].tuable = True
                except:
                    pass
            else:
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
    return board


def mouv_roi(index):
    for y in range(3):
        for x in range(3):
            if verif_board((index[0] - 1 + y, index[1] - 1 + x)):
                if board[index[0] - 1 + y][index[1] - 1 + x] == '  ':
                    board[index[0] - 1 + y][index[1] - 1 + x] = 'x '
                else:
                    if board[index[0] - 1 + y][index[1] - 1 + x].equipe != board[index[0]][index[1]].equipe:
                        board[index[0] - 1 + y][index[1] - 1 + x].tuable = True
    return board


def mouv_tour(index):
    cross = [[[index[0] + i, index[1]] for i in range(1, 8 - index[0])],
             [[index[0] - i, index[1]] for i in range(1, index[0] + 1)],
             [[index[0], index[1] + i] for i in range(1, 8 - index[1])],
             [[index[0], index[1] - i] for i in range(1, index[1] + 1)]]

    for direction in cross:
        for positions in direction:
            if verif_board(positions):
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
                else:
                    if board[positions[0]][positions[1]].equipe != board[index[0]][index[1]].equipe:
                        board[positions[0]][positions[1]].tuable = True
                    break
    return board


def mouv_fou(index):
    diagonals = [[[index[0] + i, index[1] + i] for i in range(1, 8)],
                 [[index[0] + i, index[1] - i] for i in range(1, 8)],
                 [[index[0] - i, index[1] + i] for i in range(1, 8)],
                 [[index[0] - i, index[1] - i] for i in range(1, 8)]]

    for direction in diagonals:
        for positions in direction:
            if verif_board(positions):
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
                else:
                    if board[positions[0]][positions[1]].equipe != board[index[0]][index[1]].equipe:
                        board[positions[0]][positions[1]].tuable = True
                    break
    return board


def queen_moves(index):
    board = mouv_tour(index)
    board = mouv_fou(index)
    return board


def mouv_cavalier(index):
    for i in range(-2, 3):
        for j in range(-2, 3):
            if i ** 2 + j ** 2 == 5:
                if verif_board((index[0] + i, index[1] + j)):
                    if board[index[0] + i][index[1] + j] == '  ':
                        board[index[0] + i][index[1] + j] = 'x '
                    else:
                        if board[index[0] + i][index[1] + j].equipe != board[index[0]][index[1]].equipe:
                            board[index[0] + i][index[1] + j].tuable = True
    return board


WIDTH = 800

fenetre = pygame.display.set_mode((WIDTH, WIDTH))


pygame.display.set_caption("Projet Echec Hadji")

CLAIR =  (250, 229, 211)  # #FAE5D3
FONCEE = (120, 66, 18)  # #784212
SELECTION = (211,184,126)
INTERLIGNE = (0, 0, 0)


class Node:
    def __init__(self, ligne, colo, width):
        self.ligne = ligne
        self.colo = colo
        self.x = int(ligne * width)
        self.y = int(colo * width)
        self.couleur = CLAIR
        self.occupe = None

    def draw(self, fenetre):
        pygame.draw.rect(fenetre, self.couleur, (self.x, self.y, WIDTH / 8, WIDTH / 8))

    def setup(self, fenetre):
        if board_depart[(self.ligne, self.colo)]:
            if board_depart[(self.ligne, self.colo)] == None:
                pass
            else:
                fenetre.blit(board_depart[(self.ligne, self.colo)], (self.x, self.y))

        fenetre.blit(pygame.image.load("assets/vertical.png"), (0,0))
        fenetre.blit(pygame.image.load("assets/horizontal.png"), (80,705))
def creation_grille(rows, width):
    grid = []
    gap = WIDTH // rows
    print(gap)
    for _ in range(rows):
        grid.append([])
        for __ in range(rows):
            node = Node(__, _, gap)
            grid[_].append(node)
            if (_+__)%2 ==1:
                grid[_][__].couleur = FONCEE
    return grid


def draw_grid(win, rows, width):
    gap = width // 8
    for _ in range(rows):
        pygame.draw.line(win, INTERLIGNE, (0, _ * gap), (width, _ * gap))
        for __ in range(rows):
            pygame.draw.line(win, INTERLIGNE, (__ * gap, 0), (__ * gap, width))



def maj_affichage(win, grid, rows, width):
    for ligne in grid:
        for spot in ligne:
            spot.draw(win)
            spot.setup(win)
    draw_grid(win, rows, width)

    pygame.display.update()


def Find_Node(pos, WIDTH):
    interval = WIDTH / 8
    y, x = pos
    rows = y // interval
    columns = x // interval
    return int(rows), int(columns)


def affichage_mouv_possibles(positions, grid):
    for i in positions:
        x, y = i
        grid[x][y].couleur = SELECTION


def act_mouv(PosiOriginale, PosiFinale, fenetre):
    board_depart[PosiFinale] = board_depart[PosiOriginale]
    board_depart[PosiOriginale] = None


def suppr_highlight(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i+j)%2 == 0:
                grid[i][j].couleur = CLAIR
            else:
                grid[i][j].couleur = FONCEE
    return grid

initialisation_board(board)


def main(fenetre, WIDTH):
    mouvements = 0
    choisie = False
    piece_a_bouger=[]
    grid = creation_grille(8, WIDTH)
    while True:
        pygame.time.delay(50) ##stops cpu dying
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                y, x = Find_Node(pos, WIDTH)
                if choisie == False:
                    try:
                        possible = selection_mouv((board[x][y]), (x,y), mouvements)
                        for positions in possible:
                            ligne, colo = positions
                            grid[ligne][colo].couleur = SELECTION
                        piece_a_bouger = x,y
                        choisie = True
                    except:
                        piece_a_bouger = []
                        print('Impossible de selectionner cettte pièce')
                    #print(piece_a_bouger)

                else:
                    try:
                        if board[x][y].tuable == True:
                            ligne, colo = piece_a_bouger #coordonnées de la piece de base
                            board[x][y] = board[ligne][colo]
                            board[ligne][colo] = '  '
                            deselect()
                            suppr_highlight(grid)
                            act_mouv((colo, ligne), (y, x), fenetre)
                            mouvements += 1
                            # print(mouvements) // affiche log
                            print(affiche_matrice(board))
                        else:
                            deselect()
                            suppr_highlight(grid)
                            choisie = False
                            print("Désélectionné")
                    except:
                        if board[x][y] == 'x ':
                            ligne, colo = piece_a_bouger
                            board[x][y] = board[ligne][colo]
                            board[ligne][colo] = '  '
                            deselect()
                            suppr_highlight(grid)
                            act_mouv((colo, ligne), (y, x), fenetre)
                            mouvements += 1
                            #print(mouvements) // affiche log
                            print(affiche_matrice(board))
                        else:
                            deselect()
                            suppr_highlight(grid)
                            choisie = False
                            print("Mouvement invalide")
                    choisie = False

            maj_affichage(fenetre, grid, 8, WIDTH)


main(fenetre, WIDTH)