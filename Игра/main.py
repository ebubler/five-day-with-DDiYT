import pygame
from pygame import VIDEORESIZE, RESIZABLE
import json


class Main:
    def __init__(self):
        self.config_name = 'data/config.json'

    def load_config(self):
        print('загрузка конфига')
        with open(self.config_name, 'r') as file:
            return json.load(file)

    def save_config(self, config):
        print('сохранение конфига')
        with open(self.config_name, 'w') as file:
            json.dump(config, file, indent=4)

    def setSize(self, size):
        self.width, self.height = size
        config = self.load_config()
        config['settings']['size'] = [size[0], size[1]]
        self.save_config(config)

    def mainGame(self, screen):
        game_level = self.load_config()['settings']['game']
        pygame.display.set_caption("День " + game_level)
        fps = 30
        win = False

        clock = pygame.time.Clock()

        pygame.mixer.init()
        pygame.mixer.music.load('data/song/menu/Гоша_меню.mp3')

        pygame.mixer.music.play()
        pygame.mixer.music.set_pos(1)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == VIDEORESIZE:
                    width, height = event.size
                    if height < 500:
                        height = 500
                    if width < 500:
                        width = 500
                    if height > width:
                        height = width
                    game.setSize((width, height))
                    screen = pygame.display.set_mode((width, height), RESIZABLE)

            screen.fill((0, 0, 0))

            if not pygame.mixer.music.get_busy():
                print('включение трека')
                pygame.mixer.music.play()

            pygame.display.flip()
            clock.tick(fps)
        return win

    def mainMenu(self, screen):
        pygame.display.set_caption("Меню")
        fps = 30

        game_level = self.load_config()['settings']['game']

        fps_gosha = 10
        pos_gosha = 0

        font = pygame.font.Font(None, int(self.width * 0.25 * 0.2))
        font1 = pygame.font.Font(None, int(self.width * 0.25 * 0.15))
        font2 = pygame.font.Font(None, int(self.width * 0.25 * 0.12))
        text_new_game = font.render('Новая игра', True, (255, 255, 255))
        text_cont = font1.render('Продолжить', True, (255, 255, 255))
        text_game = font2.render('День ' + game_level, True, (255, 255, 255))
        text_settings = font.render('Настройки', True, (255, 255, 255))

        clock = pygame.time.Clock()

        pygame.mixer.init()
        pygame.mixer.music.load('data/song/menu/Гоша_меню.ogg')

        but_size = (int(self.width * 0.25), int(self.height * 0.1))
        backgrount = pygame.image.load('data/image/menu/backgrount.png')
        backgrount = pygame.transform.smoothscale(backgrount, (self.width, self.height))

        name_game = pygame.image.load('data/image/menu/namegame.png')
        name_game = pygame.transform.smoothscale(name_game, (int(self.width * 0.35), int(self.height * 0.15)))

        but_new_game = pygame.image.load('data/image/menu/button.png')
        but_new_game = pygame.transform.smoothscale(but_new_game, but_size)
        pygame.mixer.music.play()
        pygame.mixer.music.set_pos(1)

        running = True
        running1 = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running1 = False
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if int(self.width * 0.1) <= event.pos[0] <= int(self.width * 0.1) + but_size[0] and int(self.height * 0.55) <= event.pos[1] <= int(self.height * 0.55) + but_size[1]:
                            running = False
                if event.type == VIDEORESIZE:
                    width, height = event.size
                    if height < 500:
                        height = 500
                    if width < 500:
                        width = 500
                    if height > width:
                        height = width
                    game.setSize((width, height))
                    screen = pygame.display.set_mode((width, height), RESIZABLE)

                    but_size = (int(self.width * 0.25), int(self.height * 0.1))
                    backgrount = pygame.image.load('data/image/menu/backgrount.png')
                    backgrount = pygame.transform.smoothscale(backgrount, (self.width, self.height))

                    name_game = pygame.image.load('data/image/menu/namegame.png')
                    name_game = pygame.transform.smoothscale(name_game,
                                                             (int(self.width * 0.35), int(self.height * 0.15)))

                    but_new_game = pygame.image.load('data/image/menu/button.png')
                    but_new_game = pygame.transform.smoothscale(but_new_game, but_size)

                    font = pygame.font.Font(None, int(self.width * 0.25 * 0.2))
                    font1 = pygame.font.Font(None, int(self.width * 0.25 * 0.15))
                    font2 = pygame.font.Font(None, int(self.width * 0.25 * 0.12))
                    text_new_game = font.render('Новая игра', True, (255, 255, 255))
                    text_cont = font1.render('Продолжить', True, (255, 255, 255))
                    text_game = font2.render('День ' + game_level, True, (255, 255, 255))
                    text_settings = font.render('Настройки', True, (255, 255, 255))

            screen.fill((0, 0, 0))

            if not pygame.mixer.music.get_busy():
                print('включение трека')
                pygame.mixer.music.play()

            if pos_gosha > 49:
                pos_gosha = 0
            screen.blit(backgrount, (0, 0, self.width, self.height))

            gosha = pygame.image.load(
                f'data/image/menu/animate/Untitled_{'0' * (6 - len(str(int(pos_gosha)))) + str(int(pos_gosha))}.png')
            gosha = pygame.transform.smoothscale(gosha, (int(self.width * 0.8), int(self.height * 1.1)))
            screen.blit(gosha, (int(self.width * 0.25), 0, self.width, self.height))
            pos_gosha += fps_gosha / fps

            screen.blit(name_game, (int(self.width * 0.05), int(self.height * 0.1), int(self.width * 0.35), int(self.height * 0.15)))

            screen.blit(but_new_game, (int(self.width * 0.1), int(self.height * 0.4), but_size[0], but_size[1]))
            screen.blit(but_new_game, (int(self.width * 0.1), int(self.height * 0.55), but_size[0], but_size[1]))
            screen.blit(but_new_game, (int(self.width * 0.1), int(self.height * 0.70), but_size[0], but_size[1]))

            screen.blit(text_new_game, text_new_game.get_rect(center=(int(self.width * 0.1) + but_size[0] // 2, int(self.height * 0.4) + but_size[1] // 2)))
            screen.blit(text_settings, text_new_game.get_rect(center=(int(self.width * 0.1) + but_size[0] // 2, int(self.height * 0.7) + but_size[1] // 2)))
            screen.blit(text_cont, text_cont.get_rect(center=(int(self.width * 0.1) + but_size[0] // 2, int(self.height * 0.56) + but_size[1] // 4)))
            screen.blit(text_game, text_game.get_rect(center=(int(self.width * 0.1) + but_size[0] // 2, int(self.height * 0.55) + but_size[1] // 1.25)))

            pygame.display.flip()
            clock.tick(fps)
        return running1


if __name__ == '__main__':
    pygame.init()

    game = Main()
    size = game.load_config()['settings']['size']
    screen = pygame.display.set_mode(size, RESIZABLE)

    game.setSize(size)

    game.mainMenu(screen)
    running = True
    while running:
        level = game.load_config()['settings']['game']
        if level == '1':
            win = game.mainGame(screen)
            running = game.mainMenu(screen)
