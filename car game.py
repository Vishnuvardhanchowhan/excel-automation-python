import math
print('''start - to start the car
stop - to stop the car
quit - to exit''')
distance_cov=0
total_time=0
while(True):
    get_command=input("enter command:")
    if get_command=="start":
        print("car started... ready to 'go'!")
        print("                             ")
        time = 0
        acceleration = 1;
        print('''go - to move the car
stop - to stop the car and turn off''')
        while(time<=100):
            get_command2 = input("enter command:")
            if get_command2=="go":
                velocity=acceleration*time
                distance = velocity * time
                time+=1
                acceleration+=0.2
                print(f'acceleration is {acceleration}m/s^2 and velocity is {velocity}m/s '
                      f'and distance covered after last stop point is {distance}m.')
                print("_"*math.ceil(distance*0.1),"/*---*\.")
            elif get_command2=="start":
                print("car is already started bro!")
            elif get_command2=="stop":
                distance_cov=distance+distance_cov
                total_time=time+total_time
                print(f'distance travelled by car is {distance}m within {time} seconds,'
                      f' total distance covered till now is {distance_cov}m in {total_time} seconds.')
                print("_" * math.ceil(distance_cov), "/*---*\.")
                time=101
            elif get_command2 == "help":
                print('''go - to move the car
stop - to stop the car and turn off''')
            else :
                print("retype command correctly!")
    elif get_command=="stop":
        if get_command=="stop"and get_command2=="stop":
            print("car is already stopped!,type any other command.")
        else:
            print("car stopped!")
    elif get_command == "help":
        print('''start - to start the car
stop - to stop the car
quit - to exit''')
    elif get_command=="quit":
        break
    else:
        print("I dont fucking understand it!")