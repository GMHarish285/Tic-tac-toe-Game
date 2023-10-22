import pygame, sys

pygame.init()


def drawing():
    screen.fill(blue_medium)
    for i in range(9):
        pygame.draw.rect(screen, rect_colour_list[i], rect_list[i])

    pygame.draw.line(screen, black, (115, 10), (115, 330), 3)
    pygame.draw.line(screen, black, (225, 10), (225, 330), 3)
    pygame.draw.line(screen, black, (10, 115), (330, 115), 3)
    pygame.draw.line(screen, black, (10, 225), (330, 225), 3)


def winner_decision():
    global winner

    if winner == "X":
        screen.fill(red_dark)
        winner_font = font_small.render("X wins", True, black)
        winner_font_rect = winner_font.get_rect(center=(170, 200))
        screen.blit(winner_font, winner_font_rect)
    elif winner == "O":
        screen.fill(red_dark)
        winner_font = font_small.render("O wins", True, black)
        winner_font_rect = winner_font.get_rect(center=(170, 200))
        screen.blit(winner_font, winner_font_rect)
    elif winner == "tie":
        screen.fill(red_dark)
        winner_font = font_small.render("Tie", True, black)
        winner_font_rect = winner_font.get_rect(center=(170, 200))
        screen.blit(winner_font, winner_font_rect)

    screen.blit(play_again_font1, play_again_font1_rect)
    screen.blit(play_again_font2, play_again_font2_rect)


def win():
    global winner, screen_window

    if rect_font_list[0] == rect_font_list[1] == rect_font_list[2] != "":
        winner = rect_font_list[0]
        screen_window = "end"
    elif rect_font_list[3] == rect_font_list[4] == rect_font_list[5] != "":
        winner = rect_font_list[3]
        screen_window = "end"
    elif rect_font_list[6] == rect_font_list[7] == rect_font_list[8] != "":
        winner = rect_font_list[6]
        screen_window = "end"
    elif rect_font_list[0] == rect_font_list[3] == rect_font_list[6] != "":
        winner = rect_font_list[0]
        screen_window = "end"
    elif rect_font_list[1] == rect_font_list[4] == rect_font_list[7] != "":
        winner = rect_font_list[1]
        screen_window = "end"
    elif rect_font_list[2] == rect_font_list[5] == rect_font_list[8] != "":
        winner = rect_font_list[2]
        screen_window = "end"
    elif rect_font_list[0] == rect_font_list[4] == rect_font_list[8] != "":
        winner = rect_font_list[0]
        screen_window = "end"
    elif rect_font_list[2] == rect_font_list[4] == rect_font_list[6] != "":
        winner = rect_font_list[2]
        screen_window = "end"
    elif rect_font_list[0] != "" and rect_font_list[1] != "" and rect_font_list[2] != "" and rect_font_list[3] != "" and [4] != "" and rect_font_list[5] != "" and rect_font_list[6] != "" and rect_font_list[7] != "" and rect_font_list[8] != "":
        winner = "tie"
        screen_window = "end"


# screen
screen_width = 340
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic Tac Toe")
icon_window = pygame.image.load("icon_32_tictactoe.png")
pygame.display.set_icon(icon_window)
clock = pygame.time.Clock()

# colours
red_dark = (255, 0, 0)
red_light = (255, 127, 127)
blue_dark = (0, 0, 255)
blue_medium = (150, 170, 255)
blue_light = (173, 216, 230)
black = (0, 0, 0)


# font
font_small = pygame.font.Font("freesansbold.ttf", 32)
font_medium = pygame.font.Font("freesansbold.ttf", 50)
font_large = pygame.font.Font("freesansbold.ttf", 120)

# row 0
rect_1 = pygame.Rect(10, 10, 100, 100)
rect_2 = pygame.Rect(120, 10, 100, 100)
rect_3 = pygame.Rect(230, 10, 100, 100)
# row 1
rect_4 = pygame.Rect(10, 120, 100, 100)
rect_5 = pygame.Rect(120, 120, 100, 100)
rect_6 = pygame.Rect(230, 120, 100, 100)
# row 2
rect_7 = pygame.Rect(10, 230, 100, 100)
rect_8 = pygame.Rect(120, 230, 100, 100)
rect_9 = pygame.Rect(230, 230, 100, 100)

rect_list = [rect_1, rect_2, rect_3, rect_4, rect_5, rect_6, rect_7, rect_8, rect_9]
rect_colour_list = [blue_dark, blue_dark, blue_dark, blue_dark, blue_dark, blue_dark, blue_dark, blue_dark, blue_dark]
rect_font_list = ["", "", "", "", "", "", "", "", ""]

XO_turn = 0
X_font = font_large.render("X", True, black)
O_font = font_large.render("O", True, black)
X_turn_font = font_small.render("X turn", True, black)
X_turn_font_rect = X_turn_font.get_rect(midtop=(170, 340))
O_turn_font = font_small.render("O turn", True, black)
O_turn_font_rect = O_turn_font.get_rect(midtop=(170, 340))
play_again_font1 = font_small.render("Press Space bar", True, black)
play_again_font1_rect = play_again_font1.get_rect(center=(170, 300))
play_again_font2 = font_small.render("to play again", True, black)
play_again_font2_rect = play_again_font2.get_rect(center=(170, 340))

screen_window = "game"
winner = ""

while True:
    mouse = pygame.mouse.get_pos()

    drawing()

    if screen_window == "game":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for i in range(9):
            if rect_list[i].collidepoint(mouse) and rect_font_list[i] == "":
                rect_colour_list[i] = blue_light
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if XO_turn % 2 == 0:
                        rect_font_list[i] = "X"
                    else:
                        rect_font_list[i] = "O"
                    XO_turn += 1
            if not rect_list[i].collidepoint(mouse):
                rect_colour_list[i] = blue_dark

            if rect_font_list[i] == "X":
                screen.blit(X_font, rect_list[i])
            if rect_font_list[i] == "O":
                screen.blit(O_font, rect_list[i])

            if XO_turn % 2 == 0:
                pygame.draw.rect(screen, red_light, X_turn_font_rect)
                screen.blit(X_turn_font, X_turn_font_rect)
            else:
                pygame.draw.rect(screen, red_light, O_turn_font_rect)
                screen.blit(O_turn_font, O_turn_font_rect)

            win()


    if screen_window == "end":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    rect_font_list = ["", "", "", "", "", "", "", "", ""]
                    XO_turn = 0
                    screen_window = "game"
            if event.type == pygame.MOUSEBUTTONDOWN:
                rect_font_list = ["", "", "", "", "", "", "", "", ""]
                XO_turn = 0
                screen_window = "game"
        winner_decision()



    pygame.display.update()
    clock.tick(120)
