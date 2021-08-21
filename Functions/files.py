text_modes = ['r', 'w', 'a', 'r+'] # r-read, w-write, a-"after write", r+ - read&write
binary_modes = ['br', 'bw', 'ba', 'br+'] # binary file

f = open('filename', 'w')
f.write('the world is changed')
f.close()

f = open('filename', 'r+')
f.read()
f.tell() # pointer. After read method pointer is in the end
f.read() # ''

f.seek(0)
f.tell() # 0
f.close()

f = open('filename', 'r+')
f.readline() # read only one row
f.close()

f = open('filename', 'r+')
f.readlines() # read row by row
f.close()

# the most recommended
with open('filename', 'w') as f:
    print(f.read())