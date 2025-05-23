init python:
    # Счётчики
    skipped_days = 1
    rep = 0

# Стиль для центрированного текста vghvgvvgvvgvgvgvg
style narr_style:
    xalign 0.5
    text_align 0.5

style window:
    yalign 1.0
    xsize 1920
    ysize 300
    background Frame("gui/textbox.png", 25, 25)

# Персонажи
define narrator = Character(
    None,
    kind=adv,
    what_slow_cps=20,
    window_style="window",   
    what_style="narr_style"
)
define N = Character('Нурик', image="nurik", what_slow_cps=20, window_style="window")
define L = Character('Дмитрий Ильич', image="larionov", what_slow_cps=20, window_style="window")

# Изображения с корректировкой размеров
image bg classroom = im.Scale("bg/lesson_larionov/new.jpg", 1920, 1080)
image bg poblighe = im.Scale("bg/lesson_larionov/poblighe.jpg", 1920, 1080)
image destroy = im.Scale("bg/lesson_larionov/destroy.png", 1000, 700)  # Добавлено изображение скримера
image nurik = im.Scale("characters/Nur_udivil.png", 500, 800)
image larionov = im.Scale("characters/lar3.png", 850, 900)

# Трансформы
transform center_right:
    xalign 0.75 yalign 1.0

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

transform scary_effect:  # Трансформ для скримера
    zoom 1.1
    alpha 0.0
    linear 0.1 alpha 1.0
    pause 0.5
    linear 0.1 alpha 0.0

image black_back = "#000"

# Эффекты
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define shake = Move((0, 10), (0, -10), 0.1, bounce=True, repeat=True, delay=0.5)

label chapter4_start:
    # Заставка главы
    scene black_back
    show text "Глава 4: Четвертая пара" at truecenter with fade
    pause 1.5
    hide text with fade
    
    scene bg classroom with fade
    show bg classroom with shake
    
    "Боль резко пронзила голову Нурика. Он лежал на полу, глаза щурились от яркого света..."
    
    show nurik at center_right with dissolve
    N "какого (язык хештегов)???? "
    
    "После не самого нежного пробуждения раскалывается голова. Четвертая пара тоже совсем не подходит для работы"
    
    show nurik at center_right with move
    "Нурик дергает ручку двери."
    hide nurik with dissolve
    
    show larionov at far_left with dissolve
    L "Эх, а могли бы сделать фласк на первом курсе... теперь придется отдуваться."
    hide larionov with dissolve
    
    show larionov at far_left with dissolve
    L "Садитесь поближе, сейчас все быстро расскажу и будете работать."
    
    # Смена фона после этой фразы
    scene bg poblighe with dissolve
    show larionov at far_left
    
    # Невнятная речь с движением
    show larionov at far_left, random_move
    "*очень быстро и невнятно говорит* (ненененене ролокс мемес)"
    show larionov at far_left
    
    L "Все понятно????"
    hide larionov with dissolve
    
    show nurik at center_right with flash
    "*испуганная пнгшка нурика*"
    hide nurik with dissolve
    
    show larionov at far_left with dissolve
    L "*продолжает очень быстро и невнятно говорить*"
    hide larionov with dissolve
    
    "Дмитрий Ильич с особым мастерством проходится...нет, пробегается по теме. И, хотя в глазах одногруппников понимания меньше, чем страха, все кивают."
    
    "Что ж, нужно выбираться из плачевного положения."
    
    "*звук возникновения идеи*"
    
    # Сцена спора - показываем обоих
    show larionov at far_left with dissolve
    show nurik at center_right with dissolve
    
    N "Дмитрий Ильич, вы такой же быстрый, как D2..."
    
    show nurik at center_right
    hide larionov with dissolve
    L "Что за бред? D1 быстрее!"
    
    show larionov at far_left with dissolve
    hide nurik with dissolve
    N "Нет, D2 намного круче чем D1! Вы видели как там мои ласточки летают???? Готов поспорить, что они быстрее."
    
    show nurik at center_right
    hide larionov with dissolve
    L "Ты сейчас договоришься, каракалпакский мальчик."
    
    # Выбор действия
    menu:
        "Настоять на своем мнении о D2":
            $ rep -= 1
            show larionov at far_left with dissolve
            L "Я же говорил!"
            play sound "audio/destroy.ogg"
            
            # Скример с destroy.jpg
            show destroy at scary_effect, truecenter
            "*звук этеншн и знак тревоги, прилетает дестрой пак*"
            hide destroy
            
            "Нурик переоценил свои способности. Теперь, помимо основной работы, он получит наказание."
            scene black_back with fade
            
        "Согласиться с Дмитрием Ильичом":
            $ rep += 1
            show larionov at far_left with dissolve
            L "Так уж и быть..."
            "Ларионов теряет интерес и нурик может выдохнуть"
            scene black_back with fade
    
    "Остаток пары проходит невозможно медленно и муторно."
    
    if rep >= 1:
        "Счастливо нурик уходит из 116."
    else:
        "О нет. Кажется ему отшибло память и он стал первокурсником. Не надо было это делать..."
    
    return