# $ renpy.call_screen("scr_achievement_get", title="Тест", a_text="Экран работает", icon="gui/icon.jpg")
init python: #эта фигня не работает вы отсюда ачивки не вызовете создавайте их через выше написала но файл нужен
    def init_achievements(): 
        if not hasattr(persistent, "achievements_dict") or not persistent.achievements_dict:
            persistent.achievements_dict = {
                "odin": {
                    "type": 0,
                    "title": "Первое достижение",
                    "text": "Ты получил первую ачивку!",
                    "icon": Solid("#00f")
                },
                "progress_example": {
                    "type": 1,
                    "title": "Прогресс!",
                    "text": "Набери максимум!",
                    "icon": "images/bg/lesson_emelina/ruchka_poisk1.png",
                    "cur_prog": 0,
                    "max_prog": 5
                }
            }

        for ach_id, ach in persistent.achievements_dict.items():
            if ach['type'] == 0:
                achievement.register(ach_id, steam=ach['title'])
            elif ach['type'] == 1:
                achievement.register(ach_id, steam=ach['title'], stat_max=ach['max_prog'])


label before_main_menu:
    $ init_achievements()
    return


transform achievement_transform:
    on show:
        xalign .95
        yalign -.3 
        linear 0.4 xalign .95 yalign .02
    on hide:
        linear 0.4 xalign 0.95 yalign -.3


screen scr_achievement_get(title, a_text, icon):
    zorder 120
    window:
        at achievement_transform
        background Transform("images/achiv_pix.png", xysize=(500, 200))

        xalign .90
        yalign .02
        xysize (450, 100)
        hbox:
            vbox:
                spacing 10
                yoffset 60
                xoffset 20
                image icon:
                    size (100, 100)
            vbox:
                xoffset 40
                yoffset 50
                xsize 330
                text title:
                    size 28
                    color "#000000"
                text a_text:
                    size 22
                    color "#000000"
    key "mouseup_1" action Return() 
    timer 2.5 action Return() 


# Прогресс достижения timer 2.5 or 
screen scr_achievement_update(title, a_text, icon, cur_prog, max_prog, trans=achievement_transform):
    zorder 120
# timer 2.4 action Hide("scr_achievement_update")
    window:
        at trans
        background Transform("images/achiv_pix.png", xysize=(500, 200))
        xalign .90
        yalign .02
        xysize (450, 100)
        hbox:
            vbox:
                spacing 10
                image icon
                text "{}/{}".format(cur_prog, max_prog):
                    xcenter 0.5 
                    ycenter 0.2
            vbox:
                xoffset 10
                xsize 330
                text title:
                    size 28
                text a_text:
                    size 22

init python:

    def get_achievement(ach_id):
       
        if ach_id not in persistent.achievements_dict:
            renpy.log("Achievement '{}' не найден.".format(ach_id))
            return     
        achievement.grant(ach_id)
        renpy.call_in_new_context("_show_achievement_screen", ach_id)



    def update_achievement(ach_id, to_add=1, trans=achievement_transform):
        ach = persistent.achievements_dict.get(ach_id, None)
        if not ach or ach["type"] != 1:
            renpy.log("Прогресс достижение '{}' не найдено или не является прогрессом.".format(ach_id))
            return

        ach["cur_prog"] += to_add
        if ach["cur_prog"] > ach["max_prog"]:
            ach["cur_prog"] = ach["max_prog"]

        achievement.progress(ach_id, to_add)

        renpy.show_screen("scr_achievement_update", title=ach["title"], a_text=ach["text"],
                        icon=ach["icon"], cur_prog=ach["cur_prog"], max_prog=ach["max_prog"], trans=trans)

label _show_achievement_screen(ach_id):
    $ ach = persistent.achievements_dict[ach_id]
    show screen scr_achievement_get(title=ach["title"], a_text=ach["text"], icon=ach["icon"])
    pause 2.5
    hide screen scr_achievement_get
    return
