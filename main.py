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
hoop_speed = 3
hoop_direction = 1

score = 0
scored = False
just_scored = False
reset_timer = 0

charging = False
power = 0
max_power = 25

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PokeBallers")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 40)

combo = 0
on_fire = False

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  keys = pygame.key.get_pressed()

  if keys[pygame.K_SPACE]:
    charging = True
    power += 0.5
    if power > max_power:
      power = max_power
  
  else:
    if charging: 
      velocity_y = -power
      velocity_x = power * 0.5 * direction
      charging = False
      power = 0

  # Gravity mechanic
  velocity_y += gravity
  ball_y += velocity_y
  ball_x += velocity_x
  velocity_x *= 0.98

  if (not scored and
    hoop_x < ball_x < hoop_x + hoop_width and
    hoop_y - ball_radius < ball_y < hoop_y and
    velocity_y > 0):

    combo += 1

    if combo >= 3:
        on_fire = True
        score += 2   # bonus points
    else:
        score += 1

    scored = True
    just_scored = True

  if scored:
    reset_timer += 1

    if reset_timer > 10:
      ball_x = 100
      ball_y = HEIGHT - ball_radius
      velocity_x = 0
      velocity_y = 0

      scored = False
      reset_timer = 0

  # Collision with ground
  if ball_y + ball_radius >= HEIGHT:
    ball_y = HEIGHT - ball_radius
    velocity_y = 0
    
    if not scored and not just_scored:
        ball_x = 100
        combo = 0
        on_fire = False
    
    just_scored = False
    


  # Side boundaries
  if ball_x - ball_radius < 0:
    ball_x = ball_radius
  if ball_x + ball_radius > WIDTH:
    ball_x = WIDTH - ball_radius

  if ball_y - ball_radius < 0:
    ball_y = ball_radius

  screen.fill((30,30,30))
  
  if on_fire:
    pygame.draw.circle(screen, (255, 100, 0), (ball_x, ball_y), ball_radius + 5)
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius)
  else:
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius)

  hoop_x += hoop_speed * hoop_direction
  if (hoop_x <= 400 or hoop_x + hoop_width >= WIDTH - 100):
    hoop_direction *= -1
  
  pygame.draw.ellipse(screen, (200, 100, 0), (hoop_x, hoop_y, hoop_width, 20), 3)
  pygame.draw.ellipse(screen, (255, 165, 0), (hoop_x, hoop_y + 4, hoop_width, 20), 3)

  score_text = font.render(f"Score: {score}", True, (255, 255, 255))
  screen.blit(score_text, (10, 10))
  combo_text = font.render(f"Combo: {combo}", True, (255, 255, 255))
  screen.blit(combo_text, (400, 10))
  pygame.draw.rect(screen, (100, 100, 100),  (10, 50, 200 , 10))
  pygame.draw.rect(screen, (0, 255, 0), (10, 50, power * 8, 10))
  pygame.display.update()
  clock.tick(60)