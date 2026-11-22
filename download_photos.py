import os, urllib.request
URLS = ['https://avatars.mds.yandex.net/get-altay/11300692/2a0000019159b4f9216632f167c550519e34/L_height']
os.makedirs('photos', exist_ok=True)
for i, u in enumerate(URLS, 1):
    r = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
    open(f'photos/{i}.jpg', 'wb').write(urllib.request.urlopen(r).read())
    print('saved', f'photos/{i}.jpg')
