import os
import sys
import time
import random
import requests


ACCESS_KEY = 'dV0tx-EbdJDZPxSbTob2cyIlzYj5aVEbs4fA4yFVHgs'
QUERY = 'nature'  

IMAGE_DIR = 'wallpapers'

def download_random_image():
    url = f'https://api.unsplash.com/photos/random?client_id={ACCESS_KEY}&query={QUERY}'
    response = requests.get(url)
    if response.status_code == 200:
        image_data = response.json()
        image_url = image_data['urls']['full']
        image_filename = os.path.join(IMAGE_DIR, f'wallpaper_{time.time()}.jpg')
        with open(image_filename, 'wb') as image_file:
            image_file.write(requests.get(image_url).content)
        return image_filename

def set_wallpaper(image_path):
    import ctypes
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

os.makedirs(IMAGE_DIR, exist_ok=True)


interval_minutes = 10
interval_seconds = interval_minutes * 60

while True:
    try:
        image_path = download_random_image()
        set_wallpaper(image_path)
        print(f'Wallpaper changed to {image_path}')
        time.sleep(interval_seconds)
    except Exception as e:
        print(f'An error occurred: {str(e)}')
        continue
#  run the script by pip install requests pywin32