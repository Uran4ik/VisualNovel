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

define l = Character('Леша', color="#c8ffc8", what_slow_cps=20, window_style="window")
define bus = Character('Автоинформатор', color="#c8ffc8", what_slow_cps=20, window_style="window")
define N = Character('Нурик', image="nurik", what_slow_cps=20, window_style="window")

# Изображения
image kab_104 = "bg/lesson_kovaleva/kbinet.png"
image blue_screen104 = "bg/lesson_kovaleva/blue_screen.png"
image lesha = "characters/lesha.png"
image nurik = "characters/nurik.png"
image black_back = "#000000"

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
    # Завершение игры
    jump game_over


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

    
    return