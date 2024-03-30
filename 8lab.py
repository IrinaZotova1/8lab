def nom1():
    from PIL import Image
    otk = Image.open("otk.jpg")
    width, height = otk.size
    left = 0
    top = 255
    right = 1080
    bottom = 1080
    bez_bykv = otk.crop((left, top, right, bottom))
    otk.show()
    bez_bykv.show()
    bez_bykv.save("otk_bez_bykv.jpg")


def nom2():
    from PIL import Image
    otkr = {
        "новый год": "ng.jpg",
        "масленница": "mas.jpg",
        "день рождения": "otk.jpg"
    }
    x = input("Введите праздник: ")
    if x.lower() in otkr:
        photo = otkr[x.lower()]
        photo_otkr = Image.open(photo)
        photo_otkr.show()
    else:
        print("Такой картинки нет")


def nom3():
    from PIL import Image, ImageFont, ImageDraw
    import random
    otkr = {
        "новый год": "ng01.jpg",
        "масленница": "mas01.jpg",
        "день рождения": "dr01.jpg"
    }
    x = input("Введите праздник: ")
    if x.lower() in otkr:
        photo = otkr[x.lower()]
        photo_otkr = Image.open(photo)
    else:
        print("Такой картинки нет")
    # w, h = photo_otkr.size - В этой строке происходит извлечение ширины и высоты изображения
    # photo_otkr с использованием метода .size из библиотеки Pillow.
    # Размер изображения сохраняется в переменные w (ширина) и h (высота).
    # Это позволяет программе знать размеры изображения, что необходимо для корректного
    # позиционирования текста и других элементов на изображении
    W, H = photo_otkr.size
    im = input("Введите имя того, кого хотите поздравить: ")
    a = "Поздравляю, "
    text = a + im + "!"
    color1 = random.randint(0, 256)
    color2 = random.randint(0, 256)
    color3 = random.randint(0, 256)
    y = [5, 2000]
    y1 = random.choice(y)
    shrift = ["arial.ttf", "ariblk.ttf"]
    shrift1 = random.choice(shrift)
    draw = ImageDraw.Draw(photo_otkr)
    font = ImageFont.truetype(f"{shrift1}", 120)
    # _, _, w1, h1 = txt.textbbox((0, y1), text, font=font)
    # Вызывается метод textbbox, чтобы определить ограничивающий прямоугольник вокруг текста text.
    # Результатом являются четыре значения, но первые два значения, которые соответствуют
    # координатам верхнего левого угла прямоугольника, здесь не используются (обозначаются как _).
    # А два последних значения, которые соответствуют ширине w1 и высоте h1, сохраняются соответственно.
    # Таким образом, это позволяет определить размеры и положение текста для последующего отображения на изображении.
    _, _, w, h = draw.textbbox((0, y1), text, font=font)
    # txt.text(((W - w)/2, y1), text, (color1, color2, color3), font=font) - В этой строке вызывается метод.
    # .text для добавления текста name_text на изображение.
    # Координаты x для отображения текста рассчитываются как центр изображения минус половина ширины текста w1,
    # что дает горизонтально центрированную позицию текста.
    # Координата y остается такой же, как и в исходном y1.
    # Параметры (b, c, d) определяют цвет текста, и font=font указывает на шрифт для отображения текста.
    draw.text(((W - w) / 2, y1), text, font=font, fill=(color1, color2, color3))
    photo_otkr.show()
    photo_otkr.save('otkritka_s_imenem.png')