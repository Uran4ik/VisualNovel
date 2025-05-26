

style narr_style:
    xalign 0.5
    text_align 0.5

style window:
    yalign 1.0
    xsize 1920
    ysize 300
    background Frame("gui/textbox.png", 25, 25)


define narrator = Character(
    None,
    kind=adv,
    what_slow_cps=20,
    window_style="window",   
    what_style="narr_style"
)
define N = Character('Нурик', image="nurik", what_slow_cps=20, window_style="window")


# Изображения
image bg classroom = im.Scale("bg/lesson_larionov/new.jpg", 1920, 1080)
image bg poblighe = im.Scale("bg/lesson_larionov/poblighe.jpg", 1920, 1080)
image destroy = im.Scale("bg/lesson_larionov/destroy.png", 1000, 700)
image nurik = im.Scale("characters/Nur_udivil.png", 500, 800)
image larionov = im.Scale("characters/lar3.png", 850, 900)
image bg background = im.Scale("bg/lesson_larionov/bacground.jpg", 1920, 1080)
image bg vih = im.Scale("bg/lesson_larionov/vih.jpg", 1920, 1080)
image bg poteryalsya = im.Scale("bg/lesson_larionov/poteryalsya.jpg", 1920, 1080)
image bg exit = im.Scale("bg/lesson_larionov/exit.jpg", 1920, 1080)

transform center_right:
    xalign 0.75 
    yalign 1.0
transform far_left:
    xalign 0.12 yalign 1.0
    zoom 1.0

transform random_move:
    linear 0.1 xoffset 10 yoffset 5
    linear 0.1 xoffset -15 yoffset -10
    linear 0.1 xoffset 20 yoffset 0
    linear 0.1 xoffset -5 yoffset 15
    linear 0.1 xoffset 0 yoffset 0
    repeat

transform scary_effect:
    zoom 1.1
    alpha 0.0
    linear 0.1 alpha 1.0
    pause 0.5
    linear 0.1 alpha 0.0

image black_back = "#000"


label chapter4_peremena:
    scene bg vih with fade
    "Пара закончилась. Студенты устало выходят из кабинета." (what_slow_cps=25)
    show nurik at center with dissolve
    N "Фух, наконец-то можно отдохнуть..." (what_slow_cps=25)
    hide nurik with moveoutright
    
    scene bg poteryalsya with fade
    "Нурик выходит за ними... чтобы понять, что он потерялся." (what_slow_cps=25)
    show nurik at center with dissolve
    N "Окак... Где это я?" (what_slow_cps=25)
    "Пока он осматривается по сторонам, пытаясь вспомнить, где он, одногруппники уже уходят." (what_slow_cps=25)
    hide nurik with dissolve
    "Нурик остается один в страшном коридоре колледжа Царицыно." (what_slow_cps=25)
    
    show nurik at center with dissolve
    N "116 кабинет - замечательное место. Особенно для прогулок." (what_slow_cps=25)
    N "Пора подключать свои скиллы ориентирования по местности." (what_slow_cps=25)
    hide nurik with dissolve
    
    # Запуск мини-игры с лабиринтом
    call maze_game
    
    scene bg exit with fade
    show nurik  at center with dissolve
    "И вот спустя долгое время Нурик наконец-то выходит." (what_slow_cps=25)
    "Но чувство облегчения медленно сменяется ужасом." (what_slow_cps=25)
    N "О нет... Сейчас будет пара баз данных..." (what_slow_cps=25)
    hide nurik with dissolve
    
    scene black_back  with fade
    "215 кабинет, стоят мало студентиков и волнуются." (what_slow_cps=25)
    show polina  at left with dissolve
    P "ХОТЬ БЫ ХОТЬ БЫ ХОТЬ БЫ 🙏🙏🙏" (what_slow_cps=25)
    show nurik  at right with dissolve
    "Похоже, одногруппники Нурика разделяют его тревогу." (what_slow_cps=25)
    "Большая часть испугалась настолько, что испарилась." (what_slow_cps=25)
    
    "Уровень благоразумия группы медленно падает." (what_slow_cps=25)
    
    
