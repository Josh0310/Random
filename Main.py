import numpy as np
#imports needed modules
n,atwork,c = 0,False,1000000
#defines atwork as initialy false
class car:
    def __init__(carname,cartitle, cos, atwork):
        carname.cartitle = cartitle
        carname.cos = cos
        carname.atwork = atwork
        carname.numberoftrips = 0
    #defines the car object constructor
carlot = [car("Car A",.45, False), car("Car B",.35, False), car("Car C",.20, False), car("Bus",1, False)]
#uses car lot as a way to store the cars statistics,plops constructors in array.
while n < c: #while n is less than the number of trips(10)
    for car in carlot:#for car in car lot
        if (car.atwork==atwork and np.random.binomial(1, car.cos, 1)): #if the cars atwork boolean is equivelant to that of the man's atwork boolean, AND the binomial method imported from numpy returns true
            atwork, car.atwork, car.numberoftrips,carlot[3].atwork = not atwork, not car.atwork, car.numberoftrips + 1,not atwork 
            break
         #invert atwork, invert the car's atwork boolean, add 1 to the car's number of trips, invert the bus's boolean to be whatever the man's is and break the for loop
    n = n+1
for car in carlot:
    print(car.cartitle + ":Number of Trips " + str(car.numberoftrips))
    print("----------------")
print("Total Days " + str(c/2))
#print statisitics
