init python:
    # Центрирование текста рассказчика
    style.narrator_dialogue = Style(style.default)
    style.narrator_dialogue.xalign = 0.5
    style.narrator_dialogue.text_align = 0.5
    rep = 0

style window:
    ypos 1080
    xsize 2000
    ysize 240
    background Frame("gui/textbox.png", 25, 25)

define narrator = Character(
    None,
    kind=adv,
    what_slow_cps=20,
    window_style="window",
    what_style="narrator_dialogue"
)

define SV = Character('Светлана Владимировна', image="mitrosha", color="#CE0071", what_slow_cps=20, window_style="window")
define nurik = Character('Нурик', image="nurik", what_slow_cps=20, window_style="window")
define P = Character('Полина', image="mitrosha", what_slow_cps=20, window_style="window")
define V = Character('Варя', image="slavka", what_slow_cps=20, window_style="window")
define A = Character('Алина', image="jarka", what_slow_cps=20, window_style="window")

image SV = Transform("characters/kiseleva.png", zoom = 1)
image kab_kis = "bg/lesson_kiseleva/cab_kis.png"
image polina = Transform("characters/small_polina.png", zoom=1.5)
image polina_deb = Transform("characters/small_polina_deb.png", zoom=1.5)
image nurik_angry = Transform("characters/nuric_angry.png", zoom=0.66)
image nurik_udivil = Transform("characters/Nur_udivil.png", zoom=0.7)
image nurik_sad = "characters/nurik_sad.png"

image varya = Transform("characters/varya.png", zoom = 0.8)
image alina = "characters/alina.png"
image black_back = "#000000"
image test_bg = "test_bg.png"
image posit_res = "pos_res.png"
image negat_res = "neg_res.png"




transform right_side:
    xalign 0.95
    yalign 1.0

transform slide_down:
    ypos -100  # Начинается выше экрана
    linear 0.5 ypos 50  # Плавно опускается вниз
    pause 2.0  # Висит 2 секунды
    linear 0.5 ypos -100  # Плавно уезжает вверх

label para1_start:
    play music "main_theme.mp3"
    scene black_back
    call para1_Enter_scene
    call para1_Polina_scene

label para1_Enter_scene:
    
    narrator "Нурик открывает дверь кабинета." (what_slow_cps=30)
    narrator "К счастью, ручку двери наконец починили." (what_slow_cps=30)

    scene kab_kis with fade:
        fit "contain"
    return

