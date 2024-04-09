import urllib.request, os, requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

name = "bayonet"        ## change based on desired weapon
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

req = urllib.request.Request(url=f'https://csgoskins.gg/weapons/{name}')
webpage = urllib.request.urlopen(req).read()
soup = BeautifulSoup(webpage, features="html5lib")

size = (150, 115)        ## image ouput resolution
dir = os.path.dirname(os.path.realpath(__file__))
for each_div in soup.findAll('img',{'class':'mx-auto'}):
    data = requests.get(each_div['src'], headers={'User-Agent': 'Mozilla/5.0'}).content
    pilImage = Image.open(BytesIO(data)).convert('RGBA')
    img = pilImage.resize(size, resample=Image.BICUBIC)
    img.save(f"{dir}\{name}_{each_div['alt'].split(' ')[-1]}.png", optimize=True, quality=30)
