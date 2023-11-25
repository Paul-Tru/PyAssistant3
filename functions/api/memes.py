import requests
import functions.tools.tools as t


def memes():
    response = requests.get("https://meme-api.com/gimme")
    data = response.json()
    pic = data.get("url")
    spoiler = data.get("spoiler")
    if spoiler is not True:
        t.save_pics(pic, "memes", pic)