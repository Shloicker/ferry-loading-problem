import ferry
import matplotlib.pyplot as plt

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

# -------- Plotting Data for Iterated Process ----------------
measures_of_cars_in_overflow = []
for k in range(1, 51):                            # applying the queuing rule using a range of k values
    lanes = [[] for i in range(numLanes)]
    cars_in_overflow = []
    ferry.iterated_process_no_input(ferry.get_fullest_lane, cars, lanes, lane_length, cars_in_overflow, k)
    measures_of_cars_in_overflow.append(sum(cars_in_overflow))

# finding the k value with the least cars in overflow
min_k_value = measures_of_cars_in_overflow.index(min(measures_of_cars_in_overflow)) + 1
print("\n\nBest k value:" + str(min_k_value))
print("\nTotal cars in overflow with best k value: " + str(min(measures_of_cars_in_overflow)))

#plotting a line graph of k values
f = plt.figure()
plt.plot(range(1, 51), measures_of_cars_in_overflow)
plt.ylabel('Total Length of Cars in Overflow')
plt.xlabel("k values")
plt.title('Performance of Different k Values in Iterated Process')
f.savefig("Performance of Different k Values in Iterated Process.pdf")

# ------- Plotting Data for Five Queue System -------------

# code is almost identical to task 1 but with five queue rule
rules = [ferry.get_first_lane, ferry.get_emptiest_lane, ferry.get_fullest_lane, ferry.get_random_lane, ferry.get_most_suitable_lane]
measures_of_cars_in_overflow = []
for rule in rules:
    if rule == ferry.get_random_lane:
        measures = []
        for i in range(1000):
            lanes = [[] for i in range(numLanes)]
            cars_in_overflow = []
            ferry.five_queues(ferry.get_random_lane, cars, lanes, lane_length, cars_in_overflow)
            measures.append(sum(cars_in_overflow))
        average = (sum(measures))/1000
        measures_of_cars_in_overflow.append(average)
        continue
    else:
        lanes = [[] for i in range(numLanes)]
        cars_in_overflow = []
        ferry.five_queues(rule, cars, lanes, lane_length, cars_in_overflow)
        print(measures_of_cars_in_overflow)
        measures_of_cars_in_overflow.append(sum(cars_in_overflow))

f = plt.figure()
rule_names = ['First', 'Emptiest', 'Fullest', 'Random(Avg)', 'Most Suitable']
plt.bar(range(len(rule_names)), measures_of_cars_in_overflow)
plt.xticks(range(len(rule_names)), rule_names)
plt.ylabel("Total Length of Cars in Overflow")
plt.xlabel("Rules")
plt.title("Performance of Different Rules when using the Five Queue System")
f.savefig("Performance of Different Rules when using the Five Queue System.pdf")
