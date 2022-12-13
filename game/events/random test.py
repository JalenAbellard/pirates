import random
#guessedAlready = []
done = False
while done == False:
    x = random.randint(1,20)
    #guessedAlready.append(x)
    if x != 20:
        print (x)
    elif x == 20:
        print (x)
        print ("Done")
        done = True 
        

