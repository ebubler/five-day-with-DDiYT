import pygame
from pygame import VIDEORESIZE, RESIZABLE
import json
import random
import datetime


class Main:
    def __init__(self):
        self.config_name = 'data/config.json'
        self.camera_routes = {
            "ВХОД 1": ["ЭТАЖ 1"],
            "ВХОД 2": ["ЭТАЖ 1"],
            "ЭТАЖ 1": ["ВХОД 1", "ВХОД 2", "ЭТАЖ 2"],
            "ЭТАЖ 2": ["ЛЕСТНИЦА", "ЭТАЖ 2-1"],
            "ЛЕСТНИЦА": ["КАБИНЕТ"],
            "ЭТАЖ 2-1": ["ЭТАЖ 2", "ЭТАЖ 3"],
            "ЭТАЖ 3": ["КАБИНЕТ"],
            "КАБИНЕТ": []  # Финальная позиция
        }
        # Текущая камера
        self.current_camera = "ВХОД 1"

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

    def telegram(self):
        screen.fill('data/image/гоша_тг/Начало.png')

    def move_to_camera(self, target_camera):
        """Перемещение на указанную камеру."""
        if target_camera in self.camera_routes[self.current_camera]:
            self.current_camera = target_camera
            return f"Перешли на {target_camera}"
        else:
            return f"Нельзя перейти с {self.current_camera} на {target_camera}"

    def random_move(self):
        """Случайное перемещение в одну из доступных камер."""
        routes = self.camera_routes[self.current_camera]
        if routes:
            self.current_camera = random.choice(routes)
            return f"Случайно переместились на {self.current_camera}"
        else:
            return f"Нет доступных переходов из {self.current_camera}"

    def available_routes(self):
        """Получение списка доступных маршрутов из текущей камеры."""
        return self.camera_routes[self.current_camera]

    def mainGame(self, screen):
        game_level = self.load_config()['settings']['game']
        pygame.display.set_caption("День " + game_level)
        fps = 30
        win = False

        clock = pygame.time.Clock()

        backgrount = pygame.image.load('data/image/game/backbrount.png')
        backgrount = pygame.transform.smoothscale(backgrount, (int(self.width * 1.5), self.height))

        delta_x = 0

        pygame.mixer.init()
        pygame.mixer.music.load('data/song/menu/Гоша_меню.mp3')
        sigma = pygame.mixer.Sound('data/song/game/nosehonk.mp3')

        text_file = 'data/image/menu/minecraft.ttf'

        font = pygame.font.Font(text_file, int(self.height * 0.05))

        pygame.mixer.music.play()
        pygame.mixer.music.set_pos(1)
        mouse_pos = (228, 228)

        start_time = datetime.datetime.strptime("12:00", "%H:%M")
        end_time = datetime.datetime.strptime("18:00", "%H:%M")
        duration = end_time - start_time
        total_seconds = duration.total_seconds()

        camera = 0

        cam_trig = total_seconds

        cam = pygame.image.load('data/image/game/камеры.png')
        cam = pygame.transform.smoothscale(cam, (int(self.width * 0.219 * 1.5), int(self.height * 0.3)))
        cam1 = pygame.image.load('data/image/game/ВХОД 1.jpg')
        cam1 = pygame.transform.smoothscale(cam1, (int(self.width * 0.219 * 1.5), int(self.height * 0.3 * 0.95)))
        back = pygame.image.load('data/image/game/назад.png')
        back = pygame.transform.smoothscale(back, (cam.get_width() // 10, cam.get_height() // 8))

        sound_cam = pygame.mixer.Sound("data/song/game/camera-video-load.mp3")

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if int(self.height * 0.6952) <= event.pos[1] <= int(self.height * 0.708) and delta_x + int(self.width * 1.5 * 0.6986) <= event.pos[0] <= delta_x + int(self.width * 1.5 * 0.706):
                            sigma.play()
                        if not camera:
                            if delta_x + int(self.width * 0.162 * 1.5) <= mouse_pos[0] <= delta_x + int(
                                    self.width * 0.162 * 1.5) + cam.get_width() // 3 and int(self.height * 0.2731) <= \
                                    mouse_pos[1] <= int(self.height * 0.2731) + cam.get_height() // 2:
                                sound_cam.stop()
                                sound_cam.play()
                                camera = 'ВХОД 1'
                                cam = pygame.image.load(f'data/image/game/рабочий стол.png')
                                cam = pygame.transform.smoothscale(cam,
                                                                   (int(self.width * 0.219 * 1.5),
                                                                    int(self.height * 0.3)))
                            if delta_x + int(self.width * 0.162 * 1.5) + cam.get_width() // 3 <= mouse_pos[0] <= delta_x + int(
                                    self.width * 0.162 * 1.5) + (cam.get_width() // 3) * 2 and int(self.height * 0.2731) <= \
                                    mouse_pos[1] <= int(self.height * 0.2731) + cam.get_height() // 2:
                                sound_cam.stop()
                                sound_cam.play()
                                camera = 'ВХОД 2'
                                cam = pygame.image.load(f'data/image/game/рабочий стол.png')
                                cam = pygame.transform.smoothscale(cam,
                                                                   (int(self.width * 0.219 * 1.5),
                                                                    int(self.height * 0.3)))
                            if delta_x + int(self.width * 0.162 * 1.5) + cam.get_width() * 2 // 3 + 1 <= mouse_pos[0] <= delta_x + int(
                                    self.width * 0.162 * 1.5) + cam.get_width() and int(self.height * 0.2731) <= \
                                    mouse_pos[1] <= int(self.height * 0.2731) + cam.get_height() // 2:
                                sound_cam.stop()
                                sound_cam.play()
                                camera = 'лестница'
                                cam = pygame.image.load(f'data/image/game/рабочий стол.png')
                                cam = pygame.transform.smoothscale(cam,
                                                                   (int(self.width * 0.219 * 1.5),
                                                                    int(self.height * 0.3)))

                            if delta_x + int(self.width * 0.162 * 1.5) <= mouse_pos[0] <= delta_x + int(
                                    self.width * 0.162 * 1.5) + cam.get_width() // 3 and int(self.height * 0.2731) + cam.get_height() // 2 <= \
                                    mouse_pos[1] <= int(self.height * 0.2731) + cam.get_height():
                                sound_cam.stop()
                                sound_cam.play()
                                camera = 'ЭТАЖ 1'
                                cam = pygame.image.load(f'data/image/game/рабочий стол.png')
                                cam = pygame.transform.smoothscale(cam,
                                                                   (int(self.width * 0.219 * 1.5),
                                                                    int(self.height * 0.3)))
                            if delta_x + int(self.width * 0.162 * 1.5) + cam.get_width() // 3 <= mouse_pos[0] <= delta_x + int(
                                    self.width * 0.162 * 1.5) + (cam.get_width() // 3) * 2 and int(self.height * 0.2731) + cam.get_height() // 2 <= \
                                    mouse_pos[1] <= int(self.height * 0.2731) + cam.get_height():
                                sound_cam.stop()
                                sound_cam.play()
                                camera = 'ЭТАЖ 2'
                                cam = pygame.image.load(f'data/image/game/рабочий стол.png')
                                cam = pygame.transform.smoothscale(cam,
                                                                   (int(self.width * 0.219 * 1.5),
                                                                    int(self.height * 0.3)))
                            if delta_x + int(self.width * 0.162 * 1.5) + cam.get_width() * 2 // 3 + 1 <= mouse_pos[0] <= delta_x + int(
                                    self.width * 0.162 * 1.5) + cam.get_width() and int(self.height * 0.2731) + cam.get_height() // 2 <= \
                                    mouse_pos[1] <= int(self.height * 0.2731) + cam.get_height():
                                sound_cam.stop()
                                sound_cam.play()
                                camera = 'ЭТАЖ 3'
                                cam = pygame.image.load(f'data/image/game/рабочий стол.png')
                                cam = pygame.transform.smoothscale(cam,
                                                                   (int(self.width * 0.219 * 1.5),
                                                                    int(self.height * 0.3)))

                            if camera:
                                cam1 = pygame.image.load(f'data/image/game/{camera}.jpg')
                                cam1 = pygame.transform.smoothscale(cam1, (
                                int(self.width * 0.219 * 1.5), int(self.height * 0.3 * 0.95)))
                        else:
                            if delta_x + int(self.width * 0.162 * 1.5) <= mouse_pos[0] <= delta_x + int(
                                    self.width * 0.162 * 1.5) + cam.get_width() // 8 and int(self.height * 0.2731) <= \
                                    mouse_pos[1] <= int(self.height * 0.2731) + cam.get_height() // 8:
                                cam = pygame.image.load('data/image/game/камеры.png')
                                cam = pygame.transform.smoothscale(cam, (
                                int(self.width * 0.219 * 1.5), int(self.height * 0.3)))
                                camera = 0
                                sound_cam.stop()
                                sound_cam.play()
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

                    backgrount = pygame.image.load('data/image/game/backbrount.png')
                    backgrount = pygame.transform.smoothscale(backgrount, (int(self.width * 1.5), self.height))
                    font = pygame.font.Font(text_file, int(self.height * 0.05))

                    cam = pygame.image.load('data/image/game/камеры.png')
                    cam = pygame.transform.smoothscale(cam, (int(self.width * 0.219 * 1.5), int(self.height * 0.3)))
                    back = pygame.image.load('data/image/game/назад.png')
                    back = pygame.transform.smoothscale(back, (cam.get_width() // 10, cam.get_height() // 8))
                    if camera:
                        cam1 = pygame.image.load(f'data/image/game/{camera}.jpg')
                        cam1 = pygame.transform.smoothscale(cam1, (
                            int(self.width * 0.219 * 1.5), int(self.height * 0.3 * 0.95)))
                    camera = 0

            if int(self.width * 0.1) >= mouse_pos[0] > 0 >= delta_x:
                delta_x += int(self.width * 0.05)
            if not (0 >= delta_x):
                delta_x = 0
            if self.width - int(self.width * 0.1) <= mouse_pos[0] < self.width <= backgrount.get_rect()[-2] + delta_x:
                delta_x -= int(self.width * 0.05)
            if not (self.width <= backgrount.get_rect()[-2] + delta_x):
                delta_x = -backgrount.get_rect()[-2] + self.width

            screen.fill((0, 0, 0))

            current_time = end_time - datetime.timedelta(seconds=total_seconds)
            text_time = font.render(str(current_time.time()), True, (0, 0, 0))

            if not pygame.mixer.music.get_busy():
                print('включение трека')
                pygame.mixer.music.play()

            screen.blit(backgrount, (delta_x, 0, self.width, self.height))

            screen.blit(text_time, (self.width - int(self.width * 0.17), int(self.height * 0.05), int(self.width * 0.17), int(self.height * 0.1)))

            screen.blit(cam, (
            delta_x + int(self.width * 0.162 * 1.5), int(self.height * 0.2731), cam.get_width(), cam.get_height()))
            if camera:
                print('камера:', camera)
                screen.blit(cam1, (
            delta_x + int(self.width * 0.162 * 1.5), int(self.height * 0.2731), cam1.get_width(), cam1.get_height()))
                screen.blit(back, (delta_x + int(self.width * 0.162 * 1.5), int(self.height * 0.2731), back.get_width(), back.get_height()))

            pygame.display.flip()
            clock.tick(fps)

            if cam_trig == total_seconds:
                self.random_move()
                cam_trig -= 500
            print(self.current_camera)

            total_seconds -= 5
            if total_seconds <= 0:
                break
        return win

    def mainMenu(self, screen):
        pygame.display.set_caption("Меню")
        fps = 30

        game_level = self.load_config()['settings']['game']
        text_file = 'data/image/menu/minecraft.ttf'

        fps_gosha = 10
        pos_gosha = 0

        font = pygame.font.Font(text_file, int(self.width * 0.25 * 0.1))
        font1 = pygame.font.Font(text_file, int(self.width * 0.25 * 0.1))
        font2 = pygame.font.Font(text_file, int(self.width * 0.25 * 0.05))
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
                            running1 = 1
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

                    font = pygame.font.Font(text_file, int(self.width * 0.25 * 0.1))
                    font1 = pygame.font.Font(text_file, int(self.width * 0.25 * 0.1))
                    font2 = pygame.font.Font(text_file, int(self.width * 0.25 * 0.05))
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
                f'data/image/menu/animate/Untitled_{"0" * (6 - len(str(int(pos_gosha)))) + str(int(pos_gosha))}.png')
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

    running = game.mainMenu(screen)

    while running:
        level = game.load_config()['settings']['game']
        if running == 1:
            win = game.mainGame(screen)
            running = game.mainMenu(screen)
