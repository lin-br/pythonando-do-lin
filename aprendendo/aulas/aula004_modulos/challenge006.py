"""
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3
"""
import pygame

pygame.init()
pygame.mixer.music.load('MarioPowerUp.mp3')
pygame.mixer.music.play()
pygame.event.wait()
