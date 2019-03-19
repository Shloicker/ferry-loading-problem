import random
import ferry
import matplotlib.pyplot as plt

# ------- Program that analyses performance of different rules with randomly generated sequences ----------

# the number of lanes and lane lengths are hard coded
numLanes = 85
lane_length = 3000

# we create a list of loading rules to iterate over. The list of strings will be used in the graph later
loading_rules = [ferry.get_first_lane, ferry.get_emptiest_lane, ferry.get_fullest_lane, ferry.get_random_lane, ferry.get_most_suitable_lane]
loading_rule_names = ["First", "Emptiest", "Fullest", "Random", "Most Suitable"]

repetitions = 10000                  # how many random sequences we will create for each loading rule

# -- Data Gathering for Simple Queue System --

rule_measures = []                  # a list containing the measures for each rule
for rule in loading_rules:
    measures = []                   # a list containing measures of total car length in overflow in each repetition
    for i in range(repetitions):
        lanes = [[] for i in range(numLanes)]                    # resetting our ferry and overflow park at each repetition
        cars_in_overflow = []

        # generating a random sequence of cars
        small_cars = [round(350 + 50*random.random()) for i in range(100)]
        medium_cars = [round(400 + 50*random.random()) for i in range(200)]
        large_cars = [round(450 + 50*random.random()) for i in range(100)]
        vans = [round(500 + 100*random.random()) for i in range(70)]
        lorries = [round(600 + 1400*random.random()) for i in range(30)]

        cars = small_cars + medium_cars + large_cars + vans + lorries
        random.shuffle(cars)

        ferry.one_queue(rule, cars, lanes, lane_length, cars_in_overflow)
        measures.append(sum(cars_in_overflow))

    average = sum(measures)/repetitions
    rule_measures.append(average)

# plotting a bar chart of the loading rules with simple queue
f = plt.figure()
plt.bar(range(len(loading_rule_names)), rule_measures)
plt.xticks(range(len(loading_rule_names)), loading_rule_names)
plt.xlabel("Loading Rules")
plt.ylabel("Total Car Length in Overflow")
plt.title("Average Measures of Rules with Random Sequences, Simple Queuing")
plt.savefig("Average Measures of Loading Rules with Random Sequences and Simple Queue.pdf")

# -- Data Gathering for Five Queue System --

# code virtually identical to previous --
rule_measures = []
for rule in loading_rules:
    measures = []
    for i in range(repetitions):
        lanes = [[] for i in range(numLanes)]
        cars_in_overflow = []

        small_cars = [round(350 + 50*random.random()) for i in range(100)]
        medium_cars = [round(400 + 50*random.random()) for i in range(200)]
        large_cars = [round(450 + 50*random.random()) for i in range(100)]
        vans = [round(500 + 100*random.random()) for i in range(70)]
        lorries = [round(600 + 1400*random.random()) for i in range(30)]

        cars = small_cars + medium_cars + large_cars + vans + lorries
        random.shuffle(cars)

        ferry.five_queues(rule, cars, lanes, lane_length, cars_in_overflow)
        measures.append(sum(cars_in_overflow))

    average = sum(measures)/repetitions
    rule_measures.append(average)

f = plt.figure()
plt.bar(range(len(loading_rule_names)), rule_measures)
plt.xticks(range(len(loading_rule_names)), loading_rule_names)
plt.xlabel("Loading Rules")
plt.ylabel("Total Car Length in Overflow")
plt.title("Average Measures of Rules with Random Sequences, Five Queues")
plt.savefig("Average Measures of Rules with Random Sequences, Five Queues.pdf")

# -- Data Gathering for Iterated Process --

# here we generate a large number of random sequences and perform the iterated process on each of them 50 times with 50 different k values
measures = [[] for i in range(50)]       # a list of 50 lists, each containing measures of each k value
for i in range(repetitions):
    small_cars = [round(350 + 50*random.random()) for i in range(100)]
    medium_cars = [round(400 + 50*random.random()) for i in range(200)]
    large_cars = [round(450 + 50*random.random()) for i in range(100)]
    vans = [round(500 + 100*random.random()) for i in range(70)]
    lorries = [round(600 + 1400*random.random()) for i in range(30)]

    cars = small_cars + medium_cars + large_cars + vans + lorries
    random.shuffle(cars)

    for k in range(1, 51):
        lanes = [[] for i in range(numLanes)]
        cars_in_overflow = []

        ferry.iterated_process_no_input(ferry.get_fullest_lane, cars, lanes, lane_length, cars_in_overflow, k)
        measures[k - 1].append(sum(cars_in_overflow))     # adding the measure to the appropriate list in 'measures'

averages = [sum(k_measures)/repetitions for k_measures in measures]  # generating the averages for each k value

# plotting a line graph of the performance of each k value
f = plt.figure()
plt.plot(range(1, 51), averages)
plt.xlabel("k Values")
plt.ylabel("Average Total Car Length in Overflow")
plt.title("Average Performance of k Values with Random Sequences")
plt.savefig("Average Performance of k Values with Random Sequences.pdf")
