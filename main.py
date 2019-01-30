from parsing import Parser


#for name in input(':>').split():
#	Parser(name, 'cp1251').get_url_image()

# for _ in range(50):
# 	Parser('природа', 'cp1251').get_url_image()

name = input(':>').split()
n = 1
for obj in name:
    tmp = len(obj) - len([n for n in obj if n.isalpha()])
    print(tmp)
    for _ in range(int(obj[-tmp:])):
        Parser(obj[:-tmp], 'cp1251').get_url_image()
