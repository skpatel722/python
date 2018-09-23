from random import randint 
rand = randint(1,100)
#print(rand)
print('''INSTRUCTIONS:
    1.player's guess should not be less than 1 or greater than 100
    2.On player's first turn, if their guess is 
      within 10 of the number, response is "WARM"
      but if further than 10 away from the number, return "COLD"
    3.On all subsequent turns, if a guess is
      closer to the number than the previous guess return "WARMER"
      farther from the number than the previous guess, return "COLDER"
    4.when the number is guessed correctly,
      the total count of your guesses is shown
    5. i am waiting to see who is the luckiest''')
count=0
i=0
z=[0,0]
y_o=0
y_n=0
try:
   while True:
    
    while True:
        x=int(input())
        if x>0 and x>100:
            continue
        else:
            y=x
            count+=1
            break
    if y==rand :
        print('you guessed it')
        break
    if  y<=rand+10 and y>=rand-10:
        print('WARM')
        y=int(input())
        #z[1]=y
       # z[2]=y
        y_o=y
        y_n=y
        count+=1
        
        if y==rand :
            print('you guessed it')
            break
        while y!=rand :
            #print(abs(y_n-rand) , abs(y_o-rand))
            if  (y<=rand+(10-i) and y>=rand-(10-i)) and abs(y_n-rand)<=abs(y_o-rand) :
                print('WARMER')
                y=int(input())
             #   z[2]=y
                y_o=y_n
                y_n=y
                count+=1
                if y==rand :
                    print('you guessed it')
                    break
            else:
                print('COLDER')
                i=i-1
                y=int(input())
                y_o=y_n
                y_n=y
                if y==rand :
                    print('you guessed it')
                    break
                count+=1
            i+=1
        
       
    else :
        print('COLD')
        count+=1
        continue
    i+=1
except:
   pass
finally:
   print('************ count = {} *************'.format(count) )
    



    