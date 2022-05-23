with open('csv_data.csv', 'w') as writefile:
    lines_str = '''
    id,name,email
    1,kk,kk@gmail.com
    2,pushpa,pushpa@outlook.com
    3,purvi,purvi@kk.com
    4,ruth,ruth@pushpa.com
    '''
    for line in lines_str.split():
        writefile.write(line+'\n')

with open('csv_data.csv','r') as rd:
    # all lines read as str
    # content = rd.read()
    # print(content, type(content))

    # read : number of characters
    # content = rd.read(10)
    # while len(content) > 0:
    #     print(content, end='**')
    #     content = rd.read(10)

    # all lines read as list 
    # lines = rd.readlines()
    # print(lines)

    # reading single line at a time
    # line = rd.readline()
    # print(line)
    # line = rd.readline()
    # print(line)

    for line in rd:
        print(line)