label stolovaya_start:
    scene black_back
    pause 1.0
    scene stolovaya bg
    narrator "(Систему обхитрить нельзя. Длинная змея очереди тянется с пятого этажа прямиком до библиотеки.)"(what_slow_cps=40)
    show nurik at right with moveinright
    narrator "(Нурик стоит среди них, надеясь успеть поесть до звонка.)"(what_slow_cps=40)
    show nurik at right with hpunch
    narrator "(Кто-то толкает его в плечо, намереваясь влезть в очередь…)"(what_slow_cps=40)
    menu:
        "(Кто-то толкает его в плечо, намереваясь влезть в очередь…)"

        "Ребенок Божий. Пропустить.":
            play sound "savepoint.mp3"
            narrator "(Ребенок Божий. Пропустить.)"(what_slow_cps=40)
            $ terpila = True
        "Наглость – второе имя. Не пропустить.":
            play sound "savepoint.mp3"
            narrator "(Наглость – второе имя. Не пропустить.)"(what_slow_cps=40)
            $ terpila = False
    if terpila:
        show studeent1 at left with moveinright
        N "(Я сегодня добрый. Пусть идёт)"(what_slow_cps=40)
        hide studeent1 with dissolve
        show nurik at right with moveinright
        narrator "(Очередь перед ним увеличивается в геометрической прогрессии. Еще один голодный студент пытается втиснуться в очередь…)"(what_slow_cps=40)

        menu:
            "(Очередь перед ним увеличивается в геометрической прогрессии. Еще один голодный студент пытается втиснуться в очередь…)"

            "Ребенок Божий. Пропустить.":
                play sound "savepoint.mp3"
                narrator "(Ребенок Божий. Пропустить.)"(what_slow_cps=40)
                $ terpila = True
            "Наглость – второе имя. Не пропустить.":
                play sound "savepoint.mp3"
                narrator "(Наглость – второе имя. Не пропустить.)"(what_slow_cps=40)
                $ terpila = False

        if terpila:
            show studeent2 at left with moveinright
            N "(Я хороший. Я хороший. Я хороший.)"(what_slow_cps=40)
            hide studeent2 with dissolve
            narrator "(Кто-то снова толкает Нурика в плечо…)"(what_slow_cps=40)

            menu:
                "(Кто-то снова толкает Нурика в плечо…)"

                "Ребенок Божий. Пропустить.":
                    play sound "savepoint.mp3"
                    narrator "(Ребенок Божий. Пропустить.)"(what_slow_cps=40)
                    $ terpila = True
                "Наглость – второе имя. Не пропустить.":
                    play sound "savepoint.mp3"
                    narrator "(Наглость – второе имя. Не пропустить.)"(what_slow_cps=40)
                    $ terpila = False
            if terpila:
                show studeent3 at left with moveinright
                N "(Просчитался... но где?)"(what_slow_cps=40)
                hide studeent3 with dissolve
                narrator "(Нурик не успел поесть! Теперь он останется  голодным до конца дня.)"(what_slow_cps=40)
                narrator "(А все потому что надо быть умнее и брать еду с собой.)"(what_slow_cps=40)
                narrator "(Расстроенный, он спускается вниз.)"(what_slow_cps=40)
                scene corridor4
                show lexa at right
                show nurik at left with moveinleft
                narrator "(Леша Смоляк, по-королевски усевшись на диван, с удовольствием ест шаурму.)"
                lesha "М-м-м… Вкусвилл мой вкусвилл…"
                narrator "(Есть же на свете еще такие жестокие люди.)"
                play sound "zvonok.mp3"
                narrator "(К сожалению, звенит звонок.)"
            else:
                N "Ага! Еще чо."
                hide nurik with dissolve
                narrator "(Счастливый, Нурик все таки успевает поесть пельмени и блэкстар бургер.)"
                narrator "(Конечно, это не значит, что он останется в добром здравии. Столовая Колледжа Царицыно хранит свои темные секреты…)"
                play sound "zvonok.mp3"
                narrator "(Звенит звонок. Студенты разбредаются вниз по аудиториям.)"

        else:
            N "Ага! Еще чо."
            hide nurik with dissolve
            narrator "(Счастливый, Нурик все таки успевает поесть пельмени и блэкстар бургер.)"
            narrator "(Конечно, это не значит, что он останется в добром здравии. Столовая Колледжа Царицыно хранит свои темные секреты…)"
            play sound "zvonok.mp3"
            narrator "(Звенит звонок. Студенты разбредаются вниз по аудиториям.)"

    else:
        N "Ага! Еще чо."
        hide nurik with dissolve
        narrator "(Счастливый, Нурик все таки успевает поесть пельмени и блэкстар бургер.)"
        narrator "(Конечно, это не значит, что он останется в добром здравии. Столовая Колледжа Царицыно хранит свои темные секреты…)"
        play sound "zvonok.mp3"
        narrator "(Звенит звонок. Студенты разбредаются вниз по аудиториям.)"
        



