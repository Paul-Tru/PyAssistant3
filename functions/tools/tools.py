import configparser
import json
import os
from datetime import datetime
import requests

now = datetime.now()
date = now.strftime("%Y-%m-%d")
current = now.strftime("%H:%M")


def read_json(sec, var):
    with open('../../data/data.json', 'r') as f:
        data = json.load(f)
    if var in data.get(sec, {}):
        return data[sec][var]
    else:
        return None


def write_json(sec, var, text, src_date):
    x = "../../data/data.json"
    if src_date == "0":
        src_date = date
    try:
        with open(x, "r") as file:
            try:
                info_data = json.load(file)
            except json.JSONDecodeError:
                info_data = {}

        new_entry = {"text": text, "date": src_date}
        info_data[sec][var] = new_entry

        with open(x, "w") as file:
            file.write(json.dumps(info_data, indent=4))
        return True

    except Exception as e:
        return e


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

