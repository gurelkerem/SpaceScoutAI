import feedparser

NASA_FEED = "https://www.nasa.gov/rss/dyn/breaking_news.rss"

def get_news():

    feed = feedparser.parse(NASA_FEED)

    print("\nNASA Haberleri\n")

    for article in feed.entries[:5]:
        print(article.title)