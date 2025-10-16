#faça um programa que abra e reproduza audio de um arquivo mp3


import pygame
pygame.init()
pygame.mixer.music.load('desafio021.mp3')
pygame.mixer.music.play()
pygame.event.wait()


