import requests
from datetime import datetime
from functions.tools import tools


def tagesschau():
    url = "https://www.tagesschau.de/api2/news"
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError if the status is 4xx, 5xx

    if response.status_code != 200:
        print(tools.read_json("status_code", response.status_code))
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

        results.append((title, fSen, news_url, news_date, breaking_news))

    return results
