init python:
    # Центрирование текста рассказчика
    style.narrator_dialogue = Style(style.default)
    style.narrator_dialogue.xalign = 0.5
    style.narrator_dialogue.text_align = 0.5

    # Счётчик прогулов
    skipped_days = 1
    rep = 0

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
image kp_or_colledge = "bg/kp4.png"
image kp_or_colledge2 = "bg/lool.png"
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

# Начало игры
label chapter1_start:
    scene black_back

    call chapter1_bus_scene
    call chapter1_college_choice
    
    if skipped_days > 4:
        jump bad_ending
    else:
        jump chapter2_start

    return

# Сцена в автобусе
label chapter1_bus_scene:
    narrator "Родной автобус Е85 - единственный и неповторимый в своей красоте и удобстве, плавно замедляет свой ход." (what_slow_cps=30)
    
    narrator "Студенты разных учреждений района Орехово-Борисово, сонной толпой толпятся у выхода, нетерпеливо ожидая, пока двери откроются." (what_slow_cps=30)
    
    narrator "Через пару минут начнутся занятия." (what_slow_cps=30)
    narrator "И только один студент все еще остается безразличным...." (what_slow_cps=30)
    
    bus "Остановка 'Седьмой микрорайон Орехово-Борисово', перед выходом не забывайте свои вещи..." (what_slow_cps=30)
    narrator "Нурик подскакивает." (what_slow_cps=30)

    show nurik at left_side with hpunch
    N "(Язык хештегов),(язык хештегов), чуть не (язык хештегов) свою остановку!" (what_slow_cps=30)
    hide nurik with dissolve
    
    scene kp_or_colledge2 with fade:
        fit "contain"
    
    return

# Выбор пути
label chapter1_college_choice:
    narrator "Великое здание возвышается перед Нуриком - а чуть позади стоит колледж Царицыно." (what_slow_cps=30)
    narrator "Ну, по крайней мере, он еще стоит."(what_slow_cps=30)
    narrator "С неохотой Нурик пытается вспомнить расписание, которое им уготовила администрация."(what_slow_cps=30)

    show nurik at left_side with hpunch
    N "Емае, сегодня пять пар..." (what_slow_cps=25)
    hide nurik with dissolve

    narrator "Нурик оглядывается на посеревшее здание, затем на яркие, красочные билборды торгового центра."(what_slow_cps=30)
    narrator "Хороший маркетинг - важная составляющая мотивации."(what_slow_cps=30)

    menu:
        "Свальсировать с пар в Каширскую плазу.":
            jump chapter1_shopping_ending
        "Пойти в колледж.":
            jump chapter1_college_ending
    
    return

label chapter1_shopping_ending:
    narrator "Капитализм победил! Булочки в Ашане оказались сильнее желания учиться." (what_slow_cps=30)
    narrator "Сегодня бедный каракалпак смог избежать страданий." (what_slow_cps=30)
    scene black_back with fade
    narrator "Нурик прогулял пары..." (what_slow_cps=30)

    $ rep -= 1
    $ skipped_days += 1

    # Показ текущего дня
    $ day_text = "День %d из 5" % skipped_days
    narrator "[day_text]" (what_slow_cps=30)

    if skipped_days > 4:
        jump bad_ending
    else:
        jump chapter1_start

    # Здесь может быть переход на главу 2
    jump chapter1_start

label chapter1_college_ending:
    narrator "Совесть взяла свое." (what_slow_cps=30)
    narrator "Не спеша, уже и так опаздывая, Нурик идет к входу, созерцая вид вновь перекладываемого асфальта." (what_slow_cps=30)
    narrator "Ух Собянин, ух молодец!" (what_slow_cps=30)
    narrator "Вдруг, мимо быстро, почти незаметно из-за своей скорости, проходит Дмитрий Ильич Ларионов." (what_slow_cps=30)

    show nurik at left_side with hpunch
    N "Здра..." (what_slow_cps=25) 
    hide nurik with dissolve

    narrator "Дмитрий Ильич даже не повернулся.." (what_slow_cps=30)

    show nurik at left_side with hpunch
    N "окак! Надо было сдавать фласку на первом курсе." (what_slow_cps=30)
    hide nurik with dissolve
    
    # Эффект затемнения экрана
    scene black_back with fade
    pause 1.0

    # Подпись: "Глава 2"
    show text "Глава 2" at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    pause 0.5

    jump chapter2_start