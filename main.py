from scraper import get_news
from analyzer import *

print("\n🚀 SON 24 SAATTEKİ UZAY GELİŞMELERİ\n")

articles = get_news()

print(
    f"Bulunan güncel haber sayısı: {len(articles)}\n"
)

for article in articles:

    title = article["title"]
    hours = article["hours"]

    category = get_category(title)
    score = get_score(title)
    usages = get_usage(title)

    print("=" * 60)

    print("Başlık:")
    print(title)

    print(f"\n⏰ {hours} saat önce")

    print(f"\nKategori: {category}")
    print(f"Önem: {score}/10")

    print("\nKullanım Alanları:")

    for usage in usages:
        print("-", usage)

    print()