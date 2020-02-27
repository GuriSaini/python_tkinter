with open('test.html','r') as webpage:
    with open('linkfind.txt','a') as wf:
        # for line in webpage.readlines():
        #     if '<a href=' in line:
        #         position = line.find('<a href=')
        #         first_quote = line.find('\"',position)
        #         second_quote = line.find('\"',first_quote+1)
        #         url = line[first_quote+1:second_quote]
        #         wf.write(url + '\n')
        for lines in webpage.readlines():
            if '<h3>' in lines: 
                first = lines.find('>')
                second = lines.find('<',first+1)
                name = lines[first+1:second]
                wf.write(name + '\n')