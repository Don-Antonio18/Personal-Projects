# importing libraries
import pygame
import time
import random
import math

snake_speed = 8

# Add this near the top with other constants
BLOCK_SIZE = 20  # You can easily change this to any size you want

# Window size
window_x = 800
window_y = 400  # Halved from 800

# Add these colors for the checkerboard and gradients
LIGHT_SQUARE = pygame.Color(162, 209, 73)    # Light green
DARK_SQUARE = pygame.Color(140, 185, 60)     # Darker green
BORDER_COLOR = pygame.Color(120, 165, 50)    # Border green
SNAKE_COLOR = pygame.Color(34, 89, 34)       # Dark green for snake
FOOD_COLOR = pygame.Color(101, 67, 33)       # Dark brown for food
SCORE_COLOR = pygame.Color(25, 70, 25)       # Very dark green for score text

# Add this for food animation
food_animation_counter = 0
FOOD_PULSE_SPEED = 0.15
FOOD_SIZE_VARIATION = 4  # How much the food size varies while pulsing

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption("Kayla Eat Dot")
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake
# body
snake_body = [
    [100, 100],
    [100 - BLOCK_SIZE, 100],
    [100 - (2 * BLOCK_SIZE), 100],
    [100 - (3 * BLOCK_SIZE), 100]
]
# fruit position
fruit_position = [
    random.randrange(1, (window_x // BLOCK_SIZE)) * BLOCK_SIZE,
    random.randrange(1, (window_y // BLOCK_SIZE)) * BLOCK_SIZE,
]
fruit_spawn = True

# setting default snake direction
# towards right
direction = "RIGHT"
change_to = direction

# initial score
score = 0


# displaying Score function
def show_score(choice, color, font, size):

    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    # create the display surface object
    # score_surface
    score_surface = score_font.render("Score : " + str(score), True, SCORE_COLOR)

    # create a rectangular object for the
    # text surface object
    score_rect = score_surface.get_rect()

    # displaying text
    game_window.blit(score_surface, score_rect)


# game over function
def game_over():
    # Declare globals at the start of the function
    global snake_position, snake_body, fruit_position, direction, change_to, score
    
    # creating font object my_font
    my_font = pygame.font.SysFont("times new roman", 50)
    
    # creating text surfaces
    score_surface = my_font.render("Your Score is : " + str(score), True, SCORE_COLOR)
    play_again_surface = my_font.render("Press Y to Play Again or Q to Quit", True, SCORE_COLOR)
    
    # create rectangular objects for the text
    score_rect = score_surface.get_rect()
    play_again_rect = play_again_surface.get_rect()
    
    # setting positions of the text
    score_rect.midtop = (window_x / 2, window_y / 4)
    play_again_rect.midtop = (window_x / 2, window_y / 3)
    
    # Draw everything
    draw_checkerboard()
    game_window.blit(score_surface, score_rect)
    game_window.blit(play_again_surface, play_again_rect)
    pygame.display.flip()
    
    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_y:
                    # Reset game state
                    snake_position = [100, 50]
                    snake_body = [
                        [100, 100],
                        [100 - BLOCK_SIZE, 100],
                        [100 - (2 * BLOCK_SIZE), 100],
                        [100 - (3 * BLOCK_SIZE), 100]
                    ]
                    fruit_position = [
                        random.randrange(1, (window_x // BLOCK_SIZE)) * BLOCK_SIZE,
                        random.randrange(1, (window_y // BLOCK_SIZE)) * BLOCK_SIZE,
                    ]
                    direction = 'RIGHT'
                    change_to = direction
                    score = 0
                    return  # Return to main game loop


def draw_checkerboard():
    for row in range(0, window_y, BLOCK_SIZE):
        for col in range(0, window_x, BLOCK_SIZE):
            # Create gradient effect
            gradient_offset = (row + col) // (BLOCK_SIZE * 2)  # Creates a diagonal gradient
            base_color = LIGHT_SQUARE if (row + col) // BLOCK_SIZE % 2 == 0 else DARK_SQUARE
            
            # Apply gradient
            color = pygame.Color(
                max(0, min(255, base_color.r - gradient_offset)),
                max(0, min(255, base_color.g - gradient_offset)),
                max(0, min(255, base_color.b - gradient_offset))
            )
            
            # Draw main square
            pygame.draw.rect(game_window, color, pygame.Rect(col, row, BLOCK_SIZE, BLOCK_SIZE))
            # Draw border
            pygame.draw.rect(game_window, BORDER_COLOR, pygame.Rect(col, row, BLOCK_SIZE, BLOCK_SIZE), 1)


def draw_food():
    global food_animation_counter
    
    # Calculate size variation using sine wave
    size_offset = int(math.sin(food_animation_counter) * FOOD_SIZE_VARIATION)
    current_size = BLOCK_SIZE + size_offset
    
    # Center the food in its grid position
    x_offset = (BLOCK_SIZE - current_size) // 2
    y_offset = (BLOCK_SIZE - current_size) // 2
    
    pygame.draw.rect(
        game_window,
        FOOD_COLOR,
        pygame.Rect(
            fruit_position[0] + x_offset,
            fruit_position[1] + y_offset,
            current_size,
            current_size
        )
    )
    
    food_animation_counter += FOOD_PULSE_SPEED


# Main Function
while True:

    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Arrow keys
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                change_to = "UP"
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                change_to = "RIGHT"

    # If two keys pressed simultaneously
    # we don't want snake to move into two directions
    # simultaneously
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    # Moving the snake
    if direction == "UP":
        snake_position[1] -= BLOCK_SIZE
    if direction == "DOWN":
        snake_position[1] += BLOCK_SIZE
    if direction == "LEFT":
        snake_position[0] -= BLOCK_SIZE
    if direction == "RIGHT":
        snake_position[0] += BLOCK_SIZE

    # Snake body growing mechanism
    # if fruits and snakes collide then scores will be
    # incremented by 10
    snake_body.insert(0, list(snake_position))
    if (
        abs(snake_position[0] - fruit_position[0]) < BLOCK_SIZE and
        abs(snake_position[1] - fruit_position[1]) < BLOCK_SIZE
    ):
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [
            random.randrange(1, (window_x // BLOCK_SIZE)) * BLOCK_SIZE,
            random.randrange(1, (window_y // BLOCK_SIZE)) * BLOCK_SIZE,
        ]

    fruit_spawn = True
    # game_window.fill(black)
    draw_checkerboard()

    # Draw snake with borders
    for pos in snake_body:
        # Draw main snake block
        pygame.draw.rect(game_window, SNAKE_COLOR, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
        # Draw border around snake block
        pygame.draw.rect(game_window, BORDER_COLOR, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE), 1)

    # Draw animated food
    draw_food()

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x - BLOCK_SIZE:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - BLOCK_SIZE:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # displaying score continuously
    show_score(1, SNAKE_COLOR, "times new roman", 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)
