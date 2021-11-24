from PIL import Image
import numpy as np


def convert_image_to_mosaic(image, size, gradation_step):
    for x in range(0, len(image), size):
        for y in range(0, len(image[0]), size):
            image[x:x + size, y:y + size] = get_average_brightness(
                image[x:x + size, y:y + size], size, gradation_step)
    return image


def get_average_brightness(block, size, gradation_step):
    average_color = (block[:size, :size].sum() / 3) // size ** 2
    return int(average_color // gradation_step) * gradation_step


def main():
    #image_file = Image.open(input("Введите имя файла, которое хотите конвертировать: "))
    #block_size = int(input("Введите размер блока: "))
    #gradations_count = int(input("Введите количество градаций серого: "))
    #image = np.array(image_file)
    image = np.array(Image.open('scale1200.jpg'))
    #gradation_step = 255 // gradations_count
    gradation_step = 255 // 50

    #res = Image.fromarray(convert_image_to_mosaic(image, block_size, gradation_step))
    res = Image.fromarray(convert_image_to_mosaic(image, 10, gradation_step))
    #res.save(input("Введите имя файла, в которой хотите сохранить результат: "))
    res.save('res.jpg')


if __name__ == '__main__':
    main()
