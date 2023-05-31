import pygame

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
square_x = window_width - square_size
square_y = 0

# Швидкість руху квадрата
velocity = 5

# Розміри та координати стін
wall_width = 620
wall_height = 255
wall1_x = 400
wall1_y = 40
wall2_x = 20
wall2_y = 100
wall3_x = 1
wall3_y = 370
wall4_x = 90
wall4_y = 100
wall5_x = 650
wall5_y = 280

# Розміри та координати кубика
cube_size = 40
cube_x = window_width - cube_size
cube_y = 0

# Завантаження зображення
image = pygame.image.load("ttt.jpg")
image_width = image.get_width()
image_height = image.get_height()

# Створення вікна гри
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Керування квадратом зі стінами")

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

    # Малювання квадрата
    pygame.draw.rect(window, (255, 0, 0), (square_x, square_y, square_size, square_size))

    # Малювання стін
    pygame.draw.rect(window, (0, 0, 0), (wall1_x, wall1_y, wall_width, wall_height))
    pygame.draw.rect(window, (0, 0, 0), (wall2_x, wall2_y, wall_width, wall_height))
    pygame.draw.rect(window, (0, 0, 0), (wall3_x, wall3_y, wall_width, wall_height))
    pygame.draw.rect(window, (0, 0, 0), (wall4_x, wall4_y, wall_width, wall_height))
    pygame.draw.rect(window, (0, 0, 0), (wall5_x, wall5_y, wall_width, wall_height))

    # Малювання кубика
    pygame.draw.rect(window, (255, 0, 0), (cube_x, cube_y, cube_size, cube_size))

    # Перевірка зіткнення квадрата зі стіною
    if square_x <= wall1_x + wall_width and square_x + square_size >= wall1_x and square_y <= wall1_y + wall_height and square_y + square_size >= wall1_y:
        # Відображення зображення
        window.blit(image, (0, 0))

    # Оновлення вікна
    pygame.display.update()

# Завершення гри
pygame.quit()
