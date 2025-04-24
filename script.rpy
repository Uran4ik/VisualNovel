# Общие настройки
define narrator = Character(None)
define l = Character('Леша', color="#c8ffc8")
define bus = Character('Автоинформатор', color="#c8ffc8")
define N = Character('Нурик', image="nurik")

# Общие изображения и трансформы
image black_back = "#000000"


label start:
    # Запуск первой главы
    jump chapter1_start

    jump chapter1_start


label game_over:
    # Общий экран завершения
    return