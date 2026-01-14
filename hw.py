import pygame

pygame.init()
screen=pygame.display.set_mode((300,300))
bg=pygame.transform.scale(pygame.image.load('game2.png').convert(),(500,500))
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("ADDING IMAGE")
bg2=pygame.transform.scale(pygame.image.load('vk.png').convert(),(100,100))


done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(bg,(0,0))
    screen.blit(bg2,(100,100))
    pygame.draw.rect(screen,"red",pygame.Rect(200,200,20,50))
    pygame.display.flip()

