from parsing import Parser

for inp in input(':>').split():
    Parser(inp, 'cp1251').get_url_image()
