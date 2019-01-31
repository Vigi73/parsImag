import requests
from bs4 import BeautifulSoup as BS
from urllib.parse import quote
from tkinter import Tk
import os
from random import randrange as rnd

base_url = 'https://www.nastol.com.ua/download'


def get_h(url, enc):
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/71.0.3578.99 YaBrowser/19.1.0.2494 (beta) Yowser/2.5 Safari/537.36',
        'login_username': 'doom',
        'login_password': '123456'
    }
    session = requests.session()
    r = session.post(url, headers=headers)
    r.encoding = enc
    return r.text


def save_file(url, name):
    r = requests.get(url, stream=True)
    if os.path.exists('img'):
        with open(name, 'bw') as f:
            f.write(r.content)
    else:
        os.mkdir('img')
        with open(name, 'bw') as f:
            f.write(r.content)


def get_pages(url, enc):
    soup = BS(get_h(url, enc), 'lxml')
    img_count = soup.find('span', {'class': 'nav-center'})
    return img_count.text.split('.')[-1].strip()


class Parser:
    def __init__(self, name, encode):

        self.obj_name = name

        try:
            n_page = rnd(
                int(get_pages(f'https://www.nastol.com.ua/tags/{quote(self.obj_name, encoding=encode)}/', encode)))
        except:
            n_page = rnd(int(
                get_pages(f'https://www.nastol.com.ua/tags/{quote(self.obj_name, encoding=encode)}/', encode).split()[
                    -1]))

        self.url = f'http://www.nastol.com.ua/tags/{quote(self.obj_name, encoding=encode)}/page/{n_page}/'
        self.encoding = encode

    def get_resolution(self):
        t = Tk()
        size = t.winfo_screenwidth(), t.winfo_screenheight()
        return size

    def get_url_image(self):

        href = []
        soup = BS(get_h(self.url, self.encoding), 'lxml')
        divs = soup.find_all('div', {'class': 'verh'})
        # получение ссылок на странице
        for div in divs:
            href.append(div.find('a', {'class': 'screen-link'})['href'])
        # получение ссылки на скачивание
        # https: // www.nastol.com.ua/download/316645/1920x1080/
        for i, url in enumerate(href, start=1):
            number_img = url.split('/')[-1].split('-')[0]
            href_d = base_url + f'/{number_img}/{self.get_resolution()[0]}x{self.get_resolution()[1]}/'
            soup3 = BS(get_h(href_d, self.encoding), 'lxml')
            url_d = soup3.find('div', {'id': 'wrapper'}).find_all('a')[-2]['href']
            save_file(url_d, f'img/{self.obj_name}' + f'_{number_img}.jpg')
            print(f'{i} - файл: {self.obj_name}' + f'_{number_img} сохранен...')
