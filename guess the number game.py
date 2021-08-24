n=45
print("total number of guess are 9")
guess =9
while(guess>0):
    print("enter the number")
    enter = int(input())
    
        print(enter," is smaller than the hidden number \n")
        guess = guess-1
        print("take passion you have some guess left ",guess)
        continue
    else :
        print("app jeet gaye \n")
        print("number of guesses you took to finish the game",9-guess)
        break
if guess==0:
    print("number of guess over ! you lost")