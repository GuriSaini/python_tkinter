import csv

f = open('file.csv', 'w')

with f:
    
    fnames = ['first_name', 'last_name']
    writer = csv.DictWriter(f, fieldnames=fnames)    

    writer.writeheader()
    writer.writerow({'first_name' : 'John', 'last_name': 'Smith'})
    writer.writerow({'first_name' : 'Robert', 'last_name': 'Brown'})
    writer.writerow({'first_name' : 'Julia', 'last_name': 'Griffin'})




# from csv import DictReader
# from csv import DictWriter

# # with open('file.csv','r') as rf:
# #     csv_read = DictReader(rf)
# #     count_mobile = 0 
# #     for row in csv_read:
# #           print(len(row))


# # from csv import reader

# # with open('file.csv','r') as rf:
# #     csv_reader = reader(rf)
# #     next(csv_reader)
# #     for row in csv_reader:
# #         print(row)\


# #wite method 

# with open('file.csv','w',newline="") as wf:
#     csv_writer = DictWriter(wf,fieldnames=['name','mobile'])
#     csv_writer.writeheader()
#     csv_writer.writerows([{'name':'guri','age':8}])