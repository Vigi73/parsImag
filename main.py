from parsing import Parser


for name in input(':>').split():
	Parser(name, 'cp1251').get_url_image()