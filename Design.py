import pygame

pygame.init()

gamedisplay=pygame.display.set_mode((300,300))

pygame.display.update()

pygame.display.set_caption('Hello')

gameExit = False

while not gameExit:
	for event in pygame.event.get():
		if pygame.event == pygame.quit:
			gameExit = True
			
		#print(event)
