# Task

Roadspeed = int(input("enter the road speed: "))
Carspeed = int(input("Enter the speed of the car: "))

# we make the point 0 and increase if it need to
Points = 0

if Carspeed < Roadspeed:
    print("OK")
else:
    while Carspeed > Roadspeed:
        Carspeed -= 5
        Points += 1
        print("point: " + str(Points))
    if  Points > 12:
        print("Time to go to jail")
