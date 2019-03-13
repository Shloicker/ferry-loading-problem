import random

def printSol(lanes, lane_length, cars_in_overflow):
    # This procedure prints details of a solution to the screen.
    print("\nSOLUTION")
    for i in range(len(lanes)):
        print("Lane-" + str(i) + " = " + str(lanes[i]) + " (" + str(sum(lanes[i])) + " cm of " + str(lane_length) + " cm used)")
    print("Overflow = " + str(cars_in_overflow))
    print("Total length in overflow = " + str(sum(cars_in_overflow)) + " cm")

def get_first_lane(car_length, lanes):
    # Find functions returns the number of the first suitable lane for the current car.
    # It returns None is there is no suitable lane
    for lane in range(len(lanes)):
        if sum(lanes[lane]) + car_length <= lane_length:
            return lane
    #If we are here, no lane is suitable.
    return None

def get_emptiest_lane(car_length, lanes):
    # Finds the emptiest lane that can fit the car. Returns None if there is no suitable lane.
    suitable_lanes = [lane for lane in range(len(lanes)) if sum(lanes[lane]) + car_length <= lane_length]
    if suitable_lanes == []:
        return None
    lanes_space_taken = [sum(lanes[lane]) for lane in suitable_lanes]
    least_space_taken = min(lanes_space_taken)
    for lane in suitable_lanes:
        if sum(lanes[lane]) == least_space_taken:
            return lane

def get_fullest_lane(car_length, lanes):
    # Finds the fullest lane that can fit the car. Returns None if there is no suitable lane.
    suitable_lanes = [lane for lane in range(len(lanes)) if sum(lanes[lane]) + car_length <= lane_length]
    if suitable_lanes == []:
        return None
    lanes_space_taken = [sum(lanes[lane]) for lane in suitable_lanes]
    least_space_taken = max(lanes_space_taken)
    for lane in suitable_lanes:
        if sum(lanes[lane]) == least_space_taken:
            return lane

def get_random_lane(car_length, lanes):
    # Finds a random lane that can fit the car. Returns None if there is no suitable lane.
    suitable_lanes = [lane for lane in range(len(lanes)) if sum(lanes[lane]) + car_length <= lane_length]
    if suitable_lanes == []:
        return None
    return random.choice(suitable_lanes)

rules = {"0. Choose first suitable lane." : get_first_lane, "1. Choose emptiest suitable lane." : get_emptiest_lane, "2. Choose fullest suitable lane." : get_fullest_lane, "3. Choose random suitable lane." : get_random_lane}
keys = [key for key in rules.keys()]

# Main Program -------------------------------------------------------------
# First read in the problem file. All car lengths are put into the list L
cars = []
with open("input.txt","r") as f:
    lane_length = int(f.readline())
    numLanes = int(f.readline())
    for line in f:
        cars.append(int(line))

# Having read in the file, output some information to the screen
print("Number of vehicles           = " + str(len(cars)))
print("Total length of vehicles     = " + str(sum(cars)) + " cm")
print("Number of lanes              = " + str(numLanes))
print("Capacity per lane            = " + str(lane_length) + " cm")
print("List of all vehicle lengths  = " + str(cars))

while True:

    # Now declare the data structures used for storing the vehicles in each lane
    # and the vehicles in the overflow
    lanes = [[] for i in range(numLanes)]
    cars_in_overflow = []

    # Here is the basic algorithm. It takes each vehicle in turn and places it
    # into the first lane observed to have sufficient capacity. When no suitable
    # lane exists, the vehcile is put into the overflow list instead

    text = "\n\nType an integer to choose from one of the following rules:\n\n" + "\n".join(keys) + "\n\n"
    user_input = input(text)
    try:
        user_input = int(user_input)
    except ValueError:
        print("Enter an integer.")
        continue
    if user_input in range(len(rules)):
            rule = rules[keys[user_input]]
    else:
        print("Enter an integer in the range.")
        continue
    for i in range(len(cars)):
        car_length = cars[i]
        lane = rule(car_length, lanes)
        if lane != None:
            lanes[lane].append(car_length)
        else:
            cars_in_overflow.append(car_length)

    # Print details of the solution to the screen
    printSol(lanes, lane_length, cars_in_overflow)
