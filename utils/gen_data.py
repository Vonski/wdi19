from gen_captcha import generate_random_labeled_sample
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import pandas as pd
import os

train_path = "../data/yolo_train/"
train_path_boxes = "../data/yolo_train_with_boxes/"
test_path = "../data/yolo_test/"
test_path_boxes = "../data/yolo_test_with_boxes/"

os.makedirs(train_path, exist_ok=True)
os.makedirs(train_path_boxes, exist_ok=True)
os.makedirs(test_path, exist_ok=True)
os.makedirs(test_path_boxes, exist_ok=True)


def generate_dataset(num, path, path_boxes):
    labels = pd.DataFrame(columns=["file", "x", "y", "width", "height", "class"])

    for i in range(num):
        im, coord, chars = generate_random_labeled_sample()

        image = im.copy()
        draw = ImageDraw.Draw(image)
        for j in range(len(chars)):
            if chars[j] is not " ":
                labels = labels.append(
                    {"file": str(i) + ".png", "x": coord[j][0], "y": coord[j][1], "width": coord[j][2],
                     "height": coord[j][3], "class": chars[j]}, ignore_index=True)
                draw.rectangle([coord[j][0], coord[j][1], coord[j][0] + coord[j][2], coord[j][1] + coord[j][3]], fill=None,
                               outline="red")

        im.save(path + str(i) + ".png", 'png')
        image.save(path_boxes + str(i) + ".png", 'png')

    # print(train_labels)
    labels.to_csv(path + "labels.csv")


generate_dataset(60000, train_path, train_path_boxes)
generate_dataset(12000, test_path, test_path_boxes)
