import csv

with open('csv_data.csv', 'w', newline='\n') as writefile:
    lines_str = '''
    id,name,email
    1,kk,kk@gmail.com
    2,pushpa,pushpa@outlook.com
    3,purvi,purvi@kk.com
    4,ruth,ruth@pushpa.com
    '''
    for line in lines_str.split():
        writefile.write(line+'\n')

with open('csv_data.csv') as csvread:
    csv_reader = csv.reader(csvread)
    # for line in csv_reader:
    #     print(line)

    with open('csv_data_1.csv','w', newline='') as csvwrite:
        csv_writer = csv.writer(csvwrite, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)

with open('csv_data_1.csv','r') as csvread:
    csv_reader = csv.DictReader(csvread, delimiter="\t")
    # for line in csv_reader:
    #     print(line)

    with open('csv_data_2.csv','w', newline='') as csvwrite:
        # fieldnames = ['id', 'name', 'email']
        fieldnames = ['id', 'name']
        csv_writer = csv.DictWriter(csvwrite, fieldnames=fieldnames, delimiter='*')
        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
