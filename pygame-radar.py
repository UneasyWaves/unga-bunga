import pygame

pygame.init

background_colour = (115,50,65)

# appears when user attempts something character is unable to do in specific situations/actions
unexecutable_char_action = ("I can't do that")

(width, height) = (900, 700)

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Unga Bunga')

screen.fill(background_colour)

pygame.display.flip()

#set frame rate
clock = pygame.time.Clock()
FPS = 60



class Radar1(pygame.sprite.Sprite):
  def __init__(self, x2, y2, scale2, speed):
    pygame.sprite.Sprite.__init__(self)
    self.speed = speed
    radarimg = pygame.image.load('libresprite stuff/greenradar.png')
    self.radarimg = pygame.transform.scale(radarimg, (radarimg.get_width() * scale2, radarimg.get_height() * scale2))
    self.rect = self.radarimg.get_rect()
    self.rect.center = (x2, y2)

  def move(self):
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
      self.rect.x -= 5
    elif key[pygame.K_d]:
      self.rect.x += 5
    elif key[pygame.K_w]:
      self.rect.y -= 5
    elif key[pygame.K_s]:
      self.rect.y += 5

  def draw(self):
    screen.blit(self.radarimg, self.rect)






class Mountain1(pygame.sprite.Sprite):
  def __init__(self, x1, y1, scale):
    pygame.sprite.Sprite.__init__(self)
    background_img = pygame.image.load('libresprite stuff/mountain-beach-water.png')
    self.background_img = pygame.transform.scale(background_img, (int(background_img.get_width() * scale), int(background_img.get_height() * scale)))
    self.background_rect = self.background_img.get_rect()
    self.background_rect.center = (x1, y1)
  
  def draw(self):
    screen.blit(self.background_img, self.background_rect)




#mountain background peramteres ect
Mountain_map = Mountain1(420, 800, 2.5)
  
Player = Radar1 (200, 200, 0.4, 5)

running = True
while running:
 
  clock.tick(FPS)

  screen.fill(background_colour)
 
  Player.move()
  Mountain_map.draw()
  Player.draw()
 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    

  pygame.display.update()

pygame.quit()
