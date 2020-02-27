def greater(a,b):
     if a>b:
         return a
     else:
         return b
num1 = int(input("Enter number A : "))
num2 = int(input("Enter number B : "))

result = greater(num1,num2)

print(f"{result} is bigger")