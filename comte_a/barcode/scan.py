#!/usr/bin/python3

i = 0
f = open('dump_file', 'a')
while i < 2:
    f.write(input('Enter a barecode: '))
    f.write('\n')
    i += 1
f.close()
