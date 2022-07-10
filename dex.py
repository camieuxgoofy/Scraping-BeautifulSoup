from bs4 import BeautifulSoup
import requests

page = requests.get("https://nekopoi.care")
soup = BeautifulSoup(page.content, "html5lib")
print(soup.prettify())
if page.status_code == 200:
    div = soup.find(id="eropost")

htmltxt = """
<html>
<head>
    <title>Scrapping</title>
</head>

<body>
<p class="cover-images">Cover Images</p>
<p class="title">Title</p>
<p class="date">Date</p>
<p class="synopsis">Synopsis</p>
<p class="tags">Genre</p>
<p class="url-downloads">Download</p>
</body>

</html>
"""

eropost = div.findAll("div", attrs={"class": "eropost"})
erofpost = []
for row in eropost:
    erofpost = {}
    erofpost["cover"] = row.img("src")
    erofpost["title"] = row.eroinfo.h2.text.replace["\n", ""]
    erofpost["time"] = row.eroinfo.span.text.replace("\n", "")
    eropost.append(erofpost)

import json
import pprint

pprint.pprint(eropost)
