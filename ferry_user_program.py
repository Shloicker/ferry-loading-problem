import ferry

# the following dictionaries are for user input

rule_keys = ["0. Choose first suitable lane.", "1. Choose emptiest suitable lane.", "2. Choose fullest suitable lane.", "3. Choose a random suitable lane.", "4. Choose the emptiest lane for lorries and vans, fullest lane otherwise."]
rules = [ferry.get_first_lane, ferry.get_emptiest_lane, ferry.get_fullest_lane, ferry.get_random_lane, ferry.get_most_suitable_lane]

queue_keys = ["0. Single queue.", "1. Five queues for different classes. The queues are proccessed in turn, starting with lorries and ending with small cars.", "2. Single queue in step. Cars are processed in a single queue but k at a time. The k cars are sorted from longest to shortest and then enter the ferry in turn."]
queues = [ferry.one_queue, ferry.five_queues, ferry.one_queue_in_step]

# Main Program -------------------------------------------------------------

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
    if user_input in range(len(queues)):
        queuing_rule = queues[user_input]
        print(queue_keys[user_input])
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
        rule = rules[user_input]
        print(rule_keys[user_input])
    else:
        print("Enter an integer in the range.")
        continue
    queuing_rule(rule, cars, lanes, lane_length, cars_in_overflow)                                         # finally calls the desired queuing rule with the desired lane allocation rule as the argument

    ferry.printSol(lanes, lane_length, cars_in_overflow)             # prints details of the solution