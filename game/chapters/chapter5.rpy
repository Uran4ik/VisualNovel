init:
    transform center_shake:
        xalign 0.5  # По центру по горизонтали
        yalign 1.0  # Внизу экрана (как у других персонажей)
        zoom 1.5  # Увеличение на 50%
        linear 0.1 xoffset 5 yoffset 5
        linear 0.1 xoffset -5 yoffset -5
        linear 0.1 xoffset 3 yoffset 3
        linear 0.1 xoffset -3 yoffset -3
        linear 0.1 xoffset 0 yoffset 0
        repeat
    transform left_big_shake_red:
        xpos 0.1
        ypos 1.0
        xanchor 0.5
        yanchor 1.0
        zoom 1.3
        parallel:
            linear 0.05 xoffset -8
            linear 0.05 xoffset 8
            repeat
        parallel:
            # matrixcolor TintMatrix("#ff6666")
            # alpha 0.5
            linear 0.3 alpha 1.0
            linear 0.3 #alpha 0.5
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
        zoom 1.65

init python:
    import re

    def normalize_answer(ans):
        # Убираем невидимые символы, пунктуацию, двойные пробелы
        cleaned = re.sub(r"[^\wа-яё\s]", "", ans.lower(), flags=re.UNICODE)
        cleaned = re.sub(r"\s+", " ", cleaned)  # Одинарные пробелы
        return cleaned.strip()

    define_strict1 = normalize_answer("отношение находится в первой нормальной форме если все его атрибуты просты и далее неделимы")
    define_strict1_1 = normalize_answer("отношение находится в первой нормальной форме, если все его атрибуты просты и далее неделимы")
    define_strict2 = normalize_answer("отношение находится во второй нормальной форме если оно находится в первой нормальной форме и каждый не ключевой атрибут функционально полно зависит от первичного ключа")
    define_strict2_2 = normalize_answer("отношение находится во второй нормальной форме, если оно находится в первой нормальной форме и каждый не ключевой атрибут функционально полно зависит от первичного ключа")
    define_strict3 = normalize_answer("больше двух")

init -2 python:
    style.input.size = 12
    style.input.color = "#ffffff"
    style.input.xmaximum = 1400  # Увеличено, чтобы вместить длинный текст
    style.input.xminimum = 800   # Минимум тоже подлиннее
    style.input.xalign = 0.0     # Можно 0.5 если хочешь по центру


screen quiz_input(prompt):
    modal True
    zorder 100

    default local_input = ""

    frame:
        xalign 0.5
        yalign 0.6
        padding (20, 20)
        has vbox

        text prompt size 26 color "#ffffff" xalign 0.5

        input id "input" default local_input changed (lambda v: SetScreenVariable("local_input", v)) size 24

        textbutton "OK" action Return(local_input) xalign 0.5

define smir = Character('Смирнов', what_slow_cps=20, window_style="window")
define p = Character('Полина', what_slow_cps=20, window_style="window")
define alina = Character('Алина', what_slow_cps=20, window_style="window")

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

    play sound "audio/wheel_of_fortune.mp3"
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

    narrator "Следующие несколько минут проходят относительно спокойно для группы, но ужасно для Полины." (what_slow_cps=25)
    hide polina with dissolve
    show polina_deb at left_big
    narrator "Её отпускают с 4. Видимо, за тряску." (what_slow_cps=25)
    
    smir "Следующий…" (what_slow_cps=25)
    hide polina_deb with dissolve


    play sound "audio/wheel_of_fortune.mp3"
    pause 4
    
    smir "Мещерякова, к доске." (what_slow_cps=25)

    narrator "Одногруппники смешливо переглядываются" (what_slow_cps=25)
    show lesha at left_side
    l "Ээ… Она обещала приехать к четвёртой паре" (what_slow_cps=25)
    hide lesha with dissolve

    smir "Ох уж эти Подольские.." (what_slow_cps=25)
    narrator "Смирнов снова запускает рандомайзер..."

    play sound "audio/wheel_of_fortune.mp3"
    pause 4

    narrator "Удача явно на стороне нурика!"  (what_slow_cps=25)
    narrator "Рандомайзер опять указывает не на него, зато Алине повезло меньше" (what_slow_cps=25)
    narrator "Она удрученно выходит отвечать, проклиная сломанный рандомайзер..." (what_slow_cps=25)

    smir "Расскажи про вторую нормальную форму" (what_slow_cps=25)
    alina "Эээ...отношение находится во второй нормальной форме..."  (what_slow_cps=25)

    narrator "Внезапно, кто-то стучит в дверь и, не дожидаясь ответа, открывает ее" (what_slow_cps=25)
    narrator "Светлана Владимировна заходит, улыбаясь группе по пути"   (what_slow_cps=25)
    narrator "Группа радостно улыбается ей в ответ: опрос откладывается из-за ее визита" (what_slow_cps=25)

    smir "Ладно, Жумаева, ты все знаешь, с тобой не интересно, садись, 5"  (what_slow_cps=25)

    narrator "Алина, как самый счастливый человек в группе, садится на место с облегчением. Все  же пронесло" (what_slow_cps=25)

    narrator "Но даже самые хорошие вещи не могут длиться долго. Светлана Владимировна уходит, оставляя группу наедине с базами данных." (what_slow_cps=30)
    
    play sound "audio/wheel_of_fortune.mp3"
    narrator "Рандомайзер запускается.." (what_slow_cps=25)
    narrator "Нурик несколько раз моргает, но заветная девятка предательски остаётся на месте." (what_slow_cps=25)
    narrator "Придётся отвечать." (what_slow_cps=25)

    jump chapter5_quiz

