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
    


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.blit(cheese, (cheese_x,cheese_y))
           
        pygame.display.flip() 
        pygame.display.update()    

        screen.fill((255,205,77))
        
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