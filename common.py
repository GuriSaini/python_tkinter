def common(list,list2):
    empty_list = []
    for i in list:
        if i in list2:
            empty_list.append(i)
    return empty_list
def list_count(l):
    count = 0
    for i in l:
        if type(i)== list:
            count += 1
    return count

numbers = [1,2,3,4,5]
number  = [2,4,4,6,7]
print(common(numbers,number))

mix = [[1,2,3],[1,2,3],[4,5,6]]
print(list_count(mix))

tupl = ([1,2,3],)
tupl[0].append('h')
print(tupl)