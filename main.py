import pygame

def main():

    pygame.init()
    

    logo, cheese = load_assets()

    pygame.display.set_icon(logo)
    pygame.display.set_caption("Cheese Game")

    # Creating the surface
    screen = pygame.display.set_mode((1000,600))

    #spawning cheese

    running = True

    screen_x=1000
    screen_y=600
    cheese_x=425
    cheese_y=250
    step=2
    
    #load image
    bg = pygame.image.load("Images\pixil-frame-0.png").convert()
    bg = pygame.transform.scale(bg, (1000, 600))
    
    
    #define game variables
    tiles = (screen_x / 1000)
    scroll = 0
    
    

#run game
    while running:
     
        
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        #draw scrolling background
        screen.blit(bg, (0, 0))
        screen.blit(cheese, (cheese_x,cheese_y))
        
        #scroll background
        scroll -= 5
           
        pygame.display.flip() 
        pygame.display.update()    
        
        #cheese move
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_LEFT] and cheese_x > step:
            cheese_x -= step
        if key_input[pygame.K_RIGHT] and cheese_x < screen_x - 132 - step:
            cheese_x += step
        if key_input[pygame.K_UP] and cheese_y > step:
            cheese_y -= step
        if key_input[pygame.K_DOWN] and cheese_y < screen_y - 100 - step:
            cheese_y += step
        
def load_assets():

    # Set cheese logo
    logo = pygame.image.load("Images\CheeseLogo.png")

    # import cheese
    cheese = pygame.image.load("Images\CheeseSprite.png")
    cheese = pygame.transform.scale(cheese, (132, 100))
    

    return logo, cheese

if __name__=="__main__":
    main()