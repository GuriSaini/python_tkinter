def odd_even(list):
    odd = []
    even = []
    for i in list:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    empty = [odd ,even]
    return empty

numbers = list(range(1,10))
print(odd_even(numbers))