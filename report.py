from datetime import datetime

def create_report(articles):

    date = datetime.now().strftime(
        "%Y-%m-%d"
    )

    with open(
        "daily_report.md",
        "w",
        encoding="utf-8"
    ) as f:

        f.write("# 🚀 SpaceScout Günlük Raporu\n\n")

        f.write(f"**Tarih:** {date}\n\n")

        f.write(
            f"**Son 24 saatte bulunan haber sayısı:** {len(articles)}\n\n"
        )

        for article in articles:

            f.write(
                f"## {article['title']}\n\n"
            )

            f.write(
                f"⏰ {article['hours']} saat önce\n\n"
            )

            f.write(
                f"**Kategori:** {article['category']}\n\n"
            )

            f.write(
                f"**Önem:** {article['score']}/10\n\n"
            )

            f.write("### Kullanım Alanları\n\n")

            for usage in article["usages"]:
                f.write(f"- {usage}\n")

            f.write("\n---\n\n")

    print("📄 daily_report.md oluşturuldu")