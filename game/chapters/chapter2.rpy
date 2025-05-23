
init python:
    
    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    config.automatic_images_minimum_components = 1
    config.automatic_images = [' ', '_', '/']
    config.automatic_images_strip = ["images"]
    oXY = []
    oN = []
    oLen = 0
    maxLen = 0
    oBg = ""
    oLast = -1
    oTime = 50.0
    oMaxTime = 500.0
    needTimer = False
    oActive = False
    oRes = False

    def InitGame(bg, time, *args):
        global oBg, oXY, oN, oLen, maxLen, oLast, oTime, oMaxTime, oActive, needTimer, oRes
        oXY = []
        oN = []
        oLen = 0
        oBg = bg
        oLast = -1
        oTime = time
        oMaxTime = time
        maxLen = 0
        oActive = True
        oRes = False
        if oTime > 0.0:
            needTimer = True
        for xy, obj_name in zip(args[0::2], args[1::2]):
            oXY.append(xy)
            oN.append(obj_name)
            maxLen += 1

    def StartGame():
        global oActive
        oActive = True
        need = True
        while need:
            renpy.call_screen("game", _layer="master")
            need = oRes == False
            if needTimer and (oTime <= .0):
                need = False


    def GameAsBG():
        global oActive
        oActive = False
        renpy.show_screen("game", _layer="master")

    def o_click(i):
        global oLen, oRes
        if i >= 0:
            if oN[i]:
                temp = oN[i]
                oN[i] = ""
                oLen += 1
                renpy.play("sounds/click.mp3", channel="sound")
                renpy.restart_interaction()
                if needTimer:
                    if oLen >= maxLen:
                        oRes = True
                else:
                    oRes = temp
    oClick = renpy.curry(o_click)

screen game:
    modal True
    if oActive and needTimer:
        timer 0.01 repeat True action [SetVariable("oTime", oTime-.01), If(oTime <= .0, true=[Return()])]
    add oBg
    for i in range(0, len(oN)):
        if oN[i]:
            imagebutton:
                focus_mask True
                pos(oXY[i])
                idle oN[i]
                hover oN[i]
                if oActive:
                    action [oClick(i), Return()]
                else:
                    action []


label chapter2_start:
    scene black_back
    play sound "undertale.mp3"
    show text "{color=#ffffff}Глава 3: Кульминация{/color}" at truecenter with dissolve

    pause 3.0

    hide text with dissolve
    show text "{color=#ffffff}103 кабинет{/color}" at truecenter with dissolve

    pause 3.0

    hide text with dissolve

    scene em kab1
    play music "main_theme.mp3"

    show girl1 at right

    girl1 "…и именно поэтому я считаю, что (язык хештегов) в общественном месте – это норма."(what_slow_cps=40)

    show nurik at left with moveinleft

    narrator "(Все аплодируют. Нурик все еще стоит в дверях, пытаясь понять, что здесь происходит.)"(what_slow_cps=40)
    narrator "(Студенты другой группы улыбаются, принимая овации.)"(what_slow_cps=40)
    narrator "(Все, кажется, слишком вовлечены в необычное мероприятие, чтобы заметить его опоздание.)"(what_slow_cps=40)

    scene em kab2 with dissolve

    show nurik at right with moveinright

    narrator "(Нурик садится за свое место и открывает ноутбук.)"(what_slow_cps=40)
    narrator "(Никто бы не мог подумать, но оказывается, тесты на айкью слишком энергозатратны.)"(what_slow_cps=40)

    N "(Нужно зарядить ноутбук.)"(what_slow_cps=40)

    narrator "(Колледж Царицыно на саперов никого не обучал, но распутывание проводов – приобретенный софт скилл.)"(what_slow_cps=40)

    scene black_back

    show dev yap

    dev "Тут типа должна быть миниигра..."(what_slow_cps=40)
    dev "...Но мне лень"(what_slow_cps=40)
    dev "Пока-пока"(what_slow_cps=40)

    scene em kab2

    show emel with dissolve

    emelina "Задание я скинула в группу. Тем, у кого точки – нужно доделать девятую практическую до завтра."(what_slow_cps=40)

    hide emel with dissolve

    show nurik at left with moveinleft

    narrator "(Гул недовольства охватывает аудиторию.)"(what_slow_cps=40)
    narrator "(Вторая пара тоже еще слишком рано для настоящей работы. К тому же, в аудитории душно.)"(what_slow_cps=40)
    narrator "(Все, за что уплочено – должно быть проглочено… Точнее, деньги, выделенные на отопление, должны быть использованы.)"(what_slow_cps=40)

    stud1 "Кто тут душный такой? Выйдите."(what_slow_cps=40)

    stud2 "Да ну откройте окно уже."(what_slow_cps=40)

    stud3 "Да, Нурик, открой окно."(what_slow_cps=40)

    narrator "(Нелегко быть студентом.)"(what_slow_cps=40)
    narrator "(Несчастный работяга встает, чтобы открыть окно – но вот загвоздка. Ручки от окна нигде нет.)"(what_slow_cps=40)
    scene em kab2
    $ InitGame("em kab2", 120, (715, 660), "handle")
    $ StartGame()
    hide nurik
    show handly with dissolve
    N "Я нашёл ручку"

    hide handly with dissolve
    show nurik at left with moveinleft

    narrator "(Найдя ручку Нурик открыл окно.)"(what_slow_cps=40)
    narrator "(Погода на улице хорошая. Прохлада наполняет кабинет и даже работать становится легче.)"(what_slow_cps=40)
    narrator "(Все идет хорошо: студентики ломают друг другу приложения и незаметно скатывают с гпт...)"(what_slow_cps=40)

    stud4 "Закройте окно, мне дует."(what_slow_cps=40)

    narrator "(Воистину, колледж – это миниатюра на жизнь всецело. Вполне напоминает электричку в разгар июля.)"(what_slow_cps=40)
    narrator "(Пока всем жарко – всегда найдется тот, кому в +30 холодно.)"(what_slow_cps=40)
    narrator "(Как обычно, нелегкая доля выпадает Нурику. Ну, по крайней мере сейчас то ручку искать не придется.)"(what_slow_cps=40)
    narrator "(Кто-то явно согласен с общепринятой точкой зрения, потому что ручка вновь пропала.)"(what_slow_cps=40)

    show polina photo at right with moveinright
    
    polina "Домовой-домовой, поиграл и отдай."(what_slow_cps=40)

    narrator "(Если бы это работало именно так, то стипендия приходила бы вовремя.)"(what_slow_cps=40)
    scene em kab2
    $ InitGame("poisk", 120, (500, 550), "handle2")
    $ StartGame()
    hide polina photo
    hide nurik
    show handly with dissolve
    N "Я нашёл ручку"
    hide handly with dissolve
    show nurik at left with moveinleft

    narrator "(Найдя ручку Нурик открыл закрыл.)"(what_slow_cps=40)

    scene em kab1

    narrator "(Голодные студентики слезно умоляют Елену Ивановну отпустить их пораньше в столовую.)"(what_slow_cps=40)

    show emel at right with moveinright

    emelina "Ну ладно, идите… Так вот, в Калязине очень интересно посмотреть на-"(what_slow_cps=40)

    hide emel with dissolve

    narrator "(Воспользовавшись возможностью, Нурик уходит с остальными. Каждая секунда на счету.)"(what_slow_cps=40)
    narrator "(Кто-то в коридоре уже бежит, надеясь миновать очередь.)"(what_slow_cps=40)
    narrator "(Глупцы…)"(what_slow_cps=40)

    jump stolovaya_start