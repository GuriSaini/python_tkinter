def cube_finder(n):
    cube = {}
    for i in range(1,n+1):
        cube[i]=i**3
    return cube

num = int(input("Enter Number : "))
store = cube_finder(num)
print(store)

def word_counter(s):
    counter={}
    for i in s:
        counter[i] = s.count(i)
    return counter
str = input("Enter Name")
print(word_counter(str))