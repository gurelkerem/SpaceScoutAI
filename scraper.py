import feedparser

NASA_FEED = "https://www.nasa.gov/rss/dyn/breaking_news.rss"

def get_news():
    feed = feedparser.parse(NASA_FEED)

    for item in feed.entries[:5]:
        print(item.title)