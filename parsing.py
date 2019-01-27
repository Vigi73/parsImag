import requests
from bs4 import BeautifulSoup as BS
from urllib.parse import quote

from tkinter import Tk


class Parser:
    def __init__(self, name, encode):
        self.obj_name = name
        self.url = f'http://www.nastol.com.ua/tags/{quote(self.obj_name, encoding=encode)}/page/1/'
        self.encoding = encode

    def get_html(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/71.0.3578.99 YaBrowser/19.1.0.2494 (beta) Yowser/2.5 Safari/537.36',
            'login_username': 'doom',
            'login_password': '123456'
        }

        session = requests.session()
        r = session.post(self.url, headers=headers)
        r.encoding = self.encoding
        return r.text

    def get_pages(self):
        soup = BS(self.get_html(), 'lxml')
        img_count = soup.find('span', {'class': 'nav-center'})

        return img_count.text.split('.')[-1].strip()

    def get_resolution(self):
        t = Tk()
        SIZE = WIDTH, HEIGHT = t.winfo_screenwidth(), t.winfo_screenheight()
        return SIZE, WIDTH, HEIGHT
