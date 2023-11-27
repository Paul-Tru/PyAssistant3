import requests
import functions.tools.tools as t


def memes():
    for x in range(5):
        response = requests.get("https://meme-api.com/gimme")
        data = response.json()
        pic = data.get("url")
        title = pic.replace("https://i.redd.it/", "")
        spoiler = data.get("spoiler")
        if spoiler is not True:
            t.save_pics(pic, "memes", title)