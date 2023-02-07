import pygame  # импортируем основной модуль pygame (в терминале установите предварительно pygame - pip install pygame)
import sys

pygame.init()  # импорт и запуск всех  расширений pygame

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
OUR_COLOR = (150, 0, 255)
OUR_COLOR_2 = (170, 170, 170)
# Задаем размеры поля
WIDTH = 680
HEIGHT = 680
window_of_view = pygame.display.set_mode((WIDTH, HEIGHT))
number_of_squares = 3  # Размерность поля
distance = 20  # расстояние между квадратами
square_size = 200  # размер каждого квадрата

# Создаем список из 0 по числу строчек и столбцов игрового поля
list_of_the_numbers = list([0, 0, 0] for i in range(3))
print(list_of_the_numbers)

# Формируем список с координатами каждого квадрата
x_y_of_the_square = []
for col in range(distance, HEIGHT - distance, int(square_size + distance)):
    for row in range(distance, WIDTH - distance, int(square_size + distance)):
        x_y_of_the_square.append((row, col))
print(x_y_of_the_square)

clock = pygame.time.Clock()  # создаем экземпляр класса Clock
FPS = 30  # частота кадров в секунду (Frames Per Second)



# Создаем игровое поле c квадратами


for element in x_y_of_the_square:
    pygame.draw.rect(window_of_view, BLUE, (
        element[0], element[1], square_size, square_size))  # с помощью модуля draw рисуем квадраты
pygame.draw.rect(window_of_view, GREEN, (0, 0, WIDTH, HEIGHT), 2)  # контур игрового окна
pygame.display.update()  # чтобы наши рисования отобразились у пользователя


# Проверка выигрышных комбинаций
def who_is_winner(list_of_signs, win_symbol):
    winner_is = False
    # Проверяем комбинацию по горизонтали

    for row in range(3):
        if list_of_signs[row][0] ==  list_of_signs[row][1] == list_of_signs[row][2] == win_symbol:
            print(f'Выиграли {win_symbol}')
            winner_is = True

    # Проверяем комбинацию по вертикали
    for col in range(3):
        if list_of_signs[0][col] == list_of_signs[1][col] == list_of_signs[2][col]== win_symbol:

            print(f'Выиграли {win_symbol}')
            winner_is = True

    # Проверяем комбинацию по диагонали

    if list_of_signs[0][0] == list_of_signs[1][1] ==  list_of_signs[2][2] == win_symbol :
        print(f'Выиграли {win_symbol}')
        winner_is = True
    if list_of_signs[0][2] == list_of_signs[1][1] ==  list_of_signs[2][0] == win_symbol:
        print(f'Выиграли {win_symbol}')
        winner_is = True

    return winner_is

# Проверка событий и выхода из программы

gamer = 0 # переменная для чередования игроков
game_over = False
while True:
    clock.tick(FPS)
    # Создаем стартовое окно

    # Обращаемся к модулю display
    # с помощью функции set_mode, задаем в качестве аргумента размеры(разрешение) окна и задаем свойство
    # изменения размера окна
    # Создаем окно игры

    pygame.display.set_caption("Krestiki-Noliki")  # Название окна нашей игры
    pygame.display.set_icon(pygame.image.load('icon.jpg'))  # Меняем иконку pygame на свою
    window_of_view = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.draw.rect(window_of_view, GREEN, (0, 0, WIDTH, HEIGHT), 2)  # контур  окна
    for current_event in pygame.event.get():
        # После того как ожидаемое событие(нажатие на крестик) наступило, завершаем работу с библиотекой
        # pygame вызовом функции pygame.quit()
        if current_event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Событие нажатие мышкой на квадрат

        elif current_event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            # while  game_over == False:
            mouse_click = current_event.pos

            row = mouse_click[1] // (square_size + distance)
            col = mouse_click[0] // (square_size + distance)

            # Заполняем список x и o

            if list_of_the_numbers[row][col] == 0:
                if gamer % 2 == 0:
                    list_of_the_numbers[row][col] = 'x'
                else:
                    list_of_the_numbers[row][col] = 'o'
            # print(list_of_the_numbers)
            gamer += 1

        gamer_1 = who_is_winner(list_of_the_numbers,'x')
        gamer_2 = who_is_winner(list_of_the_numbers,'o')
        if gamer_1 or gamer_2:
            game_over = True
            if gamer_1:

                pygame.display.set_caption('Крестики выиграли!')
                game_over = True
            else:

                pygame.display.set_caption('Нолики выиграли!')
                game_over = True
        elif gamer == 9:
            game_over = True

            pygame.display.set_caption('Ничья!')

        pygame.display.update()
        if game_over == True:
            window_of_view.fill(BLUE)
            font = pygame.font.SysFont('comicsans',38)
            text =font.render ('Игра окончена',True,RED)
            window_of_view.blit(text, (WIDTH/3,HEIGHT/3))
            pygame.display.update()
        # Изменение цвета клетки при ходе
        if not game_over:
            for row in range(3):
                for col in range(3):
                    if list_of_the_numbers[row][col] == 'x':
                        color_of_square = GREEN
                    elif list_of_the_numbers[row][col] == 'o':
                        color_of_square = BLACK
                    else:
                        color_of_square = BLUE

                    x = col * (square_size + distance) + distance
                    y = row * (square_size + distance) + distance
                    pygame.draw.rect(window_of_view, color_of_square,
                                     (x, y, square_size, square_size))

                    if color_of_square == GREEN:
                        pygame.draw.line(window_of_view, BLUE, (x, y),
                                         (x + square_size, y + square_size), 6)
                        pygame.draw.line(window_of_view, BLUE, (x + square_size, y),
                                         (x, y + square_size), 6)
                    elif color_of_square == BLACK:
                        pygame.draw.circle(window_of_view, GREEN,
                                           ((x + 0.5 * square_size), (y + 0.5 * square_size)),
                                           square_size / 2 - 2, 6)

        pygame.display.update()

