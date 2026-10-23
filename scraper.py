import feedparser
from datetime import datetime, timezone

def get_news():

    feed = feedparser.parse(
        "https://www.space.com/feeds/all"
    )

    articles = []

    now = datetime.now(timezone.utc)

    for entry in feed.entries:

        try:

            published = datetime(
                *entry.published_parsed[:6],
                tzinfo=timezone.utc
            )

            age = now - published

            if age.total_seconds() <= 86400:

                articles.append({
                    "title": entry.title,
                    "hours": int(
                        age.total_seconds() / 3600
                    )
                })

        except Exception:
            continue

    return articles