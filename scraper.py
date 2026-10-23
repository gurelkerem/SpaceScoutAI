import feedparser

def get_news():

    feed = feedparser.parse(
        "https://www.space.com/feeds/all"
    )

    print("\n🚀 Son Uzay Haberleri\n")

    print("Bulunan haber sayısı:",
          len(feed.entries))

    for article in feed.entries[:10]:
        print("- " + article.title)