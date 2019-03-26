import argparse
from captcha.image import ImageCaptcha
import os
from tqdm import tqdm


def generate_single_numbers(number, quantity, path):
    '''
    generuje n obrazków z określoną cyfrą w określonym folderze

    number - cyfra
    quantity - ilość
    path - folder
    '''

    image_captcha = ImageCaptcha(width = 60, height = 60)

    for i in tqdm(range(quantity)):
        image = image_captcha.generate_image(str(number))
        image.save(os.path.join(path, str(i)+'.jpg'))


if(__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder',type = str, required = True, help = 'path to training data folder')
    args = parser.parse_args()

    folder_path = args.folder

    if(input('Czy nadpisać folder "{}"? [y/n]'.format(folder_path)) != 'y'):
        exit()

    for i in range(10):
        curr_path = os.path.join(folder_path, str(i))
        os.mkdir(curr_path)

        print('Generating {}...'.format(i))

        generate_single_numbers(i, 2000, curr_path)