label para1_Polina_scene:
    show SV at right_side with dissolve
    SV "Друг-подружка! Опять опоздал? Ладно, тебе все можно." (what_slow_cps=30)
    hide SV with dissolve

    narrator "Нурик улыбается и проходит внутрь. Несчастные его одногруппники (их жалкое количество) здороваются с ним. Вот они – слева направо…" (what_slow_cps=30)
    narrator "Полина машет ему рукой. Затем, со всем ее талантом актерского мастерства она указывает на его кроссовки." (what_slow_cps=30)

    show polina at right_side with dissolve
    P "Ха! А у тебя шнурки развязаны!" (what_slow_cps=30)

    menu:
        "Поверить":
            play sound "savepoint.mp3"
            narrator "Нурик недоверчиво опускает голову вниз." (what_slow_cps=30)
            show nurik at left_side1 with dissolve
            nurik "Странно, но они не-" (what_slow_cps=30)
            hide polina 
            show polina_deb at right_side
            narrator "Полина щелкает его по носу с гордостью." (what_slow_cps=30)
            hide polina_deb with dissolve
            play sound "xbox.mp3"
            $ renpy.call_screen("scr_achievement_get", title="Простофиля", a_text="Ошибка новичка.", icon="GERB.png")
        "Не поверить":
            play sound "savepoint.mp3"
            show nurik_angry at left_side with dissolve
            nurik "Так я тебе и поверил." (what_slow_cps=30)
            hide polina
            
            show polina_deb at right_side
            narrator "Полина наклоняется и быстро развязывает шнурки на его кроссовках." (what_slow_cps=30)
            hide nurik_angry
            show nuric_what at left_side1 
            narrator "Ну, по крайней мере она не соврала. Теперь они действительно развязаны. Честная крымская девочка." (what_slow_cps=30)
            hide polina_deb 
            play sound "xbox.mp3"
            $ renpy.call_screen("scr_achievement_get", title="Первое правило леса", a_text="Никому не доверять!", icon="GERB.png")

    narrator "Шум смеха привлекает внимание Светланы Владимировны." (what_slow_cps=30)
    hide polina_deb
    hide nuric_what 
    show SV at right_side
    SV "Нурик! А ну не мешай девчатам. Делайте задание." (what_slow_cps=30)
    hide SV
    hide nurik
    show nurik_udivil at left_side with dissolve
    nurik "(Капец, а у нас что, есть задание...)" (what_slow_cps=30)
    hide nurik_udivil
    narrator "Нурик достает ноутбук. Но в его сердце все еще остается надежда на страдания в меньшем размере." (what_slow_cps=30)
    narrator "Например, на валяние дурака." (what_slow_cps=30)

    menu:
        "Предложить Варе поиграть в пабг":
            play sound "savepoint.mp3"
            narrator "Отличная затея." (what_slow_cps=30)
            narrator "Нурик поворачивается к Варе." (what_slow_cps=30)
            show nurik at left_side1 with dissolve
            nurik "Пошли в пабг?" (what_slow_cps=30)
            show varya at right_side with dissolve
            V "Ты дурааа? У меня нет с собой планшетааа." (what_slow_cps=30)
            hide varya with dissolve
            narrator "Удача сегодня не на его стороне. Приходится включать ноутбук…" (what_slow_cps=30)

            jump turn_on_laptop

        "Включить ноутбук":
            play sound "savepoint.mp3"
            jump turn_on_laptop
    
    
default player_iq = 0

label turn_on_laptop:
    narrator "Ноутбук включается. Слава богу винда не слетела! Лишь бы не сглазить." (what_slow_cps=30)
    show nurik at left_side1 with dissolve
    nurik "(Блин, ну еще рано… я еще глаза не открыл толком. Можно особо не стараться.)" (what_slow_cps=30)
    narrator "Ну, задание вроде не особо сложное …" (what_slow_cps=30)
    narrator "Ошибка длинным, красным сообщением заполняет весь экран Jupyter Notebook'а." (what_slow_cps=30)
    nurik "(Язык хештегов)" (what_slow_cps=30)
    nurik "Алина-а-а. А у тебя была такая ошибка?" (what_slow_cps=30)
    narrator "Алина справа от него пожимает плечами." (what_slow_cps=30)
    show alina at right_side with dissolve
    A "НуУу ууу аААММММ Хз. Загугли." (what_slow_cps=30)
    narrator "Мудрый совет. У программиста нет цели – только бесконечное плавание в попытке найти, как исправить ошибку." (what_slow_cps=30)
    hide alina with dissolve
    
    narrator "Нурик заходит в Яндекс" (what_slow_cps=30)
    scene test_bg with fade:
        fit "contain"
    nurik "О, айкью тест." (what_slow_cps=30)
    narrator "Нурик доверчиво нажимает на ссылку." (what_slow_cps=30)

    scene black_back with fade
    pause 1.0
    
    jump question_1

# тут должен быть мемный фон
label question_1:
    scene test_bg with fade:
        fit "contain"
    menu:
        "1. За сколько минут надо уйти с пары в столовую?"
        
        "10":
            "А ты научен жизнью! Вот только никто тебя не отпустит."
        
        "Сразу после звонка":
            "Ты не успеешь. Ты точно учишься в Царицынске?"
        
        "Без разницы":
            $ player_iq += 15
            "Правильно! Ты все равно не успеешь."
        
        "За год до поступления":
            "Хорошая попытка."
    
    jump question_2

# Вопрос 2
label question_2:
    menu:
        "2. Сколько этажей в Царицыно?"
        
        "6":
            $ player_iq += 15
            "Это правильно."
        
        "5":
            "А как же фотостудия..."
        
        "4":
            "А как же пролет..."
        
        "3":
            "Позор Царицыно."
    
    jump question_3

