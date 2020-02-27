#seek method
#read method
#close method
#readline method read line one at time (list)
#tell method
#with block
#context manager
#name , closed

f = open('file.txt')
print(f'cursor position - {f.tell()}')
print(f.read())
print(f'cursor position - {f.tell()}')
print(f.seek(0))
print(f.read())

f.close()

with open('file.txt') as f:
    data = f.read()
    print(data)
