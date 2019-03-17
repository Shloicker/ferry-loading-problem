import ferry
import matplotlib.pyplot as plt
import random

cars = []
with open("input.txt","r") as f:
    lane_length = int(f.readline())
    numLanes = int(f.readline())
    for line in f:
        cars.append(int(line))

rules = [ferry.get_first_lane, ferry.get_emptiest_lane, ferry.get_fullest_lane, ferry.get_random_lane, ferry.get_most_suitable_lane]
measures_of_cars_in_overflow = []
for rule in rules:
    if rule == ferry.get_random_lane:
        measures = []
        for i in range(1000):
            lanes = [[] for i in range(numLanes)]
            cars_in_overflow = []
            ferry.one_queue(ferry.get_random_lane, cars, lanes, lane_length, cars_in_overflow)
            measures.append(sum(cars_in_overflow))
        average = (sum(measures))/1000
        measures_of_cars_in_overflow.append(average)
        continue
    else:
        lanes = [[] for i in range(numLanes)]
        cars_in_overflow = []
        ferry.one_queue(rule, cars, lanes, lane_length, cars_in_overflow)
        print(measures_of_cars_in_overflow)
        measures_of_cars_in_overflow.append(sum(cars_in_overflow))

rule_names = ['First', 'Emptiest', 'Fullest', 'Random(Avg)', 'Most Suitable']
f = plt.figure()
plt.bar(range(len(rule_names)), measures_of_cars_in_overflow)
plt.xticks(range(len(rule_names)), rule_names)
plt.ylabel("Total Cars in Overflow")
plt.xlabel("Allocation Rule Used")
plt.title("Performance of Allocation Rules with a Simple Queue")
plt.savefig("Performance of Allocation Rules with a Simple Queue.pdf")
