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

# Створення вікна гри
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Меню гри")

# Функція, яка запускає основну програму гри
def start_game():
    # Закриваємо поточне вікно
    pygame.quit()

    # Запускаємо my_app.py
    os.system("python my_app.py")

# Функція для відображення тексту на екрані
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

# Шрифти
font = pygame.font.Font(None, 36)
button_font = pygame.font.Font(None, 48)

# Колір кнопки
button_color = (255, 0, 0)  # Червоний

# Розміри кнопки
button_width = 200
button_height = 100

# Початкові координати кнопки
button_x = (window_width - button_width) // 2
button_y = (window_height - button_height) // 2

# Головний цикл меню
menu_running = True
while menu_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button_x <= mouse_pos[0] <= button_x + button_width and button_y <= mouse_pos[1] <= button_y + button_height:
                start_game()
                menu_running = False

    window.fill(background_color)

    # Малюємо кнопку
    pygame.draw.rect(window, button_color, (button_x, button_y, button_width, button_height))

    # Відображаємо текст на кнопці
    draw_text("Start", button_font, (255, 255, 255), window, button_x + 50, button_y + 30)

    pygame.display.update()
