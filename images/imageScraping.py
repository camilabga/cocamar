from bs4 import BeautifulSoup

import requests
import urllib.request
import shutil

url = "https://www.insectimages.org/browse/taxthumb.cfm?order=120"
cookies = {
    'CFGLOBALS': 'urltoken%3DCFID%23%3D113056790%26CFTOKEN%23%3D583579c1fa3ea412%2DAE0A0A29%2DCF5E%2DD5D4%2D9CBADCAA360500E5%26jsessionid%23%3DFED4A2CF74EA0551772FD90D18F6EF76%2EInstance1%23lastvisit%3D%7Bts%20%272020%2D08%2D16%2011%3A05%3A59%27%7D%23timecreated%3D%7Bts%20%272020%2D08%2D15%2010%3A45%3A01%27%7D%23hitcount%3D24%23cftoken%3D37e3ca80e13d137e%2D79C9ABF2%2D98DD%2D1FF7%2DECDA97B2BDEC9192%23cfid%3D112950884%23',
    '_ga': 'GA1.2.994486128.1597502754',
    '_gid': 'GA1.2.640712119.1597502754',
    'CFCLIENT_INSECTIMAGES': 'sterm%3DNezara%20viridula%23sbegin%3D1%23',
    'CFID': '113056790',
    'CFTOKEN': '583579c1fa3ea412-AE0A0A29-CF5E-D5D4-9CBADCAA360500E5',
    'JSESSIONID': 'FED4A2CF74EA0551772FD90D18F6EF76.Instance1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en,en-US;q=0.8,pt-BR;q=0.5,pt;q=0.3',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
}

params = (
    ('order', '120'),
)

response = requests.get('https://www.insectimages.org/browse/taxthumb.cfm', headers=headers, params=params, cookies=cookies)
print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

aas = soup.find_all("img", class_='img-responsive')


image_info = []

for a in aas:
    image_tag = a.findChildren("img")
    image_info.append((image_tag[0]["src"], image_tag[0]["alt"]))


def download_image(image):
    response = requests.get(image[0], stream=True)
    realname = ''.join(e for e in image[1] if e.isalnum())

    with open("C:/Users/Marcolino/PycharmProjects/desafio-1/data/algo/{}.jpg".format(realname), 'wb') as file:
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, file)
        del response
for i in range(0, len(image_info)):
    download_image(image_info[i])