# Мини-игра "Лабиринт"
init python:
    class MazeGame:
        def __init__(self):
            self.maze = [
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
                [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
                [1,0,1,0,1,0,0,0,1,0,0,0,1,0,1],
                [1,0,1,0,1,1,1,1,1,1,1,0,1,0,1],
                [1,0,0,0,0,0,0,0,0,0,1,0,1,0,1],
                [1,1,1,1,1,1,1,0,1,0,1,0,1,0,1],
                [1,0,0,0,0,0,0,0,1,0,0,0,1,0,1],
                [1,0,1,1,1,1,1,1,1,1,1,1,1,0,1],
                [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,0,1,0,1,1,1,1,1,1,1],
                [1,0,0,0,0,0,1,0,0,0,0,0,4,0,1],
                [1,0,1,1,1,1,1,1,1,1,1,1,1,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,3,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            ]
            self.start_pos = [1, 1]
            self.player_pos = self.start_pos.copy()
            self.cell_size = 72  # Увеличил размер ячейки для 1920x1080
            self.won = False
            self.move_sound = "audio/move.wav"
            self.win_sound = "audio/win.wav"
            self.trap_sound = "audio/trap.wav"
            self.time_left = 180  # 3 минуты на прохождение
            self.steps = 0

        def reset(self):
            self.player_pos = self.start_pos.copy()
            self.won = False
            
        def move_player(self, dx, dy):
            if self.won:
                return
                
            new_x = self.player_pos[0] + dx
            new_y = self.player_pos[1] + dy
            
            if 0 <= new_x < len(self.maze[0]) and 0 <= new_y < len(self.maze):
                cell_value = self.maze[new_y][new_x]
                
                if cell_value != 1:  # Если не стена
                    self.player_pos = [new_x, new_y]
                    self.steps += 1
                    renpy.play(self.move_sound, channel="sound")
                    
                    if cell_value == 3:  # Выход
                        self.won = True
                        renpy.play(self.win_sound, channel="sound")
                    elif cell_value == 4:  # Ловушка
                        renpy.play(self.trap_sound, channel="sound")
                        self.time_left = max(0, self.time_left - 10)  # Штраф 10 секунд

screen maze_screen():
    default maze = MazeGame()
    # Размеры лабиринта (15x15 клеток)
    default maze_width = 15 * maze.cell_size
    default maze_height = 15 * maze.cell_size
    # Центрирование лабиринта (точно по центру)
    default maze_xpos = (1920 - maze_width) // 2
    default maze_ypos = (1080 - maze_height) // 2
    
  
    # Контейнер лабиринта (строго по центру)
  
    
    # Фон
    add "#000"
    # Контейнер лабиринта
    frame:
        pos (maze_xpos, maze_ypos)
        background None
        xsize maze_width
        ysize maze_height
        
        # Отрисовка лабиринта
        for y in range(len(maze.maze)):
            for x in range(len(maze.maze[0])):
                $ cell = maze.maze[y][x]
                if cell == 1:  # Стена
                    add Solid("#333333", xsize=maze.cell_size, ysize=maze.cell_size):
                        pos (x * maze.cell_size, y * maze.cell_size)
                elif cell == 3:  # Выход
                    add "bg/lesson_larionov/exit.jpg":
                        size (maze.cell_size, maze.cell_size)
                        pos (x * maze.cell_size, y * maze.cell_size)
                elif cell == 4:  # Ловушка
                    add "bg/lesson_larionov/vih.jpg":
                        size (maze.cell_size, maze.cell_size)
                        pos (x * maze.cell_size, y * maze.cell_size)
    
        # Игрок
        add "characters/Nur_udivil.png":
            size (maze.cell_size, maze.cell_size)
            pos (maze.player_pos[0] * maze.cell_size, maze.player_pos[1] * maze.cell_size)
    
    # Управление
    key "K_LEFT" action Function(maze.move_player, -1, 0)
    key "K_RIGHT" action Function(maze.move_player, 1, 0)
    key "K_UP" action Function(maze.move_player, 0, -1)
    key "K_DOWN" action Function(maze.move_player, 0, 1)
    
    # Информация о времени и шагах
    vbox:
        pos (50, 50)
        text "Время: [maze.time_left] сек" size 36
        text "Шаги: [maze.steps]" size 36
    
    # Кнопка выхода
    textbutton "Сдаюсь!":
        action Jump("maze_give_up")
        align (0.95, 0.05)
        text_size 36
        padding (25, 15)
        background "#333"
        hover_background "#555"
    
    # Таймер
    timer 1.0 repeat True action If(maze.time_left > 0 and not maze.won, 
                        SetField(maze, "time_left", maze.time_left - 1), 
                        If(maze.time_left <= 0, Jump("maze_timeout")))
    
    # Проверка победы
    if maze.won:
        timer 1.0 action Jump("maze_complete")

label maze_game:
    window hide
    call screen maze_screen
    return

label maze_complete:
    window show
    "Нурик нашел выход из лабиринта за [maze.steps] шагов!"
    return

label maze_timeout:
    window show
    show nurik at center
    N "Время вышло! Придется начинать сначала..."
    hide nurik
    jump maze_game

label maze_give_up:
    window show
    show nurik at center with dissolve
    N "Я не могу найти выход! Может, стоит попробовать еще раз?"
    hide nurik with dissolve
    jump maze_game