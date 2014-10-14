#oddNum = 1
#while (oddNum < 300):
   # print oddNum
    #oddNum = oddNum + 2
    
#list1 = [1,2,3,4,5,6,7,8,9,10]
#index = 0

#while (index < len(list1)):
    #print list1[index]
    #index = index + 1
    
import random
rand = random.randint(0,50)
guess = 52

while guess != rand:
    print "Guess a number"
    guess = raw_input()
    if guess != rand:
        print "Incorrect!"
    else print "Correct!"