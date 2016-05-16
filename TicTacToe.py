import pygame
import math
import time

 

#Variables
gameExit = False	
current_player = 0
INIT_POS_O = 195 / 2
INIT_POS_X = 25



#Colors
_WHITE = (255, 255, 255)
_BLACK  = (0, 0, 0)
_RED = (255, 15, 30)
_GREEN = (0, 255, 0)
_BLUE = (0, 0, 255)
_YELLOW = (204,204,0)

#Game board
board = [[0 for x in range(3)] for y in range(3)]



#Game init
pygame.init()
gameDisplay = pygame.display.set_mode((600, 600))
gameDisplay.fill(_WHITE)
pygame.display.set_caption('Tic Tac Toe')
pygame.display.update()	


#Pygame variables
font = pygame.font.SysFont(None, 40 ,False, False)
clock = pygame.time.Clock()


#Functions
"""
Draws the board, the existing 'X's and 'O's and the borders
"""
def draw_board():
	global board
	gameDisplay.fill(_WHITE)
	pygame.draw.rect(gameDisplay, _BLACK, [0, 0, 600, 600])
	pygame.draw.rect(gameDisplay, _WHITE, [5, 5, 590, 590])
	pygame.draw.rect(gameDisplay, _BLACK, [0, 195, 600, 10])
	pygame.draw.rect(gameDisplay, _BLACK, [0, 395, 600, 10])
	pygame.draw.rect(gameDisplay, _BLACK, [395, 0, 10, 600])
	pygame.draw.rect(gameDisplay, _BLACK, [195, 0, 10, 600])
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == 1:
				draw_o(i, j)
			elif board[i][j] == 2:
				draw_x(i,j)

"""
Draws an 'x'
"""
def draw_x(x_pos, y_pos):

	board[x_pos][y_pos] = 2
	x_pos = x_pos * 200
	x_pos_end = x_pos + 150
	y_pos = y_pos * 200
	y_pos_end = y_pos + 150
	pygame.draw.line(gameDisplay, _RED, (INIT_POS_X + x_pos, INIT_POS_X + y_pos), (INIT_POS_X + x_pos_end, INIT_POS_X + y_pos_end), 10)
	pygame.draw.line(gameDisplay, _RED, (INIT_POS_X + x_pos, INIT_POS_X + y_pos_end), (INIT_POS_X + x_pos_end, INIT_POS_X + y_pos), 10)
	

"""
Draw an 'O'
"""
def draw_o(x_pos, y_pos):
	board[x_pos][y_pos] = 1
	x_pos = x_pos * 205
	y_pos = y_pos * 205
	pygame.draw.circle(gameDisplay, _GREEN, (INIT_POS_O + x_pos, INIT_POS_O + y_pos), 75, 0)
	pygame.draw.circle(gameDisplay, _WHITE, (INIT_POS_O + x_pos, INIT_POS_O + y_pos), 65, 0)


"""
Gets the position of the map and returns it as a tuple
"""
def get_mouse_position():
	position = pygame.mouse.get_pos()
	position_x = int(math.floor(position[0] / 200))
	position_y = int(math.floor(position[1] / 200))

	return [position_x, position_y]



"""
Checks if the game was won
"""
def check_game_won():
	global board
	#Check |
	if board[0][0] == board[0][1] and board[0][0] == board[0][2] and not board[0][0] == 0:
		return True
	if board[1][0] == board[1][1] and board[1][0] == board[1][2] and not board[1][0] == 0:
		return True
	if board[2][0] == board[2][1] and board[2][0] == board[2][2] and not board[2][0] == 0:
		return True

	#Check -
	if board[0][0] == board[1][0] and board[0][0] == board[2][0] and not board[0][0] == 0:
		return True
	if board[0][1] == board[1][1] and board[0][1] == board[2][1] and not board[0][1] == 0:
		return True
	if board[0][2] == board[1][2] and board[0][2] == board[2][2] and not board[0][2] == 0:
		return True

	#Check \
	if board[0][0] == board[1][1] and board[0][0] == board[2][2] and not board[0][0] == 0:
		return True

	#Check /
	if board[0][2] == board[1][1] and board[0][2] == board[2][0] and not board[0][2] == 0:
		return True

	return False


"""
Draws the shape according to the matching player
"""
def draw_shape(x_pos, y_pos):
	global current_player
	if current_player % 2 == 0:
		draw_o(x_pos, y_pos)
	else:
		draw_x(x_pos, y_pos)

	current_player += 1


#Resets the board
def board_reset():
	global board
	global current_player
	current_player = 0
	for i in range(3):
		for j in range(3):
			board[i][j] = 0




"""
Runs the game logic
"""
def run():
	global gameExit
	global current_player
	global board
	board_reset()
	force_close = False
	while not gameExit:
		draw_board()

		for event in pygame.event.get():
			#Quit button pressed check
			if event.type == pygame.QUIT:
				gameExit = True
				force_close = True

			#Checks of the event is a key button down event
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					force_close = True
					gameExit = True

			#Chechs if the event is a mouse button down event
			if event.type == pygame.MOUSEBUTTONDOWN:
				#Gets the position of the mouse
				position = get_mouse_position()
				#Checks if the posision is empty, if so puts an x or an o according to availibility
				if not board[position[0]][position[1]] == 1 and not board[position[0]][position[1]] == 2:
					draw_shape(position[0], position[1])
		

		
		pygame.display.update()

		if force_close:
			gameExit = True
			return True

		if check_game_won():
			if current_player % 2 == 0:
				return 'Player X Wins!'
			else:
				return 'Player O Wins'
		elif current_player >= 9:
			return 'It\'s a tie!'


def write_who_won():
	global font
	won_text = run()
	if won_text == True:
		pass
	else:
		message = font.render(won_text, True, _BLUE)
		gameDisplay.blit(message, [205, 300])
		again_message = font.render('Enter to play again', True, _BLUE)
		gameDisplay.blit(again_message, [205, 345])
		pygame.display.update()

		exit = False
		while not exit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit = True
				
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						if write_who_won():
							exit = True

		pygame.quit()
		quit()


if __name__ == "__main__":
	write_who_won()
