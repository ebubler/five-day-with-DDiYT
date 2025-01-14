import pygame
import pygame_widgets
from pygame_widgets.button import Button
import random
import time

# Я плакал
camera_routes = {
    1: [2, 3],
    2: [1, 4, 8],
    3: [1, 5],
    4: [8, 2, 5, 6],
    5: [9, 4, 3, 10],
    6: [10],
    7: [5, 9],
    8: [4, 6],
    9: [10, 5, 7],
    10: [9, 6]
}

# Камеры, к которым существо неохотно двигается
end_cams = [6, 9]

# Цвета камер
camera_colors = [
    (225, 255, 0), (225, 0, 225), (0, 225, 255), (225, 122, 0), (225, 0, 122),
    (50, 50, 50), (112, 255, 0), (122, 0, 225), (0, 225, 132), (155, 33, 0)
]

# Глобальные переменные
last_move_time = time.time()
move_delay = random.uniform(3, 5)
entity_camera = 0
entity_position = (320, 210)  # Фиксированная позиция существа
current_camera_view = -1
in_main_menu = True
image = pygame.image.load('аааа.png')

# Pygame и экран
pygame.init()
width, height = 700, 600
screen = pygame.display.set_mode((width, height))

# Универсальная функция для создания кнопок
camera_buttons_list = []
exit_button = None

def create_camera_buttons():
    global camera_buttons_list, exit_button
    positions = [
        (300, 30), (230, 30), (380, 30), (250, 80), (340, 80),
        (170, 190), (400, 130), (160, 90), (320, 150), (240, 150)
    ]
    camera_buttons_list = [
        Button(screen, x, y, 60, 30, inactiveColour=(50, 50, 50), text=f'Cam_{i+1}',
               onClick=lambda cam=i: change_camera(cam))
        for i, (x, y) in enumerate(positions)
    ]
    exit_button = Button(screen, 550, 500, 100, 50, inactiveColour=(200, 0, 0), text='Меню', onClick=main_menu)
    hide_all_buttons()

def hide_all_buttons():
    """Скрыть все кнопки."""
    for button in camera_buttons_list:
        button.hide()
    if exit_button:
        exit_button.hide()

def show_camera_buttons():
    """Показать кнопки камер и кнопку выхода."""
    for button in camera_buttons_list:
        button.show()
    if exit_button:
        exit_button.show()

# Отображение камеры
def change_camera(cam):
    """Отображает интерфейс камеры."""
    global current_camera_view, in_main_menu, main_menu_button
    main_menu_button.hide()

    if current_camera_view == cam and not in_main_menu:
        return

    current_camera_view = cam
    in_main_menu = False
    screen.fill(camera_colors[cam])
    hide_all_buttons()
    show_camera_buttons()

    # Если монстр находится на текущей камере, отрисовать его
    if entity_camera is not None and cam == entity_camera:
        screen.blit(image, entity_position)

    pygame.display.update()


def main_menu():
    """Отображает главное меню."""
    global in_main_menu
    screen.fill((0, 0, 0))
    hide_all_buttons()
    main_menu_button.show()
    in_main_menu = True
    pygame.display.update()

# Движение существа
def move_entity():
    """Двигает существо между камерами."""
    global entity_camera, move_delay, last_move_time

    # Проверяем, прошло ли достаточно времени для следующего перемещения
    if time.time() - last_move_time < move_delay or in_main_menu:
        return

    # Получаем доступные маршруты для текущей камеры
    current_routes = camera_routes.get(entity_camera + 1, [])
    if not current_routes:
        return

    # Рассчитываем вероятности для маршрутов
    probabilities = [
        0.3 if cam in end_cams else 1.0 for cam in current_routes
    ]
    total = sum(probabilities)
    probabilities = [p / total for p in probabilities]

    # Выбираем следующую камеру
    next_camera = random.choices(current_routes, probabilities)[0]
    entity_camera = next_camera - 1  # Обновляем текущую камеру

    # Обновляем задержку перед следующим перемещением
    move_delay = random.uniform(3, 5)
    last_move_time = time.time()
    pygame.display.update()



# Основной игровой цикл
main_menu_button = Button(screen, 300, 300, 200, 100, inactiveColour=(30, 30, 30), text='Камеры', onClick=lambda: change_camera(0))
create_camera_buttons()
running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            quit()

    move_entity()
    pygame_widgets.update(events)
    pygame.display.flip()
