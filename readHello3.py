file = open('jeongyeran.txt', 'rt')

while True:
    str = file.readline()
    if str == '':
        break
    print(str, end='')

file.close()
