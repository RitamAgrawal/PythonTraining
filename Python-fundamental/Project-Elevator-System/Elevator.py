class Elevator(object):
    '''
    Constraints:
    Design is for residential building
    By default:
    No. of elevators = 1
    No. of floors = 5
    No. of basement floors = 2
    '''
    def __init__ (self):
        pass

    def validateCurrentFloor(self, current, start_floor=-2, end_floor=5):
        if current in range(start_floor,end_floor+1):
            return True
        else:
            print("Please enter a valid current floor ranging between {} and {}".format(start_floor,end_floor))
    
    def validateDestination (self, destination, start_floor=-2, end_floor=5):
        if destination in range(start_floor,end_floor+1):
            return True
        else:
            print("Please enter a valid destination ranging between {} and {}".format(start_floor,end_floor))

    def displayCurrentFloor (self, current):
        print("You are at floor {}".format(current))
        return

    def displayDestinationFloor (self, destination):
        print("You have reached at floor {}, your destination.".format(destination))

    def displayCurrentToDestinationFloors (self, current, destination):
        if current < destination:
            for i in range(current+1,destination+1):
                print(i)
        elif current > destination:
            res_array = [x for x in range(destination, current)]
            for y in res_array[::-1]:
                print(y)
        return

    def showingDirection (self, current, destination):
        if current < destination:
            print("Going UP...")
        elif current > destination:
            print("Going Down...")
        else:
            print("You are at the same floor as the destination")
        return
    
    def userInputCurrent(self):
        current_floor = int(input("Enter your current floor: "))
        # elevator_direction = input("Enter + for Up and - for Down: ")
        return current_floor

    def userInputDestination(self):
        destination_floor = int(input("Enter your destination floor: "))
        return destination_floor

Topmost_floor = 7
Bottom_floor = -3
ele = Elevator()

while True:
    try:
        current_fl = ele.userInputCurrent()
        break
    except ValueError as ve:
        print("Enter an integer value, error is", ve)

current = current_fl
val1 = ele.validateCurrentFloor(current, Bottom_floor, Topmost_floor)
reenter_current_floor = current

while val1 != True:
    reenter_current_floor = ele.userInputCurrent()
    val1 = ele.validateCurrentFloor(reenter_current_floor, Bottom_floor, Topmost_floor)
current_fl = reenter_current_floor


while True:
    try:
        destin_fl = ele.userInputDestination()        
        break
    except ValueError as ve:
        print("Enter an integer value, error is", ve)


def test(destin_fl, Bottom_floor, Topmost_floor):
    val = ele.validateDestination(destin_fl, Bottom_floor, Topmost_floor)
    #if returns True then only run the elevator else start taking input again.
    if val == True:
        ele.displayCurrentFloor(current_fl)
        ele.showingDirection(current_fl, destin_fl)
        ele.displayCurrentToDestinationFloors(current_fl,destin_fl)
        ele.displayDestinationFloor(destin_fl)
    else:
        reenter_destination = ele.userInputDestination()
        test(reenter_destination, Bottom_floor, Topmost_floor)

test(destin_fl, Bottom_floor, Topmost_floor)