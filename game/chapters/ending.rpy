label ending_start:
    play music "main_theme.mp3"
    scene black_back with fade
    pause 1.0
    narrator "Тяжелый день наконец-то подходит к концу." (what_slow_cps=25)
    narrator "Усталость сменяется умиротворением, как только Нурик выходит из здания и делает глубокий вдох." (what_slow_cps=25)
    
    if (rep > -5):
        jump good_rep
    else:
        jump bad_rep

image bad_end = "bg/end/col_titr.png"

label good_rep:
    scene college_end with fade:
        fit "contain"
    narrator "В будущем Нурик обязательно станет успешным программистом." (what_slow_cps=25)
    narrator "Он будет получать много-много денег, а работать с графиком 2-2: два дня отдыха и два часа работы." (what_slow_cps=25)
    narrator "Может быть, Нурик даже накопит себе на путевку в санаторий и на место на кладбище в замечательном городе Нукус."
    narrator "И заживет он долго и счастливо."
    jump titr_start

label bad_rep:
    narrator"Возможно, в будущем Нурик кем-то станет." (what_slow_cps=25)
    narrator "Может быть, даже кем-то по специальности: помогать бабушкам устанавливать винду тоже важное занятие. " (what_slow_cps=25)
    narrator "Он оборачивается на колл- а где колледж? " (what_slow_cps=25)
    scene bad_end with fade:
        fit "contain"
    show nurik_udivil at left_side with hpunch
    N "(Язык хештегов)?! Что случилось?" (what_slow_cps=25)
    narrator "Ого! Нурик так сильно облошмотился, что колледж не выдержал." (what_slow_cps=25)
    narrator "Милый, дорогой ОУИТ..." (what_slow_cps=25)
    hide nurik_udivil
    show nurik_sad at left_side1
    N "..пропал!" (what_slow_cps=25)
    scene black_back with fade
    show text "Плохая концовка."
    pause 1.0
    jump titr_start

label chit_end:
    scene black_back
    narrator "Тяжелый день наконец-то подходит к концу." (what_slow_cps=25)
    narrator "Усталость сменяется умиротворением, как только Нурик выходит из здания и делает глубокий вдох." (what_slow_cps=25)
    
    scene end_chit with fade:
        fit "contain"
    narrator "Никто не ожидал, но в будущем Нурик не покинет колледж Царицыно." (what_slow_cps=25)
    narrator "Он станет преподавателем здесь же. Будет кошмарить студентиков, как когда-то кошмарили его… Все циклично." (what_slow_cps=25) 
    play sound "xbox.mp3"
    $ renpy.call_screen("scr_achievement_get", title="", a_text="Из Царицынска не сбежать", icon="GERB.png")
    scene black_back with fade
    show text "Секретная концовка."
    pause 1.0
    jump titr_start

label titr_start:
    play music "gimn.mp3"
    scene black with fade
    with Pause(1.0)

    show screen credits_scroll

    $ renpy.pause(40.0)  # Время прокрутки титров

    hide screen credits_scroll
    with fade

    $ renpy.full_restart()



# --- ЭКРАН С ПРОКРУТКОЙ ТИТРОВ ---
screen credits_scroll:
    frame:
        background None
        xalign 0.5
        yanchor 0.0  # Крепление в верхней части фрейма
        ypos 1.5
        at scroll_up

        vbox:
            spacing 40
            text "Благодарности:" size 40 color "#FFFFFF" xalign 0.5

            text "Нурику – главному герою, спасителю колледжа Царицыно" size 30 color "#FFFFFF" xalign 0.5
            text "Алине – главной по слиянию веток и по мемам" size 30 color "#FFFFFF" xalign 0.5
            text "Варваре – крутой сценаристке, писательнице фанфиков" size 30 color "#FFFFFF" xalign 0.5
            text "Полине – хрю хрю хрю душе компании" size 30 color "#FFFFFF" xalign 0.5
            text "Стефану – какому-то хиппи диджею" size 30 color "#FFFFFF" xalign 0.5
            
            text ""  # пустая строка для пространства
            text "Елене Ивановне – за участие и разрешение сделать новеллу" size 30 color "#FFFFFF" xalign 0.5
            text "Светлане Владимировне – за участие" size 30 color "#FFFFFF" xalign 0.5
            text "Елизавете Александровне – за участие" size 30 color "#FFFFFF" xalign 0.5
            text "Дмитрию Ильичу – за участие" size 30 color "#FFFFFF" xalign 0.5
            text "Евгению Михайловичу – за участие" size 30 color "#FFFFFF" xalign 0.5

            text ""  # пустая строка для пространства
            text "Языку хештегов - верному товарищу, который был всегда рядом" size 30 color "#FFFFFF" xalign 0.5
            text "Столовой ОУИТ - очереди в которую не такие уж и большие" size 30 color "#FFFFFF" xalign 0.5
            text "Протекающему потолку - за вдохновение" size 30 color "#FFFFFF" xalign 0.5
            text "Каширской плазе - любимому зданию за существование" size 30 color "#FFFFFF" xalign 0.5
            text "Синим диванчикам – уютному кусочку рая в этом месте" size 30 color "#FFFFFF" xalign 0.5  
            

            text ""  # пустая строка для пространства
            text "В память к ОУИТу" size 36 color "#FFFFFF" xalign 0.5

            text ""  # пустая строка для пространства
            text "Спасибо за игру!" size 36 color "#FFFFFF" xalign 0.5

            text ""  # ещё пустая строка
            text ""


# --- ТРАНСФОРМ ДЛЯ ПОДЪЕМА ТЕКСТА ---
transform scroll_up:
    ypos 1.7
    linear 50.0 ypos -2.0