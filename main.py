import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
ball_x = 100
ball_y = 300
ball_radius = 15
speed = 1

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PokeBallers")

clock = pygame.time.Clock()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  keys = pygame.key.get_pressed()

  if keys[pygame.K_LEFT]:
    ball_x -= speed
  if keys[pygame.K_RIGHT]:
    ball_x += speed
  if keys[pygame.K_UP]:
    ball_y -= speed
  if keys[pygame.K_DOWN]:
    ball_y += speed

  screen.fill((30,30,30))
  pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius)
  pygame.display.update()
  clock.tick(60)