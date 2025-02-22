# %%
import re
import requests
import os
from fig2q.helpers import get_yaml


FIGMA_TOKEN = 'figd_JdfppOWxHXSkCXj5CiiXKCygm0QmHy8lMWQ3av-3'
example = 'https://www.figma.com/design/qiY7mWWSxQjrSG2d50wxFv/WI-Schweiz-Deutschland-Import%2FExport-(joe)?node-id=45-11&t=zd5V2pw1gLGsrwCv-11'

# %%
yml = get_yaml()

# %%
def get_file_id(link):
    return re.search(r'/design/(.+?)/', link).group(1)

get_file_id(example)

# %%
def get_artboard_url_id(link):
    return re.search(r'node-id=(.+?)&', link).group(1)

get_artboard_url_id(example)
# %%
def get_artboard_id(link):
    return str.replace(re.search(r'node-id=(.+?)&', link).group(1), '-', ':')

get_artboard_id(example)

# %%
def image_url(file_id, artboard_id, scale=4):
    scale = str(scale)
    api = 'https://api.figma.com/v1/images/'
    return api + file_id + '?ids=' + artboard_id + '&scale=' + scale

# %% Create folder if it doesn't exist
def ensure_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
# %%
def download_image(link, name='mw', folder='pngs'):
    if(not('https://www.figma.com' in link)):
        return None

    _headers = {
        'X-FIGMA-TOKEN': FIGMA_TOKEN
    }
    img_url = image_url(get_file_id(link), get_artboard_url_id(link), 4)
    print(img_url)
    try:
        where_img = requests.get(img_url, headers=_headers)
    except:
        raise Exception('Link zum Artboard funktioniert nicht. Vermutlich wurde das Artboard gelöscht.')
    img = where_img.json()['images'][get_artboard_id(link)]


    ensure_folder(folder)
    _img = requests.get(img, stream=True)
    with open(name, 'wb') as file:
            # Write the response content to the file
            file.write(_img.content)

#download_image(example, 'cw')
