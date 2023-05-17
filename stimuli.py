import pygame

# Initialize Pygame
pygame.init()

# Set up the Pygame window
size = (120,120)
screen = pygame.display.set_mode(size)

# Define the colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Create the surface and draw the square and dots on it
surface1 = pygame.Surface(size)
surface1.fill(white)
pygame.draw.rect(surface1, black,(15,15,90,90), 2)
pygame.draw.circle(surface1, black, (60, 40), 10)
pygame.draw.circle(surface1, black, (60, 80), 10)


surface2 = pygame.Surface(size)
surface2.fill(white)
pygame.draw.rect(surface2, black,(15,15,90,90), 2)
pygame.draw.circle(surface2, black, (60, 35), 10)
pygame.draw.circle(surface2, black, (60, 60), 10)
pygame.draw.circle(surface2, black, (60, 85), 10)

surface3 = pygame.Surface(size)
surface3.fill(white)
pygame.draw.polygon(surface3, black,[(60,10),(110,60),(60,110),(10,60)], 2)
pygame.draw.circle(surface3, black, (60, 40), 10)
pygame.draw.circle(surface3, black, (60, 80), 10)

surface4 = pygame.Surface(size)
surface4.fill(white)
pygame.draw.polygon(surface4, black,[(60,10),(110,60),(60,110),(10,60)], 2)
pygame.draw.circle(surface4, black, (60, 35), 10)
pygame.draw.circle(surface4, black, (60, 60), 10)
pygame.draw.circle(surface4, black, (60, 85), 10)

# Save the contents of the surface as a PNG file
pygame.image.save(surface1, "square_with_2_dots.png")
pygame.image.save(surface2, "square_with_3_dots.png")
pygame.image.save(surface3, "diamond_with_2_dots.png")
pygame.image.save(surface4, "diamond_with_3_dots.png")


# Wait for the user to close the window
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

# Quit Pygame
pygame.quit()

