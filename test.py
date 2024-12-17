import pygame
from pygame import VIDEORESIZE, RESIZABLE

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг')
    width = 800
    height = 400
    size = width, height
    screen = pygame.display.set_mode(size, RESIZABLE)
    mask = pygame.Surface((width, height), pygame.SRCALPHA)

    running = True
    x = width // 2
    y = height // 2
    v = 100
    fps = 30
    clock = pygame.time.Clock()

    image = pygame.image.load('20241217_181745.jpg')
    image = pygame.transform.smoothscale(image, (
        int(width * 3.2), height
    ))

    xm, ym = 0, 0
    x1 = False
    x2 = False
    y1 = False
    y2 = False
    fire = False
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == VIDEORESIZE:
                width, height = event.size
                x = width // 2
                y = height // 2
                mask = pygame.Surface((width, height), pygame.SRCALPHA)
                screen = pygame.display.set_mode((width, height), RESIZABLE)

                image = pygame.image.load('20241217_181745.jpg')
                image = pygame.transform.smoothscale(image, (
                    int(width * 3.2), height
                ))
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(image.get_rect(center=(x, y)))
                fire = not fire
            if event.type == pygame.MOUSEMOTION:
                xm, ym = event.pos
                x1 = 5 <= event.pos[0] <= 30
                x2 = width - 30 <= event.pos[0] <= width - 5
                y1 = 5 <= event.pos[1] <= 30
                y2 = height - 30 <= event.pos[1] <= height - 5

        mask.fill((15, 5, 5))
        if fire:
            for i in range(20, -1, -1):

                pygame.draw.circle(mask, (220 - i * 10, 220 - i * 10, 220 - i * 10), (xm, ym), width // 9 + 2 * i)
        if x1:
            if image.get_rect(center=(x, y))[0] < -50:
                x += 50
        if x2:
            if image.get_rect(center=(x, y))[0] + image.get_rect(center=(x, y))[2] > width + 50:
                x -= 50

        if y1:
            if image.get_rect(center=(x, y))[1] < -50:
                y += 50
        if y2:
            if image.get_rect(center=(x, y))[1] + image.get_rect(center=(x, y))[3] > height:
                y -= 50

        screen.blit(image, image.get_rect(center=(x, y)))

        screen.blit(mask, (0, 0), special_flags=pygame.BLEND_MULT)

        clock.tick(fps)
        pygame.display.flip()


    pygame.quit()