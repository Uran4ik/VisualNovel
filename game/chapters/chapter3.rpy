init python:
    # Центрирование текста рассказчика
    style.narrator_dialogue = Style(style.default)
    style.narrator_dialogue.xalign = 0.5
    style.narrator_dialogue.text_align = 0.5

# Стиль диалогового окна 
style window:
    ypos 1080
    xsize 2000
    ysize 240
    background Frame("gui/textbox.png", 25, 25)

# Персонажи
define narrator = Character(
    None,
    kind=adv,
    what_slow_cps=20,
    window_style="window",
    what_style="narrator_dialogue"
)

define Kov = Character('Елизавета Александровна' , color="#807adb", what_slow_cps=20, window_style="window")
define bus = Character('Автоинформатор', color="#c8ffc8", what_slow_cps=20, window_style="window")
define N = Character('Нурик', image="nurik", what_slow_cps=20, window_style="window")

# Изображения
image kab_104 = "bg/lesson_kovaleva/kbinet.png"
image blue_screen104 = "bg/lesson_kovaleva/blue_screen.png"
image nurik = "characters/nurik.png"
image black_back = "#000000"
image kovaleva = Transform("characters/kovaleva.png", zoom=0.3)
image kovaleva_rk = Transform("characters/kovaleva_rk.png", zoom=0.18)
image kovaleva_cool = Transform("characters/kovaleva_cool.png", zoom=0.18)
image compilator = "bg/lesson_kovaleva/compilator.png"
image game104back = "bg/lesson_kovaleva/workCode.png"

# Трансформы
transform left_side:
    xalign 0.05
    yalign 1.16

transform right_side:
    xalign 0.95
    yalign 1.0


label chapter3_start:
    scene black_back
    show text "Глава 3: Кульминация" at truecenter with fade
    pause 1.5
    hide text with fade
    
    # Контент главы 3...
    call before_game_104
    call game_104
    call aftergame_104
    # Завершение игры
    jump peremena3_start


label before_game_104: 
    scene kab_104 with fade:
        fit "contain"
    narrator "Хаги Ваги одиноко обнимает кулер. “Не пить!” – гласит надпись. Вот он – дефицит в своем истинном обличии." (what_slow_cps=25)
    
    narrator "Из каморки внутри кабинета поочередно выходят Быков, Лутфуллин и Ларионов." (what_slow_cps=25)
    
    narrator "Последний вновь быстро уходит." (what_slow_cps=25)
    narrator "Нурик садится за стол и достает ноутбук. Вновь практические." (what_slow_cps=25)
    
    narrator "На третьей паре тоже не особо работается… Ведь уже обед, а столовая забрала все моральные силы." (what_slow_cps=25)
    narrator "Неохотно, он открывает ноутбук." (what_slow_cps=25)

    scene blue_screen104 with fade:
        fit "contain"

    show nurik at left_side with hpunch
    N "(язык хэштегов), о нет, моя винда! Мой майнкрафт! Все пропало!" (what_slow_cps=30)
    hide nurik with dissolve
    
    narrator "Это расстраивает его настолько, что он думает о побеге с пар." (what_slow_cps=25)

    narrator "Но пока что ему нужно пересесть за компьютер и сделать практическую. К сожалению, даже Visial Studio не выдержала и сбежала с компьютеров колледжа." (what_slow_cps=25)

    scene compilator:
        fit "contain"
        
    show nurik at left_side with hpunch

    N "Ну, а конспект я писать конечно же не буду. Всё же можно распечатать." (what_slow_cps=25)

    narrator "Нурик открывает онлайн компилятор. Как жаль, что здесь нет рекламы айкью тестов." (what_slow_cps=25)

  
    scene black_back with fade
    pause 1
    
    scene kab_104 with fade:
        fit "contain"
    show kovaleva_rk at right_side with dissolve
    # linear 3.0 xpos 0 ypos 100
    Kov  "..A сейчас я вырублю рубильник… Кто не успел сохранить работу – тот сам виноват." (what_slow_cps=25)
    narrator "Откуда-то раздается тревожная музыка… Елизавета Александровна медленно направляется к машине для убийства нервных клеток."
    return

