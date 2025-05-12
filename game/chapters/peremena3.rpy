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

define Maks = Character('Татьяна Викторовна' , color="#e3a68a", what_slow_cps=20, window_style="window")
define bus = Character('Автоинформатор', color="#c8ffc8", what_slow_cps=20, window_style="window")
define N = Character('Нурик', image="nurik", what_slow_cps=20, window_style="window")

# Изображения
image cloakroom4 = "bg/cloakroom/cloakroom4.png"
image corridor2= "bg/corridor/corridor2.png"
image maks_scary = "bg/cloakroom/maks_scary.png"
image maks_lazer = "bg/cloakroom/maks_lazer.png"
image nurik = "characters/nurik.png"
image maksimova = Transform("characters/maksimova.png", zoom=0.8)
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
    narrator "Надо быстрее добраться до раздевалки." (what_slow_cps=25)
    
    show nurik:
        xalign -1.0 yalign 1.0
        linear 3 xalign 1.5 yalign 1.0
   
    narrator "Хуже очереди в столовую только толпа в холле." (what_slow_cps=25)
    show cloakroom4 with fade:
            fit "contain"
    hide nurik
    narrator "К огромной радости, Нурик успевает вовремя. Затора студентов нет, лишь несколько счастливчиков с тремя парами в расписании хватают свои куртки." (what_slow_cps=25)
    narrator "Воздушной походкой Нурик спешит к турникетам. Похоже, сегодня Вселенная на его стороне, потому что на выходе никого нет." (what_slow_cps=25)
    narrator "Уже представляя, как пойдет в Ашан за чесночным багетом, Нурик тянется за пропуском." (what_slow_cps=25)
    show maksimova at right_side
    Maks "Группа?" (what_slow_cps=25)
    narrator "Вот и закончилась светлая полоса его жизни." (what_slow_cps=25)
    menu:
        "Кто не рискует, тот сидит 5 пар":
            hide maksimova
            scene maks_scary:
                fit "contain"
            show nurik at left_side
            N "24ИС1-2" (what_slow_cps=25)
            narrator "Нурик совершал много ошибок в своей жизни, и решение назвать случайную группу - самая глупая из них." (what_slow_cps=25)
            narrator "Бедному студентику не повезло из всех выбрать ту, которую курирует Татьяна Викторовна" (what_slow_cps=25)
        "Честность - залог успеха":
            hide maksimova
            scene maks_scary:
                fit "contain"
            show nurik at left_side
            N "23ИС2-2" (what_slow_cps=25)
            narrator "Нурика учили никогда не врать! Примерный каракалпакский мальчик." (what_slow_cps=25)
    scene maks_lazer:
        fit "contain"
    narrator "Из глаз Татьяны Викторовны летят лазеры." (what_slow_cps=25)
    narrator "Более находчивый студент давно бы убежал, но Нурик от страха только замер." (what_slow_cps=25)
    Maks "Быстро на пару!" (what_slow_cps=25)
    
    scene black_back with fade:
        fit "contain"
    narrator "В глазах темнеет, и Нурик вырубается." (what_slow_cps=25)
return

