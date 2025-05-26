image stolovaya = "bg/eatery/stolovaya_bg.png"
image studeent1 = Transform( "characters/studeent1.png", zoom = 0.8)
image studeent2 = Transform( "characters/studeent2.png", zoom = 0.6)
image studeent3 = Transform( "characters/studeent3.png", zoom = 1)

label stolovaya_start:
    play music "main_theme.mp3"
    scene black_back
    pause 1.0
    scene stolovaya with fade:
        fit "contain"
    narrator "Систему обхитрить нельзя. Длинная змея очереди тянется с пятого этажа прямиком до библиотеки."(what_slow_cps=40)
    show nurik at left_side1
    narrator "Нурик стоит среди них, надеясь успеть поесть до звонка."(what_slow_cps=40)
    show nurik at left_side1 with hpunch
    narrator "Кто-то толкает его в плечо, намереваясь влезть в очередь…"(what_slow_cps=40)
    menu:
        "Кто-то толкает его в плечо, намереваясь влезть в очередь…"

        "Ребенок Божий. Пропустить.":
            play sound "savepoint.mp3"
            narrator "Ребенок Божий. Пропустить."(what_slow_cps=40)
            $ terpila = True
        "Наглость – второе имя. Не пропустить.":
            hide nurik 
            show nurik_angry at left_side with dissolve
            play sound "savepoint.mp3"
            narrator "Наглость – второе имя. Не пропустить."(what_slow_cps=40)
            $ terpila = False
    if terpila:
        hide nurik_angry
        show nurik at left_side1
        show studeent1 at left with moveinright
        N "(Я сегодня добрый. Пусть идёт)"(what_slow_cps=40)
        hide studeent1 with dissolve
        show nurik at left_side1
        narrator "Очередь перед ним увеличивается в геометрической прогрессии. Еще один голодный студент пытается втиснуться в очередь…"(what_slow_cps=40)

        menu:
            "Очередь перед ним увеличивается в геометрической прогрессии. Еще один голодный студент пытается втиснуться в очередь…"

            "Ребенок Божий. Пропустить.":
                play sound "savepoint.mp3"
                narrator "Ребенок Божий. Пропустить."(what_slow_cps=40)
                $ terpila = True
            "Наглость – второе имя. Не пропустить.":
                hide nurik 
                show nurik_angry at left_side with dissolve
                play sound "savepoint.mp3"
                narrator "Наглость – второе имя. Не пропустить."(what_slow_cps=40)
                $ terpila = False

        if terpila:
            hide nurik_angry
            show nurik at left_side1
            show studeent2 at left with moveinright
            N "(Я хороший. Я хороший. Я хороший.)"(what_slow_cps=40)
            hide studeent2 with dissolve
            narrator "Кто-то снова толкает Нурика в плечо…"(what_slow_cps=40)

            menu:
                "Кто-то снова толкает Нурика в плечо…"

                "Ребенок Божий. Пропустить.":
                    play sound "savepoint.mp3"
                    narrator "Ребенок Божий. Пропустить."(what_slow_cps=40)
                    $ terpila = True
                "Наглость – второе имя. Не пропустить.":
                    hide nurik 
                    show nurik_angry at left_side with dissolve
                    play sound "savepoint.mp3"
                    narrator "Наглость – второе имя. Не пропустить."(what_slow_cps=40)
                    $ terpila = False
            if terpila:
                hide nurik_angry
                show nurik at left_side1
                show studeent3 at left with moveinright
                N "(Просчитался... но где?)"(what_slow_cps=40)
                hide studeent3 with dissolve
                narrator "Нурик не успел поесть! Теперь он останется  голодным до конца дня."(what_slow_cps=40)
                narrator "А все потому что надо быть умнее и брать еду с собой."(what_slow_cps=40)
                narrator "Расстроенный, он спускается вниз."(what_slow_cps=40)
                scene corridor1 with fade:
                    fit "contain"
                show lexa at right
                show nurik at left_side1
                $ rep -= 1
                narrator "Леша Смоляк, по-королевски усевшись на диван, с удовольствием ест шаурму."
                l "М-м-м… Вкусвилл мой вкусвилл…"
                narrator "Есть же на свете еще такие жестокие люди."
                play sound "zvonok.mp3"
                narrator "К сожалению, звенит звонок."
                play sound "xbox.mp3"
                $ renpy.call_screen("scr_achievement_get", title="Он терпел", a_text="И нам велел", icon="GERB.png")
            else:
                hide nurik 
                show nurik_angry at left_side with dissolve
                N "Ага! Еще чо."
                hide nurik with dissolve
                $ rep += 1
                narrator "Счастливый, Нурик все таки успевает поесть пельмени и блэкстар бургер."
                narrator "Конечно, это не значит, что он останется в добром здравии. Столовая Колледжа Царицыно хранит свои темные секреты…"
                play sound "zvonok.mp3"
                narrator "Звенит звонок. Студенты разбредаются вниз по аудиториям."

        else:
            hide nurik 
            show nurik_angry at left_side with dissolve
            N "Ага! Еще чо."
            $ rep += 1
            hide nurik with dissolve
            narrator "Счастливый, Нурик все таки успевает поесть пельмени и блэкстар бургер."
            narrator "Конечно, это не значит, что он останется в добром здравии. Столовая Колледжа Царицыно хранит свои темные секреты…"
            play sound "zvonok.mp3"
            narrator "Звенит звонок. Студенты разбредаются вниз по аудиториям."

    else:
        hide nurik 
        show nurik_angry at left_side with dissolve
        N "Ага! Еще чо."
        hide nurik with dissolve
        $ rep += 1
        narrator "Счастливый, Нурик все таки успевает поесть пельмени и блэкстар бургер."
        narrator "Конечно, это не значит, что он останется в добром здравии. Столовая Колледжа Царицыно хранит свои темные секреты…"
        play sound "zvonok.mp3"
        narrator "Звенит звонок. Студенты разбредаются вниз по аудиториям."
jump chapter3_start 


