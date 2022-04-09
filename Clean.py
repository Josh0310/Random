import numpy as np #imports needed modules
atwork,n = False, 0 #defines atwork as false(he starts at home), n as 0(this is used for the while loop later)
carlot = [["CarA",.45,0,False],["CarB",.35,0,False],["CarC",.20,0,False],["Bus",1,0,False]]  #stores cars and their stats in a 2D Array.[carname,chance of starting,number of trips, atwork boolean]
while n < 100000:  #while n is less than the number of trips(I just do 100,000 as an example)
    for car in carlot:
       if (car[3]==atwork and np.random.binomial(1, car[1], 1)):  #if the cars atwork boolean is equivelant to that of the man's atwork boolean, AND the binomial method imported from numpy returns true
            atwork, car[3], car[2] ,(carlot[3][3]) = not atwork, (not car[3]), car[2] + 1,not atwork
            break
        #invert atwork, invert the car's atwork boolean, add 1 to the car's number of trips, invert the bus's boolean to be whatever the man's is and break the for loop
    n = n+1
print("Total Days: " + str((carlot[0][2]+ carlot[1][2] + carlot[2][2] + carlot[3][2])/2) + "\n" + str(carlot[0]) + "\n" + str(carlot[1]) + "\n" + str(carlot[2]) + "\n" + str(carlot[3]) + "\n")
#prints stats

