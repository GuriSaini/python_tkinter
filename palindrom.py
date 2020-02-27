def is_palindrom(word):
      name = word[-1::-1]
      if(word == name):
          return True
      else:
          return False
name = input("Enter the word : ")

print(is_palindrom(name))

