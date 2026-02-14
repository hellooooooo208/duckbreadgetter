import pygame

pygame.init()
pygame.display.set_caption("Ducky")
screen = pygame.display.set_mode((800, 600))
sprite = pygame.image.load("New Piskel (1).png").convert_alpha() #loads sprites
sprite = pygame.transform.scale(sprite, (200,200))
x, y = 100, 100
#load bread sprite
bread = pygame.image.load("New piskel.png").convert_alpha()
bread = pygame.transform.scale(bread, (200,200))
bread_x, bread_y = 450, 350
bread_visible = True
x, y = 100, 100
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
        
            if event.key == pygame.K_LEFT:                 
                x -= 50                                     #moves 50 
            if event.key == pygame.K_RIGHT:
                x += 50
            if event.key == pygame.K_UP:
                y -= 50  
            if event.key == pygame.K_DOWN:
                y += 50          
            if event.key == pygame.K_a:          # adding WASD controls always make lowercase 
                x -= 50                                     #moves 50 
            if event.key == pygame.K_d:
                x += 50
            if event.key == pygame.K_w:
                y -= 50  
            if event.key == pygame.K_s:
                y += 50          
    ducky_rect = sprite.get_rect(center=(x + 100, y + 100)) #get rect of ducky for collision detection
    bread_rect = bread.get_rect(center=(bread_x + 100, bread_y + 100)) #get rect of bread for collision detection
    
    if ducky_rect.colliderect(bread_rect):
        bread_visible = False

    screen.fill((255, 255, 255)) #white background
    screen.blit(sprite, (x,y)) #draws ducky
    
    if bread_visible:
        screen.blit(bread, (bread_x, bread_y)) #draws bread
    
    pygame.display.flip()


pygame.quit()