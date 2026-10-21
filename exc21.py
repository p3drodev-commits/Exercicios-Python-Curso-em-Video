# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()

pygame.mixer.music.load('caminho/para/seu/arquivo.mp3')  # Substitua pelo caminho do seu arquivo MP3
pygame.mixer.music.play()