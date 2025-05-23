init:
    transform left_big_shake_red:
        xpos 0.1
        ypos 1.0
        xanchor 0.5
        yanchor 1.0
        zoom 1.25
        parallel:
            linear 0.05 xoffset -8
            linear 0.05 xoffset 8
            repeat
        parallel:
            matrixcolor TintMatrix("#ff6666")
            alpha 0.5
            linear 0.3 alpha 1.0
            linear 0.3 alpha 0.5
            repeat

    transform shake:
        xalign 0.0
        yalign 1.0
        linear 0.05 xoffset -10
        linear 0.05 xoffset 10
        repeat

    transform left_big_shake:
        xpos 0.1
        ypos 1.0
        xanchor 0.5
        yanchor 1.0
        zoom 1.25
        parallel:
            linear 0.05 xoffset -8
            linear 0.05 xoffset 8
            repeat

    transform left_big:
        xpos 0.1
        ypos 1.0
        xanchor 0.5
        yanchor 1.0
        zoom 1.25

    transform right_big:
        xpos 0.9
        ypos 1.0
        xanchor 0.5
        yanchor 1.0
        zoom 1.5


define smir = Character('Смирнов', what_slow_cps=20, window_style="window")
define p = Character('Полина', what_slow_cps=20, window_style="window")

# --- Изображения ---
image rnd_deck = "bg/lesson_smirnov/cropped-rnd_deck.png"
image laptops = "bg/lesson_smirnov/cropped-laptops.png"
image smirnov = "characters/smirnov_small.png"
image polina = "characters/small_polina.png"
image polina_deb = "characters/small_polina_deb.png"


label chapter5_start:

    scene rnd_deck with fade:
        fit "contain"
    narrator "Пятая пара..."

    narrator "Во время ожидания опроса проходят все стадии принятия: отрицание, гнев, торг, депрессия, принятие, шутка про математиков." (what_slow_cps=30)

    narrator "Смирнов Евгений Михайлович включает рандомайзер..." (what_slow_cps=30)

    #play sound "audio/slot_machine.wav"
    narrator "Жизнь мелькает перед глазами также, как цифры в рандомайзере." (what_slow_cps=30)
    narrator "И вот, спустя секунды ужаса, выпадает 5..." (what_slow_cps=30)

    show nurik at left_side
    N "Фух..." (what_slow_cps=25)
    hide nurik with dissolve

    show polina at left_big_shake_red
    # show screen tremble_effect

    narrator "Полина медленно выходит и нервно хихикает. От страха ее руки дрожат." (what_slow_cps=30)

    show smirnov at right_big
    smir "Так… Что такое первая нормальная форма?" (what_slow_cps=25)

    p "Ну… Это…" (what_slow_cps=20)

    narrator "Следующие несколько минут проходят относительно спокойно для группы, но ужасно для Полины." (what_slow_cps=30)
    hide polina with dissolve
    show polina_deb at left_big
    narrator "Её отпускают с 4. Видимо, за тряску." (what_slow_cps=30)
    
    smir "Следующий…" (what_slow_cps=30)
    hide polina_deb with dissolve


    play sound "audio/casino_spin.wav"
    smir "Мещерякова, к доске." (what_slow_cps=30)

    narrator "Одногруппники смешливо переглядываются" (what_slow_cps=25)
    show nurik at left_side
    l "Ээ… Она обещала приехать к четвёртой паре" (what_slow_cps=25)
    narrator "Подольск — страшное место." (what_slow_cps=25)
    hide nurik with dissolve

    narrator "Нурик несколько раз моргает, но заветная девятка предательски остаётся на месте. Придётся отвечать." (what_slow_cps=30)

    jump chapter5_quiz


label chapter5_quiz:

    scene laptops with fade:
        fit "contain"
    show text "Мини-опрос: нормальные формы" at truecenter with dissolve
    pause 2.0
    hide text with dissolve

    $ correct_answers = 0

    smir "Вопрос первый. Первая нормальная форма?" (what_slow_cps=25)
    $ ans1 = renpy.input("Ответ:").strip().lower()

    if ans1 == "Отношение находятся в первой нормальной форме если все его атрибуты просты и далее неделимы":
        smir "Верно." (what_slow_cps=25)
        $ correct_answers += 1
    else:
        smir "Неверно." (what_slow_cps=25)

    smir "Второй вопрос. Вторая нормальная форма?" (what_slow_cps=25)
    $ ans2 = renpy.input("Ответ:").strip().lower()

    if ans2 == "Отношение находятся во второй нормальной форме если они находятся в первой нормальной форме и каждый не ключевой атрибут функционально полно зависит от первичного ключа.":
        smir "Правильно." (what_slow_cps=25)
        $ correct_answers += 1
    else:
        smir "Нет, не так." (what_slow_cps=25)

    smir "Третий вопрос. Что такое третья нормальная форма?" (what_slow_cps=25)
    $ ans3 = renpy.input("Ответ:").strip().lower()

    if ans3 == "godmode":
        narrator "Экран гаснет. Пространство колеблется..." (what_slow_cps=30)
        smir "…Интересно. Такое ощущение, что ты что-то знаешь больше, чем нужно..." (what_slow_cps=25)
        jump chapter5_alt_ending
    else:
        smir "Допустим. Садись." (what_slow_cps=25)

    jump chapter5_result


label chapter5_result:

    if correct_answers >= 2:
        show nurik at left_side
        N "Ну, вроде норм..." (what_slow_cps=25)
        hide nurik with dissolve

        smir "Тройка... А впрочем, тройка тоже неплохо! Да и завод с каждой секундой кажется всё перспективнее." (what_slow_cps=25)

        narrator "Ачивка: «На пять знает только Бог, на четыре — преподаватель»" (what_slow_cps=30)

        $ rep += 1
        jump chapter6_start
    else:
        smir "Спасибо. Удачи на пересдаче." (what_slow_cps=25)

        $ rep -= 1
        jump chapter6_start


label chapter5_alt_ending:

    scene black_back with fade
    narrator "Экран гаснет. Небо становится фиолетовым." (what_slow_cps=30)
    narrator "Из недр реальности доносится: «Пятёрка. Даже я бы так не ответил.»" (what_slow_cps=30)

    $ rep += 2
    narrator "Ты взломал матрицу." (what_slow_cps=30)

    jump chapter6_start
