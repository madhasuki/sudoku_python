import pygame
import numpy as np
from generator import getGrid, solve

WIDTH = 550
HEIGHT = 600
backgroud_color = (251, 247, 245)
original_grid_element_color = (52, 31, 151)
blue_box_color = (205, 237, 255)
clicked_box_color = (175, 207, 255)
button_color = (50, 100, 50)
button_hover = (30, 70, 30)

buffer = 2


def new_game():
    global grid
    global grid_original

    grid = getGrid()

    # grid = [
    #     [4, 0, 2, 6, 3, 8, 1, 0, 0],
    #     [0, 8, 0, 9, 5, 0, 3, 0, 0],
    #     [3, 1, 0, 0, 7, 2, 5, 0, 6],
    #     [0, 7, 0, 1, 2, 3, 6, 5, 0],
    #     [8, 0, 0, 7, 0, 0, 0, 0, 1],
    #     [0, 0, 0, 0, 8, 0, 0, 0, 0],
    #     [0, 4, 3, 8, 1, 0, 0, 0, 2],
    #     [6, 0, 0, 0, 0, 4, 0, 1, 0],
    #     [1, 9, 0, 0, 0, 5, 0, 0, 7]
    # ]

    grid_original = [
        [grid[x][y] for y in range(9)] for x in range(len(grid))
    ]


def insert(win, position, myFont):
    i, j = position[1], position[0]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                clicked(win, myFont)
                return
            if event.type == pygame.KEYDOWN:
                if(grid_original[i-1][j-1] != 0):
                    return
                if(event.key == 48):  # checking with 0
                    grid[i-1][j-1] = event.key - 48
                    pygame.draw.rect(win, clicked_box_color, (
                        position[0]*50 + 2, position[1]*50 + 2, 50 - 3, 50 - 3)
                    )
                    pygame.display.update()
                if(0 < event.key - 48 < 10):  # We are checking for valid input
                    pygame.draw.rect(win, clicked_box_color, (
                        position[0]*50 + 2, position[1]*50 + 2, 50 - 3, 50 - 3)
                    )
                    value = myFont.render(str(event.key - 48), True, (0, 0, 0))
                    win.blit(value, (position[0]*50+15, position[1]*50 + 5))
                    grid[i-1][j-1] = event.key - 48
                    pygame.display.update()
                return


def create_screen(win, myFont):
    for i in range(0, 10):
        coor = 50 + 50 * i
        line_bold = 2

        if (i % 3 == 0):
            line_bold = 3

        # Vertical line
        pygame.draw.line(win, (0, 0, 0), (coor, 50), (coor, 500), line_bold)
        # Horizontal line
        pygame.draw.line(win, (0, 0, 0), (50, coor), (500, coor), line_bold)

    for i in range(0, 9):
        for j in range(0, 9):
            if (0 < grid_original[i][j] < 10):
                value = myFont.render(
                    str(grid_original[i][j]), True, original_grid_element_color)
                win.blit(value, ((j+1)*50 + 15, (i+1)*50 + 5))
            elif(grid_original[i][j] == 0 and 0 < grid[i][j] < 10):
                value = myFont.render(
                    str(grid[i][j]), True, (0, 0, 0))
                win.blit(value, ((j+1)*50 + 15, (i+1)*50 + 5))

    button_font = pygame.font.Font('font/VarelaRound-Regular.ttf', 15)
    pygame.draw.rect(win, button_color, (100, 525, 110, 40), border_radius=20)
    value = button_font.render(
        "New Game", True, (255, 255, 255))
    win.blit(value, (116, 535))

    pygame.draw.rect(win, button_color, (350, 525, 110, 40), border_radius=20)
    value = button_font.render(
        "Solve", True, (255, 255, 255))
    win.blit(value, (388, 535))

    pygame.display.update()


def clear_screen(win, myFont):
    win.fill(backgroud_color)
    create_screen(win, myFont)


def clicked_screen(win, myFont, pos0, pos1):
    pygame.draw.rect(win, blue_box_color,
                     (52, pos1*50 + 2, 450 - 3, 50 - 3))
    pygame.draw.rect(win, blue_box_color,
                     (pos0*50 + 2, 52, 50 - 3, 450 - 3))
    block0 = (pos0-1) // 3 * 150 + 50
    block1 = (pos1-1) // 3 * 150 + 50
    pygame.draw.rect(win, blue_box_color,
                     (block0 + 2, block1 + 2, 150 - 3, 150 - 3))

    create_screen(win, myFont)


