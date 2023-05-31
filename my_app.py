import pygame
import sys
import os

# Ініціалізація Pygame
pygame.init()

# Розміри вікна
window_width = 800
window_height = 600

# Колір екрану
background_color = (9, 255, 255)  # Білий

# Розміри квадрата
square_size = 5

# Початкові координати квадрата
square_x = (window_width - square_size) // 2
square_y = (window_height - square_size) // 2

# Розміри стін
wall_width = 1200
wall_height = 250

# Початкові координати стін
wall1_x = (window_width - 3 * wall_width) // 5
wall2_x = (window_width - 3 * wall_width) // 5
wall3_x = (window_width + wall_width) // 11
wall4_x = (window_width + 3 * wall_width) // 6
wall1_y = (window_height - wall_height) // 4
wall2_y = (window_height - wall_height) // 8
wall3_y = (window_height - wall_height) // 1
wall4_y = (window_height - wall_height) // 5

# Розміри об'єкта
object_width = 50
object_height = 50
object_x = (window_width - object_width) // 1000
object_y = (window_height - object_height) // 1

# Швидкість руху квадрата
velocity = 5

# Прапорці для зіткнення зі стінами та об'єктом
collision_flag1 = False
collision_flag2 = False
collision_flag3 = False
collision_flag4 = False
object_collision = False

# Завантаження зображень
image = pygame.image.load('uuuuu.jpg')
image_width = 700
image_height = 500
image_x = (window_width - image_width) // 2
image_y = (window_height - image_height) // 2

# Створення вікна гри
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Страшний лабіринт")

# Функція для оновлення рівня гри
def update_level():
    global level, wall1_x, wall2_x, wall3_x, wall4_x, wall1_y, wall2_y, wall3_y, wall4_y, object_x, object_y
    level += 1
    
    # Оновлення розташування стін та об'єкта для нового рівня
    wall1_x = (window_width - 3 * wall_width) // 3
    wall2_x = (window_width - 3 * wall_width) // 5
    wall3_x = (window_width + wall_width) // 11
    wall4_x = (window_width + 3 * wall_width) // 6
    wall1_y = (window_height - wall_height) // 4
    wall2_y = (window_height - wall_height) // 8
    wall3_y = (window_height - wall_height) // 1
    wall4_y = (window_height - wall_height) // 3
    object_x = (window_width - object_width) // 2
    object_y = (window_height - object_height) // 2

# Головний цикл гри
running = True
while running:
    # Оновлення екрану
    window.fill(background_color)

    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отримання позиції миші
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Рух квадрата до позиції миші
    if square_x < mouse_x:
        square_x += velocity
    if square_x > mouse_x:
        square_x -= velocity
    if square_y < mouse_y:
        square_y += velocity
    if square_y > mouse_y:
        square_y -= velocity

    # Перевірка колізії куба зі стінами
    if square_x < wall1_x + wall_width and square_x + square_size > wall1_x:
        if square_y < wall1_y + wall_height and square_y + square_size > wall1_y:
            # Зіткнення з першою стіною
            collision_flag1 = True
        else:
            collision_flag1 = False

    if square_x < wall2_x + wall_width and square_x + square_size > wall2_x:
        if square_y < wall2_y + wall_height and square_y + square_size > wall2_y:
            # Зіткнення з другою стіною
            collision_flag2 = True
        else:
            collision_flag2 = False

    if square_x < wall3_x + wall_width and square_x + square_size > wall3_x:
        if square_y < wall3_y + wall_height and square_y + square_size > wall3_y:
            # Зіткнення з третьою стіною
            collision_flag3 = True
        else:
            collision_flag3 = False

    if square_x < wall4_x + wall_width and square_x + square_size > wall4_x:
        if square_y < wall4_y + wall_height and square_y + square_size > wall4_y:
            # Зіткнення з четвертою стіною
            collision_flag4 = True
        else:
            collision_flag4 = False

    # Перевірка колізії куба з об'єктом
    if square_x < object_x + object_width and square_x + square_size > object_x:
        if square_y < object_y + object_height and square_y + square_size > object_y:
            # Зіткнення з об'єктом
            object_collision = True
        else:
            object_collision = False

    # Малювання стін
    pygame.draw.rect(window, (0, 0, 0), (wall1_x, wall1_y, wall_width, wall_height))
    pygame.draw.rect(window, (0, 0, 0), (wall2_x, wall2_y, wall_width, wall_height))
    pygame.draw.rect(window, (0, 0, 0), (wall3_x, wall3_y, wall_width, wall_height))
    pygame.draw.rect(window, (0, 0, 0), (wall4_x, wall4_y, wall_width, wall_height))

    # Малювання квадрата
    pygame.draw.rect(window, (255, 0, 0), (square_x, square_y, square_size, square_size))

    # Малювання об'єкта
    pygame.draw.rect(window, (255, 0, 0), (object_x, object_y, object_width, object_height))

    # Відображення фото при зіткненні квадрата зі стіною
    if collision_flag1 or collision_flag2 or collision_flag3 or collision_flag4:
        window.blit(image, (image_x, image_y))

    # Перехід на другий рівень при зіткненні куба з об'єктом
    if object_collision:
        os.system('second_win.py')
        running = False

    # Оновлення екрану
    pygame.display.update()

# Завершення гри
pygame.quit()
sys.exit()






