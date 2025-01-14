import pygame
import sys

# Инициализация Pygame
pygame.init()
pygame.mixer.init()
tg_zvyk = pygame.mixer.Sound("тг_звук.mp3")

timer_duration = 2000
start_time = pygame.time.get_ticks()

image = pygame.image.load('тг_гоша/Начало.png')
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen.blit(image, (0, 0))
pygame.display.flip()

ok_Gocha = pygame.image.load('тг_гоша/ок.png')
no_Gocha = pygame.image.load('тг_гоша/нет.png')

# Получение размеров кнопок и их позиций
ok_rect = ok_Gocha.get_rect(topleft=(700, 950))
no_rect = no_Gocha.get_rect(topleft=(900, 950))

run = True
qw = True
vubor = True
vubor_ok = None

while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # Проверка нажатия на кнопку ok_Gocha
            if ok_rect.collidepoint(mouse_pos):
                image = pygame.image.load('тг_гоша/написал_ок.png')
                vubor = False
                vubor_ok = True
                screen.blit(image, (0, 0))
                pygame.display.flip()
                # Обновление таймера для задержки
                start_time = pygame.time.get_ticks()

            if no_rect.collidepoint(mouse_pos):
                image = pygame.image.load('тг_гоша/написал_нет.png')
                vubor = False
                vubor_ok = False
                screen.blit(image, (0, 0))
                pygame.display.flip()
                # Обновление таймера для задержки
                start_time = pygame.time.get_ticks()



    current_time = pygame.time.get_ticks()
    if current_time - start_time >= timer_duration and qw:
        image = pygame.image.load('тг_гоша/пишет.png')
        screen.blit(image, (0, 0))
        tg_zvyk.play()
        qw = False
        pygame.display.flip()

    if vubor_ok  and current_time - start_time >= timer_duration:
        image = pygame.image.load('тг_гоша/скинул.png')
        screen.blit(image, (0, 0))
        tg_zvyk.play()
        pygame.display.flip()
        vubor_ok = None

    if vubor_ok == False and current_time - start_time >= timer_duration:
        image = pygame.image.load('тг_гоша/злой.png')
        screen.blit(image, (0, 0))
        tg_zvyk.play()
        pygame.display.flip()
        vubor_ok = None


    if qw == False and vubor:
        screen.blit(ok_Gocha, ok_rect.topleft)
        screen.blit(no_Gocha, no_rect.topleft)
        pygame.display.flip()