def clicked(win, myFont):
    pos = pygame.mouse.get_pos()
    pos0 = pos[0]//50
    pos1 = pos[1]//50
    # print(pos0, pos1)

    if (pos0 != 0 and pos0 < 10) and (pos1 != 0 and pos1 < 10):
        clear_screen(win, myFont)
        clicked_screen(win, myFont, pos0, pos1)

        pygame.draw.rect(win, clicked_box_color, (
            pos0*50 + 2, pos1*50 + 2, 50 - 3, 50 - 3)
        )
        if(grid_original[pos1-1][pos0-1] != 0):
            value = myFont.render(
                str(grid[pos1-1][pos0-1]), True, original_grid_element_color)
            win.blit(value, (pos0*50+15, pos1*50 + 5))
        elif (grid[pos1-1][pos0-1] != 0):
            value = myFont.render(
                str(grid[pos1-1][pos0-1]), True, (0, 0, 0))
            win.blit(value, (pos0*50+15, pos1*50 + 5))
        pygame.display.update()

        # if(grid_original[pos1-1][pos0-1] == 0):
        insert(win, (pos0, pos1), myFont)
    else:
        clear_screen(win, myFont)

    if ((pos[0] >= 100 and pos[0] <= 210) and (pos[1] >= 525 and pos[1] <= 565)):
        new_game()
        clear_screen(win, myFont)
    if ((pos[0] >= 350 and pos[0] <= 460) and (pos[1] >= 525 and pos[1] <= 565)):
        solve(grid)
        clear_screen(win, myFont)


def validatingSudoku():
    row = []
    column = []
    block = []

    for i in range(9):
        # get the column
        row_i = set(grid[i])
        # get the row
        column_i = set()
        for j in range(0, 9):
            column_i.add(grid[j][i])
        # get the block
        block_i = np.array(grid).reshape((3, 3, 3, 3)).transpose(
            (0, 2, 1, 3)).reshape((9, 9))
        block_i = set(block_i[i])

        # remove all the 0
        if 0 in column_i:
            column_i.remove(0)
        if 0 in row_i:
            row_i.remove(0)
        if 0 in block_i:
            block_i.remove(0)

        # check if has all the number
        if (len(column_i) == 9):
            column.append(True)

        if (len(row_i) == 9):
            row.append(True)

        if (len(block_i) == 9):
            block.append(True)

    if(len(row) and len(column) and len(block) == 9):
        return True
    else:
        return False


def winTheGame(win, font):
    myFont = pygame.font.Font('font/VarelaRound-Regular.ttf', 20)

    pygame.draw.rect(win, (227, 240, 158,),
                     (50, HEIGHT/3, WIDTH-100, 100))
    text = myFont.render("You win!", True, (0, 0, 0))
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2-50))
    win.blit(text, text_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                clear_screen(win, font)
                return
            if event.type == pygame.QUIT:
                pygame.quit()
                return


def main():
    new_game()
    pygame.init()
    myFont = pygame.font.Font('font/VarelaRound-Regular.ttf', 35)
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    # myFont = pygame.font.SysFont(varela, 35)
    clear_screen(win, myFont)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                clicked(win, myFont)

                if validatingSudoku():
                    grid_original = grid
                    winTheGame(win, myFont)
                    clicked(win, myFont)

            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEMOTION:
                position = pygame.mouse.get_pos()
                button_font = pygame.font.Font(
                    'font/VarelaRound-Regular.ttf', 15)
                if ((position[0] >= 100 and position[0] <= 210) and (position[1] >= 525 and position[1] <= 565)):
                    pygame.draw.rect(win, button_hover,
                                     (100, 525, 110, 40), border_radius=20)
                    value = button_font.render(
                        "New Game", True, backgroud_color)
                    win.blit(value, (116, 535))
                    pygame.display.update()
                elif ((position[0] >= 350 and position[0] <= 460) and (position[1] >= 525 and position[1] <= 565)):
                    pygame.draw.rect(win, button_hover,
                                     (350, 525, 110, 40), border_radius=20)
                    value = button_font.render(
                        "Solve", True, backgroud_color)
                    win.blit(value, (388, 535))
                    pygame.display.update()
                else:
                    pygame.draw.rect(win, button_color,
                                     (100, 525, 110, 40), border_radius=20)
                    value = button_font.render(
                        "New Game", True, (255, 255, 255))
                    win.blit(value, (116, 535))

                    pygame.draw.rect(win, button_color,
                                     (350, 525, 110, 40), border_radius=20)
                    value = button_font.render(
                        "Solve", True, (255, 255, 255))
                    win.blit(value, (388, 535))

                    pygame.display.update()


main()
