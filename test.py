import pygame
from pygame import VIDEORESIZE, RESIZABLE


def klaviatyra_minigame(width, height):
    screen = pygame.display.set_mode((width, height), RESIZABLE)
    mask = pygame.Surface((width, height), pygame.SRCALPHA)
    running = True
    x, y = width // 2, height // 2
    fps = 30
    clock = pygame.time.Clock()
    file_image = 'pxArt (3).png'
    image = pygame.image.load(file_image)
    image = pygame.transform.smoothscale(image, (int(width * 3.2), height))
    image2 = pygame.image.load(file_image)
    image2 = pygame.transform.smoothscale(image2, (int(width * 3.2), height))
    timyr = pygame.image.load('Тимур.png')
    timyr = pygame.transform.smoothscale(timyr, (width // 2, height))
    im = 12
    pos_anim = 0
    anim = True

    xm, ym = 0, 0
    x1, x2, y1, y2, fire = False, False, False, False, False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == VIDEORESIZE:
                width, height = event.size
                x, y = width // 2, height // 2
                mask = pygame.Surface((width, height), pygame.SRCALPHA)
                screen = pygame.display.set_mode((width, height), RESIZABLE)

                image = pygame.image.load(file_image)
                image = pygame.transform.smoothscale(image, (int(width * 3.2), height))
                image2 = pygame.image.load(file_image)
                image2 = pygame.transform.smoothscale(image2, (int(width * 3.2), height))

                timyr = pygame.image.load('Тимур.png')
                timyr = pygame.transform.smoothscale(timyr, (width // 1.5, height))

                image_width = image.get_width()
                x3, x4 = 0, image_width
            if event.type == pygame.MOUSEBUTTONDOWN:
                fire = not fire
            if event.type == pygame.MOUSEMOTION:
                xm, ym = event.pos
                x1 = 5 <= xm <= width // 10
                x2 = width - width // 10 <= xm <= width - 5
                y1 = 5 <= ym <= 30
                y2 = height - 30 <= ym <= height - 5

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

        if anim:
            if pos_anim > 83:
                pos_anim = 0
            image_anim = pygame.image.load(
                f'1/Untitled_{"".join(['0' for i in range(6 - len(str(int(pos_anim))))])}{int(pos_anim)}.png'
            )
            image_anim = pygame.transform.smoothscale(image_anim, (width // 4, height // 1.5))
        screen.blit(image_anim, image_anim.get_rect(center=(x - 100, y)))
        screen.blit(image_anim, image_anim.get_rect(center=(x - 100 - image.get_rect()[2], y)))
        screen.blit(timyr, timyr.get_rect(center=(x - image.get_rect()[2] - 1000, y)))
        screen.blit(timyr, timyr.get_rect(center=(x - 1000, y)))
        screen.blit(mask, (0, 0), special_flags=pygame.BLEND_MULT)
        pos_anim += im / fps
        clock.tick(fps)
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг')

    width, height = 800, 400
    screen = pygame.display.set_mode((width, height), RESIZABLE)
    mask = pygame.Surface((width, height), pygame.SRCALPHA)
    running = True

    klaviatyra_minigame(width, height)

    pygame.quit()
