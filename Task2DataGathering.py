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

measures_of_cars_in_overflow = []
for k in range(1, 51):
    lanes = [[] for i in range(numLanes)]
    cars_in_overflow = []
    ferry.one_queue_in_step_no_input(ferry.get_fullest_lane, cars, lanes, lane_length, cars_in_overflow, k)
    measures_of_cars_in_overflow.append(sum(cars_in_overflow))

f = plt.figure()
plt.plot(range(1, 51), measures_of_cars_in_overflow)
plt.ylabel('Total Length of Cars in Overflow')
plt.xlabel("k values")
plt.title('Performance of Different k Values in Step Queuing Rule')
f.savefig("Performance of Different k Values in Step Queuing Rule.pdf")