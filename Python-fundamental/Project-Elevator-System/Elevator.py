from utils.util import Elevator

ele = Elevator()

# Setting Maximum and minimum floor levels in the building 
Topmost_floor = ele.errorHandlingMaxFloorIntegerValue()
Bottom_floor = ele.errorHandlingMinFloorIntegerValue()

# current floor value of the user, assuming the elevator is at the current floor
current = ele.errorHandlingCurrentFloorValue()
current_floor = ele.gettingValidCurrentFloorValue(current, Bottom_floor, Topmost_floor)

# Destination floor value, to which elevator is supposed to go from the current floor 
destination = ele.errorHandlingDestinationFloorValue()
destination_floor = ele.gettingValidDestinationValue(destination, Bottom_floor, Topmost_floor)

if current_floor == destination_floor:
    ele.showingDirection(current_floor, destination_floor)
else:
    ele.displayCurrentFloor(current_floor)
    ele.showingDirection(current_floor, destination_floor)
    ele.displayCurrentToDestinationFloors(current_floor,destination_floor)
    ele.displayDestinationFloor(destination_floor)