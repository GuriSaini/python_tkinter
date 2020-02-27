def sqaure_number(list):
    empty = []
    for i in list:
        empty.append(i*i)
    return empty
def reversed_items(list):
    return list[::-1]

def reversed_words(list):
    empty = [i[::-1] for i in list]
    return empty 

# numbers = list(range(1,11))
words = ['abc','tuv','xyz']
# print("Sqaure Number List ")
# print(sqaure_number(numbers))
# print("Reversed Number List")
# print(reversed_items(numbers))
print(f"List of Words {words}")
print("After Reverse")
print(reversed_words(words))


