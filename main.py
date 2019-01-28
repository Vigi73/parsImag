from parsing import Parser


code = 'cp1251'
name_obj = input()

p = Parser(name_obj, code)
print(p.get_pages())
#print(p.get_resolution()[0])

for url in p.get_url_image():
    print(url)


