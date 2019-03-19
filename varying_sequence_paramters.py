import random
import ferry
import matplotlib.pyplot as plt

# to test the effects of changing lane length and number of lanes we will use the best performing queuing and loading rule from previous analysis,
# that is, the five queue system with the fullest lane rule

numLanes_measures = []
repetitions = 10000
for i in range(50, 121, 5):
    numLanes = i
    lane_length = round(2550/i) * 100
    print(lane_length)
    measures = []
    for j in range(repetitions):
        lanes = [[] for i in range(numLanes)]
        cars_in_overflow = []

        small_cars = [round(350 + 50*random.random()) for i in range(100)]
        medium_cars = [round(400 + 50*random.random()) for i in range(200)]
        large_cars = [round(450 + 50*random.random()) for i in range(100)]
        vans = [round(500 + 100*random.random()) for i in range(70)]
        lorries = [round(600 + 1400*random.random()) for i in range(30)]

        cars = small_cars + medium_cars + large_cars + vans + lorries
        random.shuffle(cars)

        ferry.five_queues(ferry.get_fullest_lane, cars, lanes, lane_length, cars_in_overflow)
        measures.append(sum(cars_in_overflow))
    average = sum(measures)/repetitions
    numLanes_measures.append(average)

f = plt.figure()
plt.plot(range(50, 121, 5), numLanes_measures)
plt.xlabel("Number of Lanes")
plt.ylabel("Total Length of Cars in Overflow")
plt.title("Performance of Best System with Different Number of Lanes")
plt.savefig("Performance of Best System with Different Number of Lanes.pdf")
