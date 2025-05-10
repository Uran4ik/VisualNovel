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
image cloakroom = "bg/cloakroom/cloakroom1.png"
image corridor2= "bg/corridor/corridor2.png"
image nurik = "characters/nurik.png"
image black_back = "#000000"

# Трансформы
transform left_side:
    xalign 0.05
    yalign 1.16

transform right_side:
    xalign 0.95
    yalign 1.0


label peremena3_start:
    scene black_back
    show text "Перемена" at truecenter with fade
    pause 1.5
    hide text with fade
    
    # Контент главы 3...
    call peremena3_go
    # Завершение игры
    jump game_over

label peremena3_go:
    show corridor2 with fade:
            fit "contain"
    narrator "Надо быстрее добраться до раздевалки." (what_slow_cps=30)
    $ renpy.call_screen("scr_achievement_get", title="Тест", a_text="Экран работает", icon="images/GERB.png")
    narrator "Надо быстрее добраться до раздевалки." (what_slow_cps=30)
    show nurik:
        xalign -1.0 yalign 1.0
        linear 3 xalign 1.0 yalign 1.0
    narrator "Хуже очереди в столовую только толпа в холле." (what_slow_cps=30)
    show cloakroom with fade:
            fit "contain"
    show nurik at left_side with hpunch
    return