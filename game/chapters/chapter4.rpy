init python:
    # Счётчики
    skipped_days = 1
    rep = 0

    
    import random
    import pygame

    # Класс Fish
    class Fish(object):
        def __init__(self):
            self.image = Transform("bg/lesson_larionov/fish.png", size=(150, 100))
            self.active = False
            self.dimensions = [150, 200]  # Обновлено под новый размер
            self.position = [0, 0]
            self.speed = [0, 10]
            self.maxY = 880  # Почти до нижнего края экрана (1080 - 200)
            
        def createNew(self):
            self.position[0] = random.randrange(0, 1770)  # 1920 - 150 (ширина рыбы)
            self.position[1] = 0 - self.dimensions[1]
            self.speed[1] = random.randrange(5, 15) 
            self.active = True
            
        def update(self, deltaTime):
            if self.active:
                self.position[1] += self.speed[1]
            
            if self.position[1] > self.maxY:
                self.active = False
                
        def isCaught(self, dogPosition, dogDimensions):
            if (dogPosition[0] < self.position[0] + self.dimensions[0] and
                dogPosition[0] + dogDimensions[0] > self.position[0] and
                dogPosition[1] < self.position[1] + self.dimensions[1] and
                dogPosition[1] + dogDimensions[1] > self.position[1]):
                self.active = False
                return True
            return False
            
        def render(self, renderer, shownTimebase, animationTimebase):
            if self.active:
                r = renpy.render(self.image, 800, 600, shownTimebase, animationTimebase)
                renderer.blit(r, (self.position[0], self.position[1]))

    # Класс Player
    class Player(object):
        def __init__(self):
            self.image = Transform("bg/lesson_larionov/dog.png", size=(450, 500))
            self.dimensions = [300, 400]  # Обновлено под новый размер
            self.position = [810, 680]  
            self.speed = [300, 20]  # Увеличена скорость
            self.grabCounter = 0
            self.grabCounterMax = 20
            self.action = "NONE"
            self.score = 0
            
        def handleInput(self, action):
            if self.grabCounter <= 0:
                self.action = action
                
        def update(self, deltaTime):
            if self.grabCounter > 0:
                if self.grabCounter > self.grabCounterMax/2:
                    self.position[1] -= self.speed[1] * deltaTime
                else:
                    self.position[1] += self.speed[1] * deltaTime
                    
                self.grabCounter -= 1
                if self.grabCounter == 0:
                    self.position[1] = 680  # Возвращаем в исходную позицию по Y
            else:
                if self.action == "LEFT" and self.grabCounter <= 0:
                    self.position[0] -= self.speed[0] * deltaTime
                elif self.action == "RIGHT" and self.grabCounter <= 0:
                    self.position[0] += self.speed[0] * deltaTime
                elif self.action == "GRAB" and self.grabCounter <= 0:
                    self.grabCounter = self.grabCounterMax
                
                if self.position[0] < 0:
                    self.position[0] = 0
                elif self.position[0] > 1920 - self.dimensions[0]:  # 1920 - ширина собаки
                    self.position[0] = 1920 - self.dimensions[0] 
            
            self.action = "NONE"
            
        def render(self, renderer, shownTimebase, animationTimebase):
            r = renpy.render(self.image, 800, 600, shownTimebase, animationTimebase)
            renderer.blit(r, (self.position[0], self.position[1]))

    # Класс FishCatcherGame
    class FishCatcherGame(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.player = Player()
            self.debug = []
            self.fish = []
            self.fishCaught = 0
            self.lastStart = None   
            self.frameRate = 60
            self.clock = pygame.time.Clock()
            self.countdown = 30
            self.milliseconds = 0
            self.gameover = False
            
        def event(self, event, x, y, shownTimebase):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.handleInput("GRAB")
                elif event.key == pygame.K_LEFT:
                    self.player.handleInput("LEFT")
                elif event.key == pygame.K_RIGHT:
                    self.player.handleInput("RIGHT")
                    
        def update(self, shownTimebase, animationTimebase):
            delta = self.getDelta(shownTimebase)
            rate = 1000 / self.frameRate
            speedAdjust = delta * rate
            
            if not self.gameover:
                chance = random.randrange(0, 20)
                if chance == 0 and len(self.fish) < 5:
                    fish = Fish()
                    fish.createNew()
                    self.fish.append(fish)
                
                removalList = []
                for fish in self.fish:
                    fish.update(1)
                    if fish.isCaught(self.player.position, self.player.dimensions):
                        self.player.score += 1
                    if not fish.active:
                        removalList.append(fish)
                
                for fish in removalList:
                    self.fish.remove(fish)
                    
                self.player.update(1)
                
                if self.milliseconds > 1000:
                    self.countdown -= 1
                    self.milliseconds = 0

                    
    self.milliseconds += self.clock.tick_busy_loop(60)
                if self.countdown <= 0:303
                    self.gameover = True
                    # Проверяем количество очков
                    if self.player.score < 50:
                        renpy.store.rep -= 1
                
                del self.debug[:]
                self.debug.append("Отладка")
                self.debug.append("Случайный: " + str(chance))
                self.debug.append("Положение Нурика: " + str(self.player.position[0]) + ", " + str(self.player.position[1]))
                for fish in self.fish:
                    self.debug.append("Положение мцд: " + str(fish.position[0]) + ", " + str(fish.position[1]) + ", Active: " + str(fish.active))
                self.debug.append("Дэльта: " + str(delta))
                
        def render(self, width, height, shownTimebase, animationTimebase):
            self.update(shownTimebase, animationTimebase)
            renderer = renpy.Render(width, height)
            
            if not self.gameover:
                for fish in self.fish:
                    fish.render(renderer, shownTimebase, animationTimebase)
                
                self.player.render(renderer, shownTimebase, animationTimebase)
                
                counter = 0
                for debug in self.debug:
                    txt = Text(_(debug), size=10)
                    textRender = renpy.render(txt, 800, 600, shownTimebase, animationTimebase)
                    renderer.blit(textRender, (0, 10 * counter))
                    counter += 1
            else:
                txt = Text(_("Конец игры"), size=40)
                renderer.blit(renpy.render(txt, 800, 600, shownTimebase, animationTimebase), (300, 250))
                   
            txtScore = Text(_("Время: " + str(self.countdown)), size=20)
            renderer.blit(renpy.render(txtScore, 800, 600, shownTimebase, animationTimebase), (700, 0))
            
            txtScore = Text(_("Счет: " + str(self.player.score)), size=20)
            renderer.blit(renpy.render(txtScore, 800, 600, shownTimebase, animationTimebase), (700, 20))
            
            renpy.redraw(self, 0)
            return renderer
            
        def per_interact(self):
            renpy.timeout(0)
            renpy.redraw(self, 0)
            
        def getDelta(self, shownTimebase):
            if self.lastStart is None:
                self.lastStart = shownTimebase
                    
            delta = shownTimebase - self.lastStart
            self.lastStart = shownTimebase
            return delta


style narr_style:
    xalign 0.5
    text_align 0.5

style window:
    yalign 1.0
    xsize 1920
    ysize 300
    background Frame("gui/textbox.png", 25, 25)


define narrator = Character(
    None,
    kind=adv,
    what_slow_cps=20,
    window_style="window",   
    what_style="narr_style"
)
define N = Character('Нурик', image="nurik", what_slow_cps=20, window_style="window")
define L = Character('Дмитрий Ильич', image="larionov", what_slow_cps=20, window_style="window")

# Изображения
image bg classroom = im.Scale("bg/lesson_larionov/new.jpg", 1920, 1080)
image bg poblighe = im.Scale("bg/lesson_larionov/poblighe.jpg", 1920, 1080)
image destroy = im.Scale("bg/lesson_larionov/destroy.png", 1000, 700)
image nurik = im.Scale("characters/Nur_udivil.png", 500, 800)
image larionov = im.Scale("characters/lar3.png", 850, 900)
image bg background = im.Scale("bg/lesson_larionov/bacground.jpg", 1920, 1080)

transform center_right:
    xalign 0.75 
    yalign 1.0
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

transform scary_effect:
    zoom 1.1
    alpha 0.0
    linear 0.1 alpha 1.0
    pause 0.5
    linear 0.1 alpha 0.0

image black_back = "#000"

define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define shake = Move((0, 10), (0, -10), 0.1, bounce=True, repeat=True, delay=0.5)
label chapter4_start:
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
    
    scene bg poblighe with dissolve
    show larionov at far_left
    
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
    
    menu:
        "Настоять на своем мнении о D2":
            $ rep -= 1
            show larionov at far_left with dissolve
            L "Я же говорил!"
            play sound "audio/destroy.ogg"
            
            show destroy at scary_effect, truecenter
            "*звук этеншн и знак тревоги, прилетает дестрой пак*"
            hide destroy
            
            "Нурик переоценил свои способности. Теперь, помимо основной работы, он получит наказание."
            
            # Запуск мини-игры
            call fish_catcher
            
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
    
    jump chapter4_peremena

label fish_catcher:    
    window hide None
    scene bg background
    with fade
    
    python:
        ui.add( FishCatcherGame() )
        ui.interact( suppress_overlay=True, suppress_underlay=True )
    
    return