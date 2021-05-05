class Elevator(object):
    '''
    Constraints:
    Design is for residential building
    Default Values:
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
        import time

        if current < destination:
            for i in range(current+1,destination+1):
                print(i)
                time.sleep(1)
        elif current > destination:
            res_array = [x for x in range(destination, current)]
            for y in res_array[::-1]:
                print(y)
                time.sleep(1)
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
    
    def errorHandlingCurrentFloorValue(self):
        while True:
            try:
                current_fl = self.userInputCurrent()
                break
            except ValueError as ve:
                print("Enter an integer value, error is", ve)
        return current_fl

    def errorHandlingDestinationFloorValue(self):
        while True:
            try:
                destin_fl = self.userInputDestination()        
                break
            except ValueError as ve:
                print("Enter an integer value, error is", ve)
        return destin_fl
    
    def gettingValidDestinationValue(self, destin_fl, Bottom_floor, Topmost_floor):
        is_valid = self.validateDestination(destin_fl, Bottom_floor, Topmost_floor)
        reenter_destination_floor = destin_fl

        while is_valid != True:
            reenter_destination_floor = self.userInputDestination()
            is_valid = self.validateDestination(reenter_destination_floor, Bottom_floor, Topmost_floor)
        
        return reenter_destination_floor
    
    def gettingValidCurrentFloorValue(self,current, Bottom_floor, Topmost_floor):
        is_valid = self.validateCurrentFloor(current, Bottom_floor, Topmost_floor)
        reenter_current_floor = current

        while is_valid != True:
            reenter_current_floor = self.userInputCurrent()
            is_valid = self.validateCurrentFloor(reenter_current_floor, Bottom_floor, Topmost_floor)
        
        return reenter_current_floor
    
    def errorHandlingMaxFloorIntegerValue(self):
        while True:
            try:
                Top_floor = int(input("Design your own elevator, Start with entering the integer value for the topmost floor: "))
                break     
            except ValueError as ve:
                print("Enter an integer value, existing error is", ve)
        return Top_floor
    
    def errorHandlingMinFloorIntegerValue(self):
        while True:
            try:
                Bottom_floor = int(input("And the bottommost floor: "))
                break     
            except ValueError as ve:
                print("Enter an integer value less than or equal to 0, existing error is", ve)
        return Bottom_floor