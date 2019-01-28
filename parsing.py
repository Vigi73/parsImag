import requests
from bs4 import BeautifulSoup as BS
from urllib.parse import quote
from tkinter import Tk

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
        size = t.winfo_screenwidth(), t.winfo_screenheight()
        return size

    def get_url_image(self):
        href = []

        soup = BS(self.get_html(), 'lxml')
        divs = soup.find_all('div', {'class': 'verh'})
        #Цикл получения ссылок на странице
        for div in divs:
            href.append(div.find('a', {'class': 'screen-link'})['href'])
        # Цикл получения ссылки на скачивание
        #https: // www.nastol.com.ua/download/316645/1920x1080/
        for url in href:
            number_img = url.split('/')[-1].split('-')[0]
            href_d = base_url + f'/{number_img}/{self.get_resolution()[0]}x{self.get_resolution()[1]}/'
            soup3 = BS(get_h(href_d, self.encoding), 'lxml')
            print(soup3.find('div', {'id': 'wrapper'}).find_all('a')[-2]['href'])