label chapter5_quiz:
    
    scene laptops with fade:
        fit "contain"
    pause 2.0
    hide text with dissolve

    $ correct_answers = 0
    show nurik at left_side
    show smirnov at right_big
    smir "Вопрос первый. Первая нормальная форма?" (what_slow_cps=25)

    # Устанавливаем стиль для ввода
    init python:
        style.input.size = 22  # Размер шрифта
        style.input.color = "#ffffff"  # Цвет текста
        style.input.xmaximum = 800  # Максимальная ширина поля ввода
    
    $ ans1 = renpy.input("Ответ:").strip().lower()

    if ans1 == define_strict1 or ans1 == define_strict1_1:
        smir "Ну допустим.." (what_slow_cps=25)
        $ correct_answers += 1
        $ rep += 1
    else:
        smir "НЕВЕРНО!" (what_slow_cps=25)

    smir "Второй вопрос. Вторая нормальная форма?" (what_slow_cps=25)

    $ ans2 = renpy.input("Ответ:").strip().lower()

    if ans2 == define_strict2 or ans2 == define_strict2_2:
        smir "Ну хорошо.." (what_slow_cps=25)
        $ correct_answers += 1
        $ rep += 1
    else:
        smir "Мдаа.. Можешь больше не возвращаться в 26.." (what_slow_cps=25)

    smir "Третий вопрос. Ладно расскажи тогда сколько звездочек на небе?" (what_slow_cps=25)

    $ ans3 = renpy.input("Ответ:").strip().lower()

    if ans3 == define_strict3:
        # Начинаем эффект мерцания
        show black_back
        play sound "audio/glitch.mp3"  # Нужен подходящий звуковой эффект
        narrator "Экран гаснет..." (what_slow_cps=30)
        
        show black_back with Dissolve(0.1)
        pause 0.2
        scene laptops with Dissolve(0.1):
            fit "fill"  # Полное заполнение экрана без сохранения пропорций
        pause 0.1
        show black_back with Dissolve(0.05)
        pause 0.1
        scene laptops with Dissolve(0.05):
            fit "fill"  # Полное заполнение экрана
        pause 0.1
        show black_back with Dissolve(0.1)

        narrator "Пространство колеблется..." (what_slow_cps=30)
        # Дрожание текста
        show smirnov at center_shake
        smir "…Интересно.{w=0.5} Такое ощущение,{w=0.3} что ты что-то знаешь больше,{w=0.3} чем нужно..." (what_slow_cps=15)
        
        # Финал с эффектами
        show black_back with hpunch
        play sound "audio/thunder.mp3"
        pause 0.5
        show text "{size=60}ДОСТУП К СИСТЕМЕ ОГРАНИЧЕН" at truecenter with Dissolve(0.5)
        pause 2.0
        hide text with Dissolve(1.0)
        
        jump chapter5_alt_ending
    else:
        "Мда.. Даже Подольские справились бы лучше..." (what_slow_cps=25)
    jump chapter5_result

label chapter5_result:

    if correct_answers >= 2:
        show nurik at left_side
        narrator "Опрос окончен.. в ожидании оценки.."
        N "Так ну, я вроде норм ответил на 2 вопроса..." (what_slow_cps=25)
        hide nurik with dissolve
        narrator "Нурик, довольный собой, ожидает оценку. Он уверен, что получит как минимум четверку. " (what_slow_cps=25)

        smir "3."

        narrator "... а впрочем, тройка тоже неплохо! Да и завод с каждой секундой кажется всё перспективнее." (what_slow_cps=25)

        $ renpy.call_screen("scr_achievement_get", title="", a_text="На пять знает только Бог, на четыре — преподаватель", icon="images/GERB.png")

        $ rep += 1
        jump end_start
    else:
        narrator "Опрос окончен.. Нурик мысленно молится Вселенной для смягчения удара" (what_slow_cps=25)
        smir "2" (what_slow_cps=15)
        
        narrator "Вселенная его не услышала. Сердце переполняет обида на мир и на Смирнова. Ему нужно выйти поплакать." (what_slow_cps=25)
        hide nurik with dissolve
        narrator "Впрочем, дело сделано: опрос прошел, поэтому можно выдохнуть" (what_slow_cps=25)
        $ rep -= 1
        jump end_start

label chapter5_alt_ending:
    scene black_back with fade
    play music "audio/creepy.mp3" fadein 2.0  # Мрачная музыка
    
    # Постепенно появляющийся текст
    show text "{size=40}СИСТЕМНЫЙ СБОЙ" at truecenter with Dissolve(2.0)
    pause 2.0
    hide text with Dissolve(1.0)
    
    show text "{size=30}Небо становится фиолетовым.\nГравитация перестает работать." at truecenter with Dissolve(1.5)
    pause 3.0
    hide text with Dissolve(1.0)
    
    # Эффект "глюков"
    show glitch_effect with Dissolve(0.5)  # Нужно создать изображение с эффектом глюков
    pause 1.0
    hide glitch_effect with Dissolve(0.5)
    
    # Финальное сообщение
    show text "{size=35}Из недр реальности доносится:\n\n«Пятёрка.{w=0.5} Даже я бы так не ответил.»" at truecenter with Dissolve(1.5)
    pause 3.0
    hide text with Dissolve(2.0)
    
    # Заключительный эффект
    show text "{size=50}ТЫ ВЗЛОМАЛ МАТРИЦУ" at truecenter with vpunch
    pause 3.0
    
    $ rep += 2
    stop music fadeout 3.0
    
    # Добавляем переход к следующей главе
    jump end_start
    
