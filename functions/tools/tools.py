import configparser
import os
import requests


def config_var(sec, var):
    config = configparser.ConfigParser()
    config.read("../../data/config.ini")
    return config.get(sec, var)


# to save photos from APIs
def save_pics(pic_url, dic, title):
    img_data = requests.get(pic_url).content
    path = f'../../data/PICTURES/{dic}'
    if not os.path.exists(path):
        os.makedirs(path)
    with open(os.path.join(path, f'{title}'), 'wb') as handler:
        handler.write(img_data)
