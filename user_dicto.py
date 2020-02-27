user ={}
name = input("Enter Name : ")
age  = int(input("Enter Age : "))

user['name'] = name
user['age']  = age
for key,values in user.items():
    print(f"{key}:{values}")