import requests
from bs4 import BeautifulSoup

def get_news():

    url = "https://www.nasa.gov/news/"

    response = requests.get(
        url,
        timeout=20
    )

    print("Durum kodu:", response.status_code)

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    titles = soup.find_all("h2")

    print("Bulunan başlıklar:")

    for title in titles[:10]:
        print(title.get_text(strip=True))