import feedparser

def get_news():

    feed = feedparser.parse(
        "https://www.space.com/feeds/all"
    )

    return feed.entries[:10]