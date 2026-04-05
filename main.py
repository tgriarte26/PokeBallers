import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
ball_x = 100
ball_y = 300
ball_radius = 15

speed = 5
velocity_y = 0
velocity_x = 0
gravity = 0.5
direction = 1

hoop_x = 600
hoop_y = 300
hoop_width = 80
hoop_height = 10

score = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PokeBallers")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 40)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  keys = pygame.key.get_pressed()

  # Shot
  if keys[pygame.K_LEFT]:
    ball_x -= speed if on_ground else speed * 0
    direction = -1
  if keys[pygame.K_RIGHT]:
    ball_x += speed if on_ground else speed * 0
    direction = 1

  # Jump when on ground
  if ball_y + ball_radius >= HEIGHT:
    on_ground = True
  else:
    on_ground = False
    
  if keys[pygame.K_SPACE] and on_ground:
    velocity_y = -20
    velocity_x = 6 * direction

  # Gravity mechanic
  velocity_y += gravity
  ball_y += velocity_y
  ball_x += velocity_x
  velocity_x *= 0.98

  if (hoop_x < ball_x < hoop_x + hoop_width) and (hoop_y - ball_radius < ball_y < hoop_y) and velocity_y > 0:
    score += 1
    pygame.time.delay(300)
    ball_x = 100
    ball_y = HEIGHT - ball_radius
    velocity_x = 0
    velocity_y = 0

  # Collision with ground
  if ball_y + ball_radius >= HEIGHT:
    ball_y = HEIGHT - ball_radius
    velocity_y = 0

  # Side boundaries
  if ball_x - ball_radius < 0:
    ball_x = ball_radius
  if ball_x + ball_radius > WIDTH:
    ball_x = WIDTH - ball_radius

  if ball_y - ball_radius < 0:
    ball_y = ball_radius


  screen.fill((30,30,30))
  pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), 
  ball_radius)
  pygame.draw.rect(screen, (255, 165, 0), (hoop_x, hoop_y, hoop_width, hoop_height))
  score_text = font.render(f"Score: {score}", True, (255, 255, 255))
  screen.blit(score_text, (10, 10))
  pygame.display.update()
  clock.tick(60)