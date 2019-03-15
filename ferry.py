import random

def printSol(lanes, lane_length, cars_in_overflow):
    # This procedure prints details of a solution to the screen.
    print("\nSOLUTION")
    for i in range(len(lanes)):
        print("Lane-" + str(i) + " = " + str(lanes[i]) + " (" + str(sum(lanes[i])) + " cm of " + str(lane_length) + " cm used)")
    print("Overflow = " + str(cars_in_overflow))
    print("Total length in overflow = " + str(sum(cars_in_overflow)) + " cm")

def get_first_lane(car):
    # returns the number of the first suitable lane for the car. Returns None if there is no suitable lane.
    for lane in range(len(lanes)):
        if sum(lanes[lane]) + car <= lane_length:
            return lane
    #If we are here, no lane is suitable.
    return None

def get_emptiest_lane(car):
    # returns the number of the emptiest lane that can fit the car. Returns None if there is no suitable lane.
    suitable_lanes = [lane for lane in range(len(lanes)) if sum(lanes[lane]) + car <= lane_length]
    if suitable_lanes == []:
        return None
    lanes_space_taken = [sum(lanes[lane]) for lane in suitable_lanes]
    least_space_taken = min(lanes_space_taken)
    for lane in suitable_lanes:
        if sum(lanes[lane]) == least_space_taken:
            return lane

def get_fullest_lane(car):
    # Returns the number of the fullest lane that can fit the car. Returns None if there is no suitable lane.
    suitable_lanes = [lane for lane in range(len(lanes)) if sum(lanes[lane]) + car <= lane_length]
    if suitable_lanes == []:
        return None
    lanes_space_taken = [sum(lanes[lane]) for lane in suitable_lanes]
    most_space_taken = max(lanes_space_taken)
    for lane in suitable_lanes:
        if sum(lanes[lane]) == most_space_taken:
            return lane

def get_random_lane(car):
    # Returns the number of a random lane that can fit the car. Returns None if there is no suitable lane.
    suitable_lanes = [lane for lane in range(len(lanes)) if sum(lanes[lane]) + car <= lane_length]
    if suitable_lanes == []:
        return None
    return random.choice(suitable_lanes)

def one_queue(rule):
    # simply applies a rule to each car in the queue in turn. Takes a lane selection rule as an argument (e.g. get random lane)
    for car in cars:
        lane = rule(car)
        if lane != None:
            lanes[lane].append(car)
        else:
            cars_in_overflow.append(car)

def five_queues(rule):
    # splits the queue into five queues with the different vehicle classes then sends the cars into lanes from lorries to small cars, using a given rule.
    car_types = [lorries, vans, large_cars, medium_cars, small_cars]
    for car_type in car_types:
        for car in car_type:
            lane = rule(car)
            if lane != None:
                lanes[lane].append(car)
            else:
                cars_in_overflow.append(car)

def one_queue_in_step(rule):
    # single queue but processes k cars at a time. The k cars are sorted from longest to shortest then enter the ferry in turn using a given rule.
    def process(car_batch):
        # a 'sub function' for processing the batch of k cars as this will be called twice
        car_batch.sort(reverse=True)                                             # sorts from longest to shortest
        for batch_car in car_batch:                                              # allocates each car to their lane using the given rule
            lane = rule(batch_car)
            if lane != None:
                lanes[lane].append(batch_car)
            else:
                cars_in_overflow.append(batch_car)
    while True:                                                                  # endless while loop in case user gives invalid input
        text = "\nEnter an integer between 0 and {}.\n\n".format(len(cars))      # asks for the k value to be used
        user_input = input(text)
        try:
            user_input = int(user_input)
        except ValueError:
            print("Enter an integer.")
            continue
        if user_input in range(len(cars)):
            k = user_input
            cars_to_be_processed = []
            for car in cars:
                cars_to_be_processed.append(car)
                if len(cars_to_be_processed) == k:                                # we only want to process the batch one it reaches the desired size
                    process(cars_to_be_processed)
                else:
                    continue                                                      # so we don't execute the following line if it hasn't reached the desired size
                cars_to_be_processed = []                                         # clears the batch since the cars in it have been processed
            process(cars_to_be_processed)                                         # this will process the remaining cars if we have reached the end of the queue
            break
        else:
            print("Enter an integer in the range.")
            continue

# the following dictionaries are for user input

rules = {"0. Choose first suitable lane." : get_first_lane, "1. Choose emptiest suitable lane." : get_emptiest_lane, "2. Choose fullest suitable lane." : get_fullest_lane, "3. Choose random suitable lane." : get_random_lane}

queuing_rules = {"0. Single queue." : one_queue, "1. Single queue in step. Cars are processed in a single queue but k at a time. The k cars are sorted from longest to shortest and then enter the ferry in turn." : one_queue_in_step, "2. Five queues for different classes. The queues are proccessed in turn, starting with lorries and ending with small cars." : five_queues}

rule_keys = [key for key in rules.keys()]
queue_keys = [key for key in queuing_rules.keys()]

# Main Program -------------------------------------------------------------

cars = []
with open("input.txt","r") as f:
    lane_length = int(f.readline())
    numLanes = int(f.readline())
    for line in f:
        cars.append(int(line))
# creating lists of different car types
small_cars = [car for car in cars if car in range(350, 400)]
medium_cars = [car for car in cars if car in range(400, 450)]
large_cars = [car for car in cars if car in range(450, 500)]
vans = [car for car in cars if car in range(500, 600)]
lorries = [car for car in cars if car in range(600, 2000)]

# Having read in the file, output some information to the screen
print("Number of vehicles           = " + str(len(cars)))
print("Total length of vehicles     = " + str(sum(cars)) + " cm")
print("Number of lanes              = " + str(numLanes))
print("Capacity per lane            = " + str(lane_length) + " cm")
print("List of all vehicle lengths  = " + str(cars))

while True:                                                                         # endless while loop for user input

    # Now declare the data structures used for storing the vehicles in each lane
    # and the vehicles in the overflow
    lanes = [[] for i in range(numLanes)]
    cars_in_overflow = []

    text = "\n\nType an integer to choose from one of the following queuing rules:\n\n" + "\n".join(queue_keys) + "\n\n"  #text for user input
    user_input = input(text)
    try:
        user_input = int(user_input)
    except ValueError:
        print("Enter an integer.")
        continue
    if user_input in range(len(queuing_rules)):
        queuing_rule = queuing_rules[queue_keys[user_input]]
    else:
        print("Enter an integer in the range.")
    text = "\n\nType an integer to choose from one of the following rules:\n\n" + "\n".join(rule_keys) + "\n\n"
    user_input = input(text)
    try:
        user_input = int(user_input)
    except ValueError:
        print("Enter an integer.")
        continue
    if user_input in range(len(rules)):
        rule = rules[rule_keys[user_input]]
    else:
        print("Enter an integer in the range.")
        continue
    queuing_rule(rule)                                         # finally calls the desired queuing rule with the desired lane allocation rule as the argument

    printSol(lanes, lane_length, cars_in_overflow)             # prints details of the solution