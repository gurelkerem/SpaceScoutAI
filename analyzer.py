def get_category(title):

    title = title.lower()

    if "satellite" in title:
        return "🛰️ Uydu"

    elif "rocket" in title:
        return "🚀 Roket"

    elif "moon" in title:
        return "🌕 Ay"

    elif "mars" in title:
        return "🔴 Mars"

    elif "black hole" in title:
        return "🕳️ Kara Delik"

    elif "telescope" in title:
        return "🔭 Teleskop"

    return "🌌 Genel Uzay"


def get_score(title):

    score = 5

    keywords = [
        "launch",
        "moon",
        "mars",
        "black hole",
        "discovery",
        "satellite",
        "rocket",
        "telescope"
    ]

    for word in keywords:
        if word in title.lower():
            score += 1

    return min(score, 10)


def get_usage(title):

    title = title.lower()

    if "satellite" in title:
        return [
            "İletişim",
            "Savunma",
            "Dünya gözlemi"
        ]

    if "rocket" in title:
        return [
            "Uzay görevleri",
            "Uydu taşımacılığı"
        ]

    if "moon" in title:
        return [
            "Ay üsleri",
            "Madencilik",
            "Bilimsel araştırma"
        ]

    if "mars" in title:
        return [
            "İnsanlı görevler",
            "Koloni araştırmaları"
        ]

    if "black hole" in title:
        return [
            "Temel fizik araştırmaları"
        ]

    return [
        "Bilimsel araştırma"
    ]