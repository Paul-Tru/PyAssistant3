import requests
from datetime import datetime
from functions.tools import tools


def tagesschau():
    url = "https://www.tagesschau.de/api2/news"
    response = requests.get(url)

    if response.status_code != 200:
        print(tools.read_json("status_code", response.status_code))
        response.raise_for_status()
        return

    data = response.json()
    news_items = data["news"][:75]  # Limit to the first 75 news items

    results = []
    for news_item in news_items:
        title = news_item["title"]

        try:
            news_date = datetime.strptime(news_item["date"], "%Y-%m-%dT%H:%M:%S.%f%z").strftime("%d-%m-%Y %H:%M")
        except ValueError as e:
            print(f"Error parsing date: {e}")
            continue  # Skip this news item and continue with the next one.

        fSen = news_item.get("firstSentence")
        breaking_news = news_item.get("breakingNews")
        news_url = news_item.get("detailsweb")
        ex_id = news_item.get("externalId")
        ex_id = ex_id[:20]

        teaser_image = news_item.get("teaserImage")
        if teaser_image:
            image_variants = teaser_image.get("imageVariants")
            if image_variants and "1x1-144" in image_variants:
                pic_url = image_variants["1x1-144"]
                tools.save_pics(pic_url, "Tagesschau", ex_id + ".jpg")

        rj = tools.read_json("news", title)
        if rj is not None and title not in rj:
            tools.write_json("news", title, fSen, news_date)
            results.append((title, fSen, news_url, ex_id, news_date, breaking_news))

    return results
