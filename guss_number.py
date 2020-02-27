# Gussing Number Game 
import random 
winning_number = random.randint(1,100)
gussing_num = int(input("Enter number between 1 to 100 : "))
if winning_number == gussing_num :
    print("YOU WIN !!!")
else: 
    if(gussing_num < winning_number):
        print("Too Low")
    else:
        print("Too High")