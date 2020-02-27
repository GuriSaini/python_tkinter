with open('file.txt','r') as rf:
    with open('file1.txt','w') as wf:
        for line in rf.readlines():
            name,salary = line.split(',')
            wf.write(f'{name}\'s salray is {salary}')
