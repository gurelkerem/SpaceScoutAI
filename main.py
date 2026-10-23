from scraper import get_news
from analyzer import *

print("\n🚀 SPACESCOUT RAPORU\n")

articles = get_news()

for article in articles:

    title = article.title

    category = get_category(title)

    score = get_score(title)

    usages = get_usage(title)

    print("=" * 50)

    print("Başlık:")
    print(title)

    print("\nKategori:")
    print(category)

    print("\nÖnem:")
    print(f"{score}/10")

    print("\nKullanım Alanları:")

    for usage in usages:
        print("-", usage)

    print()