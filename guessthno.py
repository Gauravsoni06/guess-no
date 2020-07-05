import random
class guessno:
    def __init__(self,l,r):
        b=random.randint(-r,r)
        self.l1=0
        print("\nGuess The Number")
        while l>self.l1:
            
            print("\nYou have",l,"moves and the number is between",-r,"and",r)
            c=int(input("Enter the number "))
            if c<b:
                print("\n",c," is less than the number")
            elif c>b:
                print("\n",c," is greater than the number")
            else:
                print("\nGreat! you did it the number is ",c,"now you should try next level")
                break
            l=l-1
        print("game over")
print("********wellcome to the game**********")
while 1:
    level=int(input('''choose the level\n1 for beginner\n2 for easy\n3 for medium\n4 for hard\nenter the level form above'''))
    if level==1:
        level=40
    elif level==2:
        level=30
    elif level==3:
        level=20
    else:
        level=10
    r=int(input("choose the range\n1 for 100\n2 for 500\n3 for 1000\nenter your choice "))
    if r==1:
        r=100
    elif r==2:
        r=500
    else:
        r=1000
    guessno(level,r) 
    while(True):   
        t=input("want to play again y/n?")
        if t=="n":
            print("thank you for playing")
            break
        else:            
            k=input("with same configuration y/n?")
            if k=="y":
                guessno(level,r)
            else:
                continue
    if k=='n':
        k=False
        continue
    else:
        break      
        
        
            
    
