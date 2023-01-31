import pygame


def main():
    pygame.init()
    
    char = load_assets()
    
    # displaying screen and setting variables
    pygame.display.set_caption("test game")
    screen = pygame.display.set_mode((screen_x, screen_y))
    
    # Setting run
    running = True
    
    # Screen width and height variables
    screen_x = 1000
    screen_y = 600
    
    # setting future character movement variables
    char_x = 500
    char_y = 300
    step = 2

    # load background image
    bg = pygame.image.load("Images\\bg2.png").convert()
    bg = pygame.transform.scale(bg, (1000, 600))
    


#run game
    while running:
        
        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(bg, (0, 0))
        screen.blit(char, (char_x,char_y))
        
        pygame.display.flip()
        pygame.display.update()
        
        # character move
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_LEFT] and char_x > step:
            char_x -= step
        if key_input[pygame.K_RIGHT] and char_x < screen_x - 72 - step:
            char_x += step
        if key_input[pygame.K_UP] and char_y > step:
            char_y -= step
        if key_input[pygame.K_DOWN] and char_y < screen_y - 81 - step:
            char_y += step

def load_assets():
    # load character
    char = pygame.image.load("Images\CheeseCharacter.png")
    char = pygame.transform.scale(char, (72, 81))
    
    return char

if __name__ == "__test__":
    main()