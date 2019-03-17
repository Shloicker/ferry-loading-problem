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
for k in range(1, 51):
    lanes = [[] for i in range(numLanes)]
    cars_in_overflow = []
    ferry.iterated_process_no_input(ferry.get_fullest_lane, cars, lanes, lane_length, cars_in_overflow, k)
    measures_of_cars_in_overflow.append(sum(cars_in_overflow))

# finding the k value with the least cars in overflow
min_k_value = measures_of_cars_in_overflow.index(min(measures_of_cars_in_overflow)) + 1
print(min_k_value)
# verifying the k value
lanes = [[] for i in range(numLanes)]
cars_in_overflow = []
ferry.iterated_process_no_input(ferry.get_fullest_lane, cars, lanes, lane_length, cars_in_overflow, min_k_value)
print(sum(cars_in_overflow))
print(min(measures_of_cars_in_overflow))

#plotting a line graph of k values
f = plt.figure()
plt.plot(range(1, 51), measures_of_cars_in_overflow)
plt.ylabel('Total Length of Cars in Overflow')
plt.xlabel("k values")
plt.title('Performance of Different k Values in Step Queuing Rule')
f.savefig("Performance of Different k Values in Step Queuing Rule.pdf")

# ------- Plotting Data for Five Queue System -------------

measures_of_cars_in_overflow = []
rules = [ferry.get_first_lane, ferry.get_emptiest_lane, ferry.get_fullest_lane, ferry.get_random_lane, ferry.get_most_suitable_lane]
for rule in rules:
    lanes = [[] for i in range(numLanes)]
    cars_in_overflow = []
    ferry.five_queues(rule, cars, lanes, lane_length, cars_in_overflow)
    measures_of_cars_in_overflow.append(sum(cars_in_overflow))

f = plt.figure()
rule_names = ["Get First Lane", "Get Emptiest Lane", "Get Fullest Lane", "Get Random Lane", "Get Most Suitable Lane"]
plt.bar(range(len(rule_names)), measures_of_cars_in_overflow)
plt.xticks(range(len(rule_names)), rule_names)
plt.ylabel("Total Length of Cars in Overflow")
plt.xlabel("Rules")
plt.title("Performance of Different Rules When Using the Five Queue System")
f.savefig("Performance of Different Rules When Using the Five Queue System.pdf")
