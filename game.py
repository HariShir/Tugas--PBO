import os
os.system("cls")
import pygame

# instalasi
pygame.init()

# mengatur ukuran layar/screen

height = 600
width = 600

screen = pygame.display.set_mode([height,width])

# mengubah warna screen
screen.fill((200,30,5))

# buat lingkaran
pygame.draw.circle(screen, (0,0,255), (300,300), 100)

# agar screen tampil terus (tidak langung close/menghilang)
running = True
while running:
  # loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  pygame.display.update()

pygame.quit()