# Вопрос 3
label question_3:
    menu:
        "3. Ваше расписание: физкультура, философия, английский, высшая математика. К какой паре нужно придти?"
        
        "К первой":
            "Окак."
        
        "Ко второй":
            "Окак."
        
        "К третьей":
            "Окак."
        
        "Не приходить":
            $ player_iq += 15
            "Правильный ответ!"
    
    jump question_4

# Вопрос 4
label question_4:
    menu:
        "4. Как расшифровывается ОУИТ?"
        
        "Отделение управления информационными технологиями.":
            $ player_iq += 15
            "Верно."
        
        "Отдел управлениями информационными технологиями.":
            "Неверно."
        
        "ОУИТ":
            "Окак."
        
    
    jump question_5

# Вопрос 5
label question_5:
    menu:
        "5. Где протекает потолок в колледжe Царицыно?"
        
        "Актовый зал":
            "Это верно, но не совсем."
        
        "Холл":
            "Это верно, но не совсем."
        
        "Везде":
            $ player_iq += 15
            "Да."
    
    jump question_6

# Вопрос 6
label question_6:
    menu:
        "6. Расшифруйте ЕЕИ."
        
        "ЕЕЕ Еду Иду":
            "Нет."
        
        "Емелина Елена Ивановна":
            $ player_iq += 15
            "Да."
        
        "Емелина Елена Ивановна":
            "Да, но баллов не дадут."
        
        "Емелина Елена Ивановна":
            "Да, но баллов не дадут."
    
    jump question_7

# Вопрос 7
label question_7:
    menu:
        "7. Чьи кабинеты в сумме дают 325?"
        
        "Першунина, Емелина, Ковалева":
            "Нет."
        
        "Сниховская, Ларионов, Ефимова":
            "Нет."
        
        "Ковалева, Климова, Смирнов":
            "Нет."
        
        "Сниховская, Ковалева, Смирнов":
            $ player_iq += 20
            "Да."
    

    scene black_back with fade
    jump results

label results:
    if player_iq >= 80:
        $ rep += 1
        jump pos_res
    else:
        $ rep -= 1
        jump otr_res

label pos_res:
    scene posit_res with fade:
        fit "contain"
    pause 3.0
    scene cab_kis with fade:
        fit "contain"
    show SV at right_side with dissolve
    SV "Ну что, друзьяшки, сделали задание?" (what_slow_cps=30)
    hide SV with dissolve
    narrator "Тесты на айкью никогда не врут! Нурик списывает задание у Алины..." (what_slow_cps=30)
    narrator "...Варя списывает задание у Нурика..." (what_slow_cps=30)
    narrator "...Полине никто не дал списать, поэтому она косится на завязанные шнурки своих одногруппников в качестве мести." (what_slow_cps=30)
    scene black_back with fade
    jump end_of_para

label otr_res:
    scene negat_res with fade:
        fit "contain"
    pause 3.0
    narrator "Все вокруг осуждающе поднимают бровь." (what_slow_cps=30)
    scene cab_kis with fade:
        fit "contain"

    show polina at left_side with dissolve
    P "Может тебе в ЗЕУ перевестись?" (what_slow_cps=30)
    scene black_back with fade

    show text "Спустя некоторое время..." at truecenter with fade
    pause 2.0  
    hide text with dissolve 

    scene cab_kis with fade:
        fit "contain"

    show SV at right_side with dissolve
    SV "Ну что, друзьяшки, сделали задание?" (what_slow_cps=30)
    show nurik at left_side1 with dissolve
    nurik "Неет, я не успел." (what_slow_cps=30)
    narrator "Светлана Владимировна вздыхает." (what_slow_cps=30)
    SV "Ну что ты меня подводишь, друг-подружка. Вот как посажу тебя на весь день в свой кабинет..." (what_slow_cps=30)
    scene black_back with fade
    jump end_of_para

label end_of_para:
    narrator "Наконец, звенит звонок. Все с кратковременным облегчением выходят в коридор." (what_slow_cps=30)
    #$ renpy.notify(f"Текущая репутация: {rep}")  
    
    scene black_back with fade
    pause 1.0
  
    jump peremena1_start