label game_104:
    scene game104back with fade:
        fit "contain"
    narrator "Нурик судорожно хватает мышку. Придется сохранять работу в блокнот"
    # Настройки игры
    $ total_rounds = 7               # Всего кнопок
    $ time_per_round = 2          # Время на реакцию в сек
    $ current_round = 1              
    $ game_success = False           

    
    $ x_min = 0.1
    $ x_max = 0.9
    $ y_min = 0.2
    $ y_max = 0.7

    # Запуск игры
    call screen button_chase_game

    # Проверка результата
    if game_success:
        jump saved
    else:
        jump time_up

screen button_chase_game():
    # Показываем новую кнопку 
    timer 0.9 repeat True action If(
        current_round <= total_rounds,
        [SetVariable("clicked", False), Show("button_chase")],
        [SetVariable("game_success", True), Hide("button_chase"), Return()]
    )

screen button_chase():
    # Координаты 
    $ x_pos = renpy.random.uniform(x_min, x_max)
    $ y_pos = renpy.random.uniform(y_min, y_max)

    # Таймер исчезновения кнопки
    timer time_per_round action [
        If(not clicked, [Hide("button_chase"), SetVariable("current_round", total_rounds + 1), Return()])
    ]

    # кнопка 
    button:
        xpos x_pos
        ypos y_pos
        xanchor 0.5
        yanchor 0.5
        at button_appear
        background Solid("#404040")
        padding (25, 15)
        action [
            SetVariable("clicked", True),
            Hide("button_chase"),
            SetVariable("current_round", current_round + 1),
            
        ]

        text "Сохранить!":
            size 30
            color "#FFFFFF"

    # раунд сверху налпсиь
    vbox:
        xalign 0.5
        ypos 50
        text "Раунд: [current_round]/[total_rounds]":
            size 30
            color "#FFFFFF"

#поялвление кнопки
transform button_appear:
    alpha 0.0
    linear 0.3 alpha 1.0  

label time_up:
    narrator "О нет! Нурик забыл сохранить работу."
    show kovaleva_cool at right_side with dissolve
    Kov "Надо было сохранять." (what_slow_cps=25)
    scene black_back
    narrator "Нурик долго ругается на свою забывчивость, но все же приступает к работе заново."
    # здесь минус репутация вайб аура счастье идк!!!!!!!
    return

label saved:
    narrator "Ура! Работа сохранена и в полной безопасности. Осталось только защитить её и уйти."
    return


label aftergame_104:
    scene kab_104 with fade:
        fit "contain"
    show nurik at left_side with hpunch
    N "Я готов сдавать!" (what_slow_cps=25)
    narrator "Или сдаваться." (what_slow_cps=25)
    narrator "Елизавета Александровна подходит к нему." (what_slow_cps=25)
    show kovaleva_rk at right_side with dissolve
    Kov "А где конспект?" (what_slow_cps=25)
    show nurik at left_side with hpunch
    N "Ну.." (what_slow_cps=25)
    narrator "К неудаче, Нурик принял решение быть не таким как все. Лучше бы он слился с обществом." (what_slow_cps=25)
    Kov "Ну вот как напишешь – тогда и защитишь." (what_slow_cps=25)
    hide kovaleva
    narrator "Двойная печаль! Потому что как только он пересиливает себя, готовый написать конспект, пара заканчивается." (what_slow_cps=25)
    narrator "В голову Нурика приходит замечательная идея, которая моментально поднимает ему настроение." (what_slow_cps=25)
    show nurik at left_side with hpunch
    N "Лучше чистить фары, чем сидеть 4 пары." (what_slow_cps=25)
    return