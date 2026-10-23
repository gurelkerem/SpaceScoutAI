def create_report(articles):

    html = """
    <html>
    <head>
        <meta charset="utf-8">

        <title>SpaceScout AI</title>

        <style>

        body{
            font-family: Arial;
            background:#0b1020;
            color:white;
            max-width:1000px;
            margin:auto;
            padding:20px;
        }

        h1{
            color:#4fc3f7;
        }

        .card{
            background:#182038;
            padding:20px;
            border-radius:10px;
            margin-bottom:20px;
        }

        </style>

    </head>

    <body>

    <h1>🚀 SpaceScout AI</h1>

    <p>Son 24 saatteki uzay gelişmeleri</p>
    """

    for article in articles:

        html += f"""
        <div class="card">

        <h2>{article['title']}</h2>

        <p>
        ⏰ {article['hours']} saat önce
        </p>

        <p>
        {article['category']}
        </p>

        <p>
        ⭐ {article['score']}/10
        </p>

        <ul>
        """

        for usage in article["usages"]:
            html += f"<li>{usage}</li>"

        html += """
        </ul>

        </div>
        """

    html += """
    </body>
    </html>
    """

    with open(
        "index.html",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(html)

    print("✅ index.html oluşturuldu")