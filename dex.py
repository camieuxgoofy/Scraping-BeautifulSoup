from bs4 import BeautifulSoup

dokumen = '''
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
'''

html_soup = BeautifulSoup(dokumen, 'html.parser')

cover-images = html_soup.find('p', class_='cover-images')
title = html_soup.find('p', class_='title')
date = html_soup.find('p', class_='date')
synopsis = html_soup.find('p', class_='synopsis')
tags = html_soup.find('p', class_='tags')
url-downloads = html_soup.find('p', class_='url-dowbnloads')


print(cover-images)
print(title)
print(date)
print(synopsis)
print(tags)
print(url-downloads)

content = html_soup.find_all('p')
print(content)
