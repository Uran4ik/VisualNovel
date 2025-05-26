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

define nurik = Character('Нурик', image="nurik", what_slow_cps=20, window_style="window")


image nurik = "characters/nurik.png"
image cor1 = "bg/corridor/corridor1.png"
image cor2 = "bg/corridor/corridor2.png"
image cor3 = "bg/corridor/corridor5.png"
image cor4 = "bg/corridor/corridorrrr.png"
image black_back = "#000000"



transform left_side:
    xalign 0.05
    yalign 1.16

transform right_side:

    xalign 0.95
    yalign 1.0

transform slide_down:
    ypos -100  # Начинается выше экрана
    linear 0.5 ypos 50  # Плавно опускается вниз
    pause 2.0  # Висит 2 секунды
    linear 0.5 ypos -100  # Плавно уезжает вверх

label peremena1_start:
    scene black_back
    call peremena1_Enter_scene

label peremena1_Enter_scene:

    scene black_back with fade
    
    nurik "Пить хочется…"

    jump choice_scene

label choice_scene:
    menu:
        "Поискать воду в коридоре у сотых кабинетов":

            scene cor2 with fade:
                fit "contain"

            narrator "Нурик спускается на этаж ниже."
            narrator "К сожалению, кулера здесь нет… Стоило запомнить, что бюджет не резиновый."
           
            $ rep -= 1
            # $ renpy.notify(f"Текущая репутация: {rep}")

            scene black_back with fade

            jump choice_cups_scene
           

        "Поискать воду в коридоре у трехсотых кабинетов.":
            scene cor1 with fade:
                fit "contain"

            narrator "Нурик огибает половину колледжа, чтобы дойти до коридора у трехсотых кабинетов."
            narrator "Спасительным оазисом кулер возвышается памятником спасения."
            narrator "О нет, здесь нет стаканчиков!"

            $ rep += 1
            # $ renpy.notify(f"Текущая репутация: {rep}")

            scene black_back with fade

            jump choice_cups_scene

label choice_cups_scene:
    menu:
        "Поискать стаканчики в коридоре у четырехсотых кабинетов.":
            scene cor4 with fade:
                fit "contain"

            narrator "О, вкусняшка. Нурик нашел стаканы. Осталось вновь спуститься вниз и успеть побороться за воду."
            $ rep += 1
            # $ renpy.notify(f"Текущая репутация: {rep}")

            scene black_back with fade

            jump end_peremena1
        
        "Поискать стаканчики в коридоре у двухсотых кабинетов.":
            scene cor3 with fade:
                fit "contain"

            narrator "Нурик возвращается туда, откуда пришел."
            narrator "Надо было смотреть по сторонам. Стаканчиков здесь нет."

            $ rep -= 1
            # $ renpy.notify(f"Текущая репутация: {rep}")

            scene black_back with fade

            jump end_peremena1

label end_peremena1:
    scene cor1 with fade:
        fit "contain"
    
    narrator "Попробовать найти воду в колледже “Царицыно” похоже на голодные игры."
    narrator "Нурик так долго искал воду, что прозвенел звонок. Теперь ему нужно добраться до 103 кабинета."

    $ renpy.call_screen("scr_achievement_get", title="Голодные игры", a_text="И пусть удача всегда будет с вами!", icon="GERB.png")

    scene black_back with fade
    pause 1.0

    jump chapter2_start

            

