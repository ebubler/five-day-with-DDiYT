import pygame
from pygame import VIDEORESIZE, RESIZABLE
from pygamevideo import Video


def klaviatyra_minigame(width, height):
    screen = pygame.display.set_mode((width, height), RESIZABLE)
    mask = pygame.Surface((width, height), pygame.SRCALPHA)


    x, y = width // 2, height // 2
    fps = 30
    clock = pygame.time.Clock()

    file_image = '1.png'

    video = Video("Гоша_меню.mp4")

    image = pygame.image.load(file_image)
    image = pygame.transform.smoothscale(image, (int(width * 3.2), height))

    image2 = pygame.image.load(file_image)
    image2 = pygame.transform.smoothscale(image2, (int(width * 3.2), height))

    gocha = pygame.image.load('Гоша.png')
    gocha = pygame.transform.smoothscale(gocha, (width // 2, height // 2))

    scream_anim = [pygame.image.load('скример_гоши/скример_гоши1.png'),
                   pygame.image.load('скример_гоши/скример_гоши2.png'),
                   pygame.image.load('скример_гоши/скример_гоши3.png'),
                   pygame.image.load('скример_гоши/скример_гоши4.png'),
                   pygame.image.load('скример_гоши/скример_гоши5.png'),
                   pygame.image.load('скример_гоши/скример_гоши6.png'),
                   pygame.image.load('скример_гоши/скример_гоши7.png'),
                   pygame.image.load('скример_гоши/скример_гоши8.png'),
                   pygame.image.load('скример_гоши/скример_гоши9.png'),
                   pygame.image.load('скример_гоши/скример_гоши10.png')]

    xm, ym = 0, 0
    x1, x2, y1, y2, fire = False, False, False, False, False

    scream = pygame.mixer.Sound("Звук_скримера.mp3")


    play = True
    life = True
    end = False
    menu = True
    running = False
    while play:
        im = 12
        pos_anim = 0




        start_time = pygame.time.get_ticks()

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    play = False
                if event.type == VIDEORESIZE:
                    width, height = event.size
                    x, y = width // 2, height // 2
                    mask = pygame.Surface((width, height), pygame.SRCALPHA)
                    screen = pygame.display.set_mode((width, height), RESIZABLE)

                    image = pygame.image.load(file_image)
                    image = pygame.transform.smoothscale(image, (int(width * 3.2), height))
                    image2 = pygame.image.load(file_image)
                    image2 = pygame.transform.smoothscale(image2, (int(width * 3.2), height))

                    gocha = pygame.image.load('Гоша.png')
                    gocha = pygame.transform.smoothscale(gocha, (width // 2, height // 2))

                if event.type == pygame.MOUSEMOTION:
                    xm, ym = event.pos
                    x1 = 5 <= xm <= width // 10
                    x2 = width - width // 10 <= xm <= width - 5
                    y1 = 5 <= ym <= 30
                    y2 = height - 30 <= ym <= height - 5

            elapsed_time = pygame.time.get_ticks() - start_time
            if elapsed_time >= 5000 and life:
                screen.fill((0, 0, 0))
                scream.play()
                for i in range(10):
                    screen.blit(scream_anim[i], (0, 0))# Через 5 секунд
                    pygame.display.flip()
                    pygame.time.delay(100)
                    screen.fill((0, 0, 0))
                    continue
                life = False
                running = False
                end = True

            mask.fill((15, 5, 5))
            if fire:
                for i in range(20, -1, -1):
                    pygame.draw.circle(mask, (220 - i * 10, 220 - i * 10, 220 - i * 10), (xm, ym), width // 9 + 2 * i)

            if x1:
                x += 50
            if x2:
                x -= 50

            if y1 and image.get_rect(center=(x, y))[1] < -50:
                y += 50
            if y2 and image.get_rect(center=(x, y))[1] + image.get_rect(center=(x, y))[3] > height:
                y -= 50

            if image.get_rect(center=(x - image.get_rect()[2], y))[0] >= 0:
                x -= image.get_rect()[2]

            if image.get_rect(center=(x, y))[0] + image.get_rect(center=(x, y))[2] <= width:
                x += image.get_rect()[2]

            screen.blit(image, image.get_rect(center=(x, y)))
            screen.blit(image2, image2.get_rect(center=(x - image.get_rect()[2], y)))

            screen.blit(gocha, gocha.get_rect(center=(x - image.get_rect()[2] - 240, y)))
            screen.blit(gocha, gocha.get_rect(center=(x - 240, y)))

            pos_anim += im / fps
            clock.tick(fps)
            pygame.display.flip()

        while end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = False
                    play = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if continue_button.collidepoint(event.pos):
                        end = False
                        running = True
                        start_time = pygame.time.get_ticks()  # Перезапуск времени отсчёта
                        life = True

                    if quit_button.collidepoint(event.pos):
                        end = False
                        play = False

            screen.fill((0, 0, 0))
            font = pygame.font.SysFont(None, 50)
            img = font.render('Гоша смог', True, (23, 54, 65))
            screen.blit(img, (280, 50))

            continue_button = pygame.Rect(width // 3, height // 2 - 60, width // 3, 50)
            quit_button = pygame.Rect(width // 3, height // 2 + 20, width // 3, 50)

            pygame.draw.rect(screen, (0, 255, 0), continue_button)
            pygame.draw.rect(screen, (255, 0, 0), quit_button)

            continue_text = font.render("Я сигма, я смогу", True, (0, 0, 0))
            quit_text = font.render("Уйти с позором", True, (0, 0, 0))

            screen.blit(continue_text, (continue_button.x + 10, continue_button.y + 10))
            screen.blit(quit_text, (quit_button.x + 10, quit_button.y + 10))

            pygame.display.flip()

        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu = False
                    play = False
            screen.fill((0, 0, 0))

            video.play()


            video.draw_to(screen, (500, 0))

            continue_button = pygame.Rect(width // 3, height // 2 - 60, width // 3, 50)
            pygame.display.flip()






if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг')

    width, height = 800, 400
    screen = pygame.display.set_mode((width, height), RESIZABLE)
    mask = pygame.Surface((width, height), pygame.SRCALPHA)

    klaviatyra_minigame(width, height)

    pygame.quit()