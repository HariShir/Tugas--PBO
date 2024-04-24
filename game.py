import os
os.system("cls")
import pygame
# import sys

# instalasi
pygame.init()

# mengatur ukuran layar/screen

screen = pygame.display.set_mode([600, 600])

# mengubah warna screen
screen.fill(("#FDFFC2"))

# buat lingkaran
pygame.draw.circle(screen, ("red"), (300,300), 100)

# agar screen tampil terus (tidak langung close/menghilang)
running = True
while running:
  # loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  pygame.display.update()

pygame.quit()