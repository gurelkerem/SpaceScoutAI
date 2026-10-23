from scraper import get_news
from analyzer import *
from report import create_report

print("\n🚀 SPACESCOUT RAPORU\n")

articles = get_news()

print(
    f"Son 24 saatte bulunan haber sayısı: {len(articles)}\n"
)

report_data = []

for article in articles:

    title = article["title"]
    hours = article["hours"]

    category = get_category(title)
    score = get_score(title)
    usages = get_usage(title)

    print("=" * 60)

    print(title)
    print(f"⏰ {hours} saat önce")
    print(f"Kategori: {category}")
    print(f"Önem: {score}/10")

    report_data.append({
        "title": title,
        "hours": hours,
        "category": category,
        "score": score,
        "usages": usages
    })

create_report(report_